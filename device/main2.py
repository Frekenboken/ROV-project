import os
import time
import base64
import psutil
import zmq
import serial
import cv2
import numpy as np
from gpiozero import CPUTemperature
from piservo import Servo
from PID import PIDController


def main():
    print("Initialization... (5 sec)")

    # Инициализация ZeroMQ
    context = zmq.Context()
    socket = context.socket(zmq.REP)
    socket.bind("tcp://*:5555")

    # Настройки камеры
    cap = cv2.VideoCapture(0, cv2.CAP_V4L2)
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
    cap.set(cv2.CAP_PROP_FPS, 30)
    cap.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter_fourcc(*'MJPG'))

    # Настройки последовательного порта
    ser = serial.Serial('/dev/ttyUSB0', 115200, timeout=0.5)

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

    servos = [Servo(18), Servo(18), Servo(18), Servo(18)]
    motors = [Servo(19), Servo(19), Servo(19), Servo(19)]

    # Проверяем подключение к Arduino
    for i in range(10):
        if ser.in_waiting > 0:
            break
        time.sleep(0.5)
    else:
        raise Exception("No data from serial device")

    print("Ready!")

    while True:
        try:
            # Чтение кадра с камеры
            ret, frame = cap.read()
            if not ret:
                print("Failed to capture frame")
                continue

            _, buffer = cv2.imencode('.jpg', frame)
            jpg_as_text = buffer.tobytes()

            # Неблокирующий прием команды от клиента
            try:
                message = socket.recv_json(flags=zmq.NOBLOCK)
                print(f"Received control signal: {message}")
            except zmq.Again:
                pass  # Нет входящих сообщений

            # Чтение данных с Arduino
            arduino_data = [None] * 8  # Дефолтные значения
            if ser.in_waiting > 0:
                try:
                    line = ser.readline().decode('utf-8').rstrip()
                    arduino_data = line.split(",")
                    if len(arduino_data) < 8:
                        arduino_data = [None] * 8
                    print(f"Received: {line}")
                except Exception as e:
                    print(f"Serial read error: {e}")

            # Отправляем данные клиенту
            try:
                cpu_temp = CPUTemperature().temperature
            except:
                cpu_temp = None

            socket.send(jpg_as_text, flags=zmq.SNDMORE)
            socket.send_json({
                "cpu_temperature": cpu_temp,
                "cpu_usage": psutil.cpu_percent(),
                "depth": arduino_data[0],
                "gx": arduino_data[1],
                "gy": arduino_data[2],
                "in_temperature": arduino_data[3],
                "in_humidity": arduino_data[4],
                "in_pressure": arduino_data[5],
                "out_temperature": arduino_data[6]
            })

            # STEP
            # depth_speed = depth_pid.compute(get_sensors('depth'), get_sensors('depth_target'))
            # roll_speed = roll_pid.compute(get_sensors('gx'), get_sensors('gx_target'))
            # pitch_speed = pitch_pid.compute(get_sensors('gy'), get_sensors('gy_target'))

            # servos[0].write(depth_speed - roll_speed + pitch_speed)  # lf
            # servos[1].write(depth_speed + roll_speed + pitch_speed)  # rf
            # servos[2].write(depth_speed - roll_speed - pitch_speed)  # lb
            # servos[3].write(depth_speed + roll_speed - pitch_speed)  # rb

            # Получаем текущее использование памяти
            process = psutil.Process(os.getpid())
            memory_info = process.memory_info()
            print(f"Memory Usage - RSS: {memory_info.rss} bytes, VMS: {memory_info.vms} bytes")

        except KeyboardInterrupt:
            print("Shutting down...")
            break
        except Exception as e:
            print(f"Error: {e}")
            continue

    # Завершаем работу
    cap.release()
    socket.close()
    context.term()
    ser.close()
    print("Program terminated.")


if __name__ == "__main__":
    main()
