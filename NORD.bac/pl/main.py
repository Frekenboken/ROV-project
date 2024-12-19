from piservo import Servo
from gpiozero import CPUTemperature
import threading
import cv2
import sys
import serial
import pynmea2
import RPi.GPIO as gpio
import time
import psutil
import socket
from queue import Queue
import zmq
import cv2
import base64


class PIDController:
    def __init__(self, Kp, Ki, Kd):
        self.Kp = Kp
        self.Ki = Ki
        self.Kd = Kd
        self.prev_error = 0
        self.integral = 0

        self.min_output = 0
        self.max_output = 180
        self.offset = 0

    def compute(self, current_value, target):
        error = target - current_value
        self.integral += error
        derivative = error - self.prev_error

        raw_output = self.Kp * error + self.Ki * self.integral + self.Kd * derivative

        self.prev_error = error

        output = max(min(raw_output + self.offset, self.max_output), self.min_output)

        return output

    def set_limit(self, min_out, max_out):
        self.min_output = min_out
        self.max_output = max_out

    def set_offset(self, value):
        self.offset = value


def millis():
    return round(time.time() * 1000)


def gps_connection(self):
    try:
        serGPS = serial.Serial('/dev/ttyACM0', 19200, timeout=0.011)
        serGPS.flush()
        return serGPS
    except:
        return None


def arduino_connection(self):
    try:
        serArduino = serial.Serial('/dev/ttyUSB0', 38400, timeout=0.02)
        serArduino.flush()
        return serArduino
    except:
        return None


def data_stream():
    print('Loading...')
    while q.empty():
        pass
    context = zmq.Context()
    socket = context.socket(zmq.PAIR)
    socket.bind("tcp://*:5555")
    print('Done!')

    while True:

        if not q.empty():
            frame = q.get_nowait()

        # Пример списка данных (может быть вашим списком)
        data_dict = sensors

        # Кодирование изображения в base64
        _, encoded_frame = cv2.imencode('.jpg', frame)
        image_str = base64.b64encode(encoded_frame.tobytes()).decode('utf-8')

        # Отправка данных
        data = {'image': image_str, 'data_list': data_dict}
        response = socket.recv_string()
        if response == 'c':
            print('Close connection.')
            break
        socket.send_pyobj(data)
        # time.sleep(0.05)  # Задержка для управления частотой передачи кадров


def frame_stream():
    cap = cv2.VideoCapture(0)
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)
    while True:
        suc, frame = cap.read()
        if suc and not q.qsize():
            q.put(frame)


def update_sensors():
    t = millis()
    serGPS = GPS.connection()
    serArduino = Arduino.connection()
    cpu = CPUTemperature()

    while True:
        if serGPS and serGPS.in_waiting > 0:
            lineGPS = serGPS.readline().decode('utf-8').rstrip()
            msg = pynmea2.parse(lineGPS)
            if isinstance(msg, pynmea2.GGA):
                sensors['satellites'] = msg.num_sats
                sensors['lat'] = msg.latitude
                sensors['lat_dir'] = msg.lat_dir
                sensors['lon'] = msg.longitude
                sensors['lon_dir'] = msg.lon_dir
            if isinstance(msg, pynmea2.VTG):
                sensors['track'] = msg.true_track
                sensors['speed'] = msg.spd_over_grnd
            if isinstance(msg, pynmea2.RMC):
                datetime = str(msg.datetime)  # 2024-01-17 16:17:30+00:00
                sensors['date'] = datetime[:10]
                sensors['time'] = datetime[11:19]

        if serArduino and serArduino.in_waiting > 0:
            arduino_data = serArduino.readline().decode('utf-8').rstrip().split(',')
            sensors['gx'] = float(arduino_data[0])
            sensors['gy'] = float(arduino_data[1])
            sensors['temp_on'] = float(arduino_data[2])
            sensors['humidity_on'] = float(arduino_data[3])
            sensors['pressure_on'] = int(arduino_data[4])
            sensors['temp_out'] = float(arduino_data[5])
            sensors['depth'] = int(arduino_data[6])

        if millis() - t > 10000:
            try:
                with open(f'logs/{sensors["date"]}', 'a') as log:
                    logline = f'{sensors["time"]}: Sats: {sensors["satellites"]}, CPU%: {psutil.cpu_percent()}' + '\n'
                    log.write(logline)
                print('SAVE LOG')
                t = millis()
            except:
                print('Ошибка записи лога')

        sensors['cpu_temp'] = int(cpu.temperature)
        sensors['cpu_usage'] = int(psutil.cpu_percent())


def control():
    depth_pid = PIDController(0.01, 0.0001, 0.1)
    depth_pid.set_limit(10, 170)
    depth_pid.set_offset(90)

    roll_pid = PIDController(0.01, 0.0001, 0.1)
    roll_pid.set_limit(-5, 5)
    roll_pid.set_offset(0)

    pitch_pid = PIDController(0.01, 0.0001, 0.1)
    pitch_pid.set_limit(-5, 5)
    pitch_pid.set_offset(0)

    # Инициализация серво моторов емкостей
    left_front_servo, right_front_servo, left_back_servo, right_back_servo = Servo(), Servo(), Servo(), Servo()

    # Инициализация ходовых двигателей
    left_front_motor, right_front_motor, left_back_motor, right_back_motor = Servo(), Servo(), Servo(), Servo()

    camera_servo = Servo()

    while True:
        target_depth = 150
        target_roll = 0
        target_pitch = 0
        depth_speed = depth_pid.compute(sensors['depth'], target_depth)
        roll_speed = roll_pid.compute(sensors['gx'], target_roll)
        pitch_speed = pitch_pid.compute(sensors['gy'], target_pitch)
        left_front_servo.write(depth_speed - roll_speed + pitch_speed)
        right_front_servo.write(depth_speed + roll_speed + pitch_speed)
        left_back_servo.write(depth_speed - roll_speed - pitch_speed)
        right_back_servo.write(depth_speed + roll_speed - pitch_speed)


if __name__ == '__main__':
    sensors = {name: 0 for name in
               ['gx', 'gy', 'temp_on', 'humidity_on', 'pressure_on', 'temp_out', 'depth', 'depth_target', 'satellites',
                'lat', 'lat_dir',
                'lon', 'lon_dir',
                'speed', 'track', 'cpu_temp', 'cpu_usage', 'time', 'date']}
    q = Queue()

    data_thread = threading.Thread(target=data_stream)
    frame_thread = threading.Thread(target=frame_stream)
    update_sensors_thread = threading.Thread(target=update_sensors)
    control_thread = threading.Thread(target=control)
    data_thread.start()
    frame_thread.start()
    update_sensors_thread.start()
    # control_thread.start()
