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

# Параметры камеры
CAMERA_INDEX = 0
FRAME_WIDTH, FRAME_HEIGHT, FPS = 640, 480, 30

# Настройки сервера
ZMQ_PORT = 5555
SERIAL_PORT = "/dev/ttyUSB0"
SERIAL_BAUDRATE = 115200
SERIAL_TIMEOUT = 1
SHOW_MEMORY_USAGE_EVERY = 100  # Период вывода памяти в циклах

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
servos = [Servo(18), Servo(18), Servo(18), Servo(18)]
motors = [Servo(19), Servo(19), Servo(19), Servo(19)]

# Инициализация камеры
cap = cv2.VideoCapture(CAMERA_INDEX, cv2.CAP_V4L2)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, FRAME_WIDTH)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, FRAME_HEIGHT)
cap.set(cv2.CAP_PROP_FPS, FPS)
cap.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter_fourcc(*"MJPG"))

# Подключение к Arduino
try:
    ser = serial.Serial(SERIAL_PORT, SERIAL_BAUDRATE, timeout=SERIAL_TIMEOUT)
    time.sleep(2)  # Ожидание стабилизации соединения
except Exception as e:
    print(f"Ошибка подключения к Arduino: {e}")
    ser = None

# Настройка ZeroMQ
context = zmq.Context()
socket = context.socket(zmq.REP)
socket.bind(f"tcp://*:{ZMQ_PORT}")

# Флаг работы потока
running = True


def read_arduino_data():
    """Читает данные с Arduino."""
    if not ser:
        return [None] * 7  # Если нет соединения, возвращаем пустые данные

    try:
        line = ser.readline().decode("utf-8").strip()
        data = line.split(",")
        return data if len(data) >= 7 else [None] * 7
    except Exception as e:
        print(f"Ошибка чтения с Arduino: {e}")
        return [None] * 7


def pid_control_loop():
    """Фоновый поток для расчетов PID."""
    while running:
        print('c')
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

        time.sleep(0.05)  # Регулируем частоту выполнения


# Запуск PID в отдельном потоке
pid_thread = Thread(target=pid_control_loop, daemon=True)
# pid_thread.start()

print("Сервер запущен!")

frame_count = 0

while True:
    ret, frame = cap.read()
    if not ret:
        print("Ошибка чтения кадра с камеры!")
        continue

    # Кодируем изображение в JPEG
    _, buffer = cv2.imencode(".jpg", frame)
    jpg_as_text = buffer.tobytes()

    try:
        message = socket.recv_json()
        print(f"Получен запрос: {message}")

        # Читаем данные с Arduino
        arduino_data = read_arduino_data()

        # Отправляем изображение + JSON
        socket.send_multipart(
            [jpg_as_text,
             str({
                 "cpu_temperature": psutil.sensors_temperatures()["cpu_thermal"][0][1],
                 "cpu_usage": int(psutil.cpu_percent()),
                 "depth": arduino_data[0],
                 "gx": arduino_data[1],
                 "gy": arduino_data[2],
                 "in_temperature": arduino_data[3],
                 "in_humidity": arduino_data[4],
                 "in_pressure": arduino_data[5],
                 "out_temperature": arduino_data[6]
             }).encode()]
        )

        # Вывод информации о памяти каждые N циклов
        if frame_count == SHOW_MEMORY_USAGE_EVERY:
            memory_info = psutil.Process(os.getpid()).memory_info()
            print(f"RSS: {memory_info.rss / 1024 / 1024:.2f} MB, VMS: {memory_info.vms / 1024 / 1024:.2f} MB")
            frame_count = 0

        frame_count += 1

    except Exception as e:
        print(f"Ошибка связи с клиентом: {e}")

cap.release()
socket.close()
context.term()
running = False
pid_thread.join()
