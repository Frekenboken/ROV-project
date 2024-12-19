from piservo import Servo
from gpiozero import CPUTemperature
import threading
import cv2
import sys
import pynmea2
import RPi.GPIO as gpio
import time
import psutil
from queue import Queue
import zmq
import cv2
import base64

from connections import gps_connection, arduino_connection
from PID import PIDController


def millis():
    return round(time.time() * 1000)


def open_connection_on(address):
    context = zmq.Context()
    socket = context.socket(zmq.PAIR)
    socket.bind(address)
    return socket, context


def close_context(context):
    context.term()


class Nord:
    def __init__(self, motor_pins, servo_pins, camera_pin):
        self.motors = (Servo(motor_pins[0]),
                       Servo(motor_pins[1]),
                       Servo(motor_pins[2]),
                       Servo(motor_pins[3]))
        self.servos = (Servo(servo_pins[0]),
                       Servo(servo_pins[1]),
                       Servo(servo_pins[2]),
                       Servo(servo_pins[3]))
        self.camera_servo = Servo(camera_pin)

        self.arduino_address = '/dev/ttyUSB0'
        self.arduino_speed = 38400
        self.arduino_timeout = 0.02

        self.gps_address = '/dev/ttyACM0'
        self.gps_speed = 19200
        self.gps_timeout = 0.011

        self.connection_address = "tcp://*:5555"

        self.sensors = {name: 0 for name in
                        ['depth_target', 'gx', 'gy', 'temp_on', 'humidity_on', 'pressure_on', 'temp_out', 'depth',
                         'sat',
                         'lat', 'lat_dir',
                         'lon', 'lon_dir',
                         'speed', 'track', 'cpu_temp', 'cpu_usage', 'time', 'date']}

        self.depth_pid = PIDController(0.01, 0.0001, 0.1)
        self.depth_pid.set_limit(10, 170)
        self.depth_pid.set_offset(90)

        self.roll_pid = PIDController(0.01, 0.0001, 0.1)
        self.roll_pid.set_limit(-5, 5)
        self.roll_pid.set_offset(0)

        self.pitch_pid = PIDController(0.01, 0.0001, 0.1)
        self.pitch_pid.set_limit(-5, 5)
        self.pitch_pid.set_offset(0)

        self.q = Queue()

        print('Loading...')

        self.socket, self.context = open_connection_on(self.connection_address)
        print(f'Connection is open on {self.connection_address}!')

        # Инициализация камеры
        self.cap = cv2.VideoCapture(0)
        self.cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
        self.cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)
        print('Camera is connected!')

        print('Done!')

    def set_arduino(self, **kwargs):
        if 'address' in kwargs.keys():
            self.arduino_address = kwargs.get('address')
        if 'speed' in kwargs.keys():
            self.arduino_speed = kwargs.get('speed')
        if 'timeout' in kwargs.keys():
            self.arduino_timeout = kwargs.get('timeout')

    def set_gps(self, **kwargs):
        if 'address' in kwargs.keys():
            self.gps_address = kwargs.get('address')
        if 'speed' in kwargs.keys():
            self.gps_speed = kwargs.get('speed')
        if 'timeout' in kwargs.keys():
            self.gps_timeout = kwargs.get('timeout')

    def get_sensors(self, key):
        return self.sensors.get(key)

    def get_sensors_dict(self):
        return self.sensors

    def update_sensors(self):
        ser_arduino = arduino_connection(self.arduino_address, self.arduino_speed, self.arduino_timeout)
        ser_gps = gps_connection(self.gps_address, self.gps_speed, self.gps_timeout)
        cpu = CPUTemperature()

        while True:
            if ser_gps and ser_gps.in_waiting > 0:
                line_gps = ser_gps.readline().decode('utf-8').rstrip()
                msg = pynmea2.parse(line_gps)
                if isinstance(msg, pynmea2.GGA):
                    self.sensors['sat'] = msg.num_sats
                    self.sensors['lat'] = msg.latitude
                    self.sensors['lat_dir'] = msg.lat_dir
                    self.sensors['lon'] = msg.longitude
                    self.sensors['lon_dir'] = msg.lon_dir
                if isinstance(msg, pynmea2.VTG):
                    self.sensors['track'] = msg.true_track
                    self.sensors['speed'] = msg.spd_over_grnd
                if isinstance(msg, pynmea2.RMC):
                    datetime = str(msg.datetime)  # 2024-01-17 16:17:30+00:00
                    self.sensors['date'] = datetime[:10]
                    self.sensors['time'] = datetime[11:19]

            if ser_arduino and ser_arduino.in_waiting > 0:
                arduino_data = ser_arduino.readline().decode('utf-8').rstrip().split(';')
                self.sensors['depth_target'] = float(arduino_data[0])
                self.sensors['fb'] = float(arduino_data[1])
                self.sensors['lr'] = float(arduino_data[2])
                self.sensors['rotate'] = float(arduino_data[3])
                self.sensors['control_mode'] = float(arduino_data[4])
                self.sensors['None'] = float(arduino_data[5])
                self.sensors['gx'] = float(arduino_data[6])
                self.sensors['gy'] = float(arduino_data[7])
                self.sensors['temp_on'] = float(arduino_data[8])
                self.sensors['humidity_on'] = float(arduino_data[9])
                self.sensors['pressure_on'] = int(arduino_data[10])
                self.sensors['temp_out'] = float(arduino_data[11])
                self.sensors['depth'] = int(arduino_data[12])
                self.sensors['gx_target'] = float(arduino_data[13])
                self.sensors['gy_target'] = float(arduino_data[14])
            self.sensors['cpu_temp'] = int(cpu.temperature)
            self.sensors['cpu_usage'] = int(psutil.cpu_percent())

    def step(self):
        depth_speed = self.depth_pid.compute(self.get_sensors('depth'), self.get_sensors('depth_target'))
        roll_speed = self.roll_pid.compute(self.get_sensors('gx'), self.get_sensors('gx_target'))
        pitch_speed = self.pitch_pid.compute(self.get_sensors('gy'), self.get_sensors('gy_target'))

        self.servos[0].write(depth_speed - roll_speed + pitch_speed)  # lf
        self.servos[1].write(depth_speed + roll_speed + pitch_speed)  # rf
        self.servos[2].write(depth_speed - roll_speed - pitch_speed)  # lb
        self.servos[3].write(depth_speed + roll_speed - pitch_speed)  # rb

    def send_data(self):  # передача всех данных оператору
        if not self.q.empty():
            frame = self.q.get_nowait()

        data_dict = nord.get_sensors_dict()

        # Кодирование изображения в base64
        _, encoded_frame = cv2.imencode('.jpg', frame)
        image_str = base64.b64encode(encoded_frame.tobytes()).decode('utf-8')

        # Отправка данных
        data = {'image': image_str, 'data_dict': data_dict}
        response = self.socket.recv_string()
        if response == 'c':
            print('Close connection.')
        self.socket.send_pyobj(data)
        # time.sleep(0.05)  # Задержка для управления частотой передачи кадров

    def put_frame_to_queue(self):
        suc, frame = self.cap.read()
        if suc and self.q.qsize() < 3:
            self.q.put(frame)

    def write_log(self):
        try:
            with open(f'logs/{self.get_sensors("date")}', 'a') as log:
                logline = f'{self.get_sensors("time")}: Sat: {self.get_sensors("sat")}, CPU%: ' \
                          f'{psutil.cpu_percent()}' + '\n'
                log.write(logline)
            print('SAVE LOG')
        except:
            print('Ошибка записи лога')

    def thread_log(self, delay=10000):
        t = millis()
        while True:
            if millis() - t > delay:
                self.write_log()
                t = millis()

    def thread_camera(self):
        while True:
            self.put_frame_to_queue()

    def thread_sender(self):
        while self.q.empty():
            pass
        while True:
            self.send_data()

    def start(self):
        camera = threading.Thread(target=self.thread_camera)
        sender = threading.Thread(target=self.thread_sender)
        log = threading.Thread(target=self.thread_log)

        camera.start()
        sender.start()
        log.start()

        while True:
            self.step()


if __name__ == '__main__':
    nord = Nord((1, 2, 3, 4), (5, 6, 7, 8), 9)
    nord.start()
