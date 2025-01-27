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
import serial

from PID import PIDController


class Nord:
    def __init__(self, motor_pins, servo_pins, camera_pin):
        # self.motors = (Servo(motor_pins[0]),
        #                Servo(motor_pins[1]),
        #                Servo(motor_pins[2]),
        #                Servo(motor_pins[3]))
        # self.servos = (Servo(servo_pins[0]),
        #                Servo(servo_pins[1]),
        #                Servo(servo_pins[2]),
        #                Servo(servo_pins[3]))
        # self.camera_servo = Servo(camera_pin)

        self.ser = serial.Serial('/dev/ttyUSB0', 38400, timeout=1)

        self.depth_pid = PIDController(0.01, 0.0001, 0.1)
        self.depth_pid.set_limit(10, 170)
        self.depth_pid.set_offset(90)

        self.roll_pid = PIDController(0.01, 0.0001, 0.1)
        self.roll_pid.set_limit(-5, 5)
        self.roll_pid.set_offset(0)

        self.pitch_pid = PIDController(0.01, 0.0001, 0.1)
        self.pitch_pid.set_limit(-5, 5)
        self.pitch_pid.set_offset(0)

        self.sensors = []

        print('Loading...')

        # Инициализация камеры
        self.cap = cv2.VideoCapture(0)
        self.cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
        self.cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)
        print('Camera is connected!')

        self.context = zmq.Context()
        self.socket = self.context.socket(zmq.REP)
        self.socket.bind("tcp://*:5555")  # Привязываемся к порту 5555

        print("Сервер запущен и ожидает запросы...")


        print('Done!')

    def update_sensors(self):
        pass
        # self.sensors['cpu_temp'] = int(cpu.temperature)
        # self.sensors['cpu_usage'] = int(psutil.cpu_percent())

    def step(self):
        depth_speed = self.depth_pid.compute(self.get_sensors('depth'), self.get_sensors('depth_target'))
        roll_speed = self.roll_pid.compute(self.get_sensors('gx'), self.get_sensors('gx_target'))
        pitch_speed = self.pitch_pid.compute(self.get_sensors('gy'), self.get_sensors('gy_target'))

        self.servos[0].write(depth_speed - roll_speed + pitch_speed)  # lf
        self.servos[1].write(depth_speed + roll_speed + pitch_speed)  # rf
        self.servos[2].write(depth_speed - roll_speed - pitch_speed)  # lb
        self.servos[3].write(depth_speed + roll_speed - pitch_speed)  # rb

    def send_data(self):  # передача всех данных оператору
        suc, frame = self.cap.read()
        if not suc:
            return

        data_dict = self.get_sensors_dict()

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

    def start(self):
        timer_update_sensors = time.time()
        timer_comm = time.time()
        try:
            while True:
                if time.time() - timer_update_sensors > 1:
                    if self.ser.in_waiting > 0:
                        line = self.ser.readline().decode('utf-8').rstrip()
                        print(f"Received: {line}")
                    timer_update_sensors = time.time()

                if time.time() - timer_comm > 2:
                    # Получаем запрос от клиента
                    message = self.socket.recv_pyobj()
                    print(f"Получен запрос: {message}")

                    # Обрабатываем запрос (например, удваиваем каждый элемент списка)
                    response = [x * 2 for x in message]

                    # Отправляем ответ клиенту
                    self.socket.send_pyobj(response)
        except KeyboardInterrupt:
            print("Программа остановлена пользователем")
        finally:
            # Закрываем порт
            self.ser.close()


if __name__ == '__main__':
    nord = Nord((1, 2, 3, 4), (5, 6, 7, 8), 9)
    nord.start()
