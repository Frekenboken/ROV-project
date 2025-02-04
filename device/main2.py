import base64
import os
import cv2
import zmq
import serial
import time
import psutil
import numpy as np
from threading import Thread
from piservo import Servo
import RPi.GPIO as gpio
from gpiozero import CPUTemperature
from PID import PIDController

# Настройки
SERIAL_PORT = "/dev/ttyUSB0"
SERIAL_BAUDRATE = 115200
SERIAL_TIMEOUT = 0.5

# PID-контроллеры
depth_pid = PIDController(0.01, 0.0001, 0.1)
depth_pid.set_limit(10, 170)
depth_pid.set_offset(90)

roll_pid = PIDController(0.01, 0.0001, 0.1)
roll_pid.set_limit(-5, 5)
roll_pid.set_offset(0)

pitch_pid = PIDController(0.01, 0.0001, 0.1)
pitch_pid.set_limit(-5, 5)
pitch_pid.set_offset(0)

# Сервоприводы
servos = [Servo(12), Servo(18),
          Servo(18), Servo(18)]
motors = [Servo(19), Servo(19),
          Servo(19), Servo(19)]

# Инициализация камеры
cap = cv2.VideoCapture(0)

# Подключение к Arduino
ser = serial.Serial(SERIAL_PORT, SERIAL_BAUDRATE, timeout=SERIAL_TIMEOUT)
time.sleep(2)  # Ожидание стабилизации соединения


def map_value(value, from_min, from_max, to_min, to_max):
    # Проверяем, чтобы значения в исходном диапазоне не совпадали
    if from_min == from_max:
        raise ValueError("from_min и from_max не могут быть равными.")

    # Вычисляем, в какой пропорции находится value в исходном диапазоне
    from_range = from_max - from_min
    to_range = to_max - to_min
    scaled_value = (value - from_min) / from_range  # Нормализуем значение
    return to_min + (scaled_value * to_range)  # Преобразуем в новый диапазон


# Функция для установки угла для каждого сервомотора
def set_angle(pwm, angle):
    duty = (angle / 18) + 2  # Преобразуем угол в коэффициент заполнения
    pwm.ChangeDutyCycle(duty)


def read_arduino():
    if ser.in_waiting > 0:
        try:
            line = ser.readline().decode("utf-8").strip()
            data = line.split(",")

            if len(data) < 7:
                return [None] * 7  # Защита от неполных данных

            # print(f"Arduino: {line}")  # Логирование данных
            ser.reset_input_buffer()  # Очищаем входной буфер
            return data
        except Exception as e:
            print(f"Ошибка чтения с Arduino: {e}")

    return [None] * 7  # Если данных нет, возвращаем пустой список


def cam_and_data_send():
    context = zmq.Context()
    socket = context.socket(zmq.PAIR)
    socket.bind(f"tcp://*:5555")

    while True:
        suc, frame = cap.read()
        if not suc:
            print("Ошибка чтения камеры!")
            break

        # Кодирование изображения в base64
        _, encoded_frame = cv2.imencode('.jpg', frame)
        image_str = base64.b64encode(encoded_frame.tobytes()).decode('utf-8')

        arduino_data = read_arduino()

        # Отправка данных
        data = {'image': image_str, 'data': {'depth': arduino_data[0],
                                             'dy': arduino_data[1],
                                             'dx': arduino_data[2],
                                             'temperature_in': arduino_data[3],
                                             'humidity_in': arduino_data[4],
                                             'pressure_in': arduino_data[5],
                                             'temperature_out': arduino_data[6],
                                             'cpu_temperature': str(psutil.sensors_temperatures()["cpu_thermal"][0][1]),
                                             'cpu_usage': str(psutil.cpu_percent())}}
        response = socket.recv_string()
        if response == 'c':
            print('Close connection.')
        socket.send_pyobj(data)


def control_send():
    context2 = zmq.Context()
    socket2 = context2.socket(zmq.PAIR)
    socket2.bind("tcp://*:5556")

    gpio.setwarnings(False)
    gpio.setmode(gpio.BCM)

    # Настройка GPIO пинов для ШИМ
    pins = [19, 20, 21, 22]
    for pin in pins:
        gpio.setup(pin, gpio.OUT)

    # Создаем объекты PWM для каждого пина с частотой 50 Гц
    pwm_instances = [gpio.PWM(pin, 50) for pin in pins]

    # Запуск ШИМ сигналов с начальной шириной импульса 0%
    for pwm in pwm_instances:
        pwm.start(0)

    while True:
        try:
            response = socket2.recv_pyobj()
            print(response)
            data = {'status': 'ok'}
            socket2.send_pyobj(data)

            # servos[0].write(map_value(float(response['x']), -1, 1, 0, 180))

            # depth = 100  # Заглушка (здесь нужно получать реальные данные)
            # gx = 0
            # gy = 0
            #
            # depth_speed = depth_pid.compute(depth, 120)  # 120 - пример целевого значения
            # roll_speed = roll_pid.compute(gx, 0)
            # pitch_speed = pitch_pid.compute(gy, 0)
            #
            # servos[0].write(depth_speed - roll_speed + pitch_speed)
            # servos[1].write(depth_speed + roll_speed + pitch_speed)
            # servos[2].write(depth_speed - roll_speed - pitch_speed)
            # servos[3].write(depth_speed + roll_speed - pitch_speed)

            for pwm in pwm_instances:
                set_angle(pwm, map_value(float(response['x']), -1, 1, 0, 180))

        except KeyboardInterrupt:
            for pwm in pwm_instances:
                pwm.stop()  # Останавливаем ШИМ на всех портах
            gpio.cleanup()  # Очистка GPIO


cdt = Thread(target=cam_and_data_send)
# ct = Thread(target=control_send)
cdt.start()
# ct.start()

control_send()

print("Сервер запущен!")
