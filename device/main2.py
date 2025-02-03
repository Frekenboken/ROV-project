import os

from piservo import Servo
from gpiozero import CPUTemperature
import threading
import cv2
import sys
import pynmea2
import RPi.GPIO as gpio
import time
import psutil
import zmq
import cv2
import base64
import serial
import numpy as np

from PID import PIDController


def main():
    print("Initialization... (5 sec)")

    context = zmq.Context()
    socket = context.socket(zmq.REP)
    socket.bind("tcp://*:5555")

    cap = cv2.VideoCapture(0)

    ser = serial.Serial('/dev/ttyUSB0', 38400, timeout=1)

    depth_pid = PIDController(0.01, 0.0001, 0.1)
    depth_pid.set_limit(10, 170)
    depth_pid.set_offset(90)

    roll_pid = PIDController(0.01, 0.0001, 0.1)
    roll_pid.set_limit(-5, 5)
    roll_pid.set_offset(0)

    pitch_pid = PIDController(0.01, 0.0001, 0.1)
    pitch_pid.set_limit(-5, 5)
    pitch_pid.set_offset(0)

    servos = [Servo(18), Servo(18),
              Servo(18), Servo(18)]
    motors = [Servo(19), Servo(19),
              Servo(19), Servo(19)]

    data = []

    for i in range(10):
        if ser.in_waiting > 0:
            break
        time.sleep(0.5)
    else:
        raise Exception

    print("Ready!")

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        # Преобразуем изображение в формат, подходящий для передачи
        _, buffer = cv2.imencode('.jpg', frame)
        jpg_as_text = buffer.tobytes()

        # Принимаем управляющий сигнал от клиента
        message = socket.recv_json()
        print(f"Received control signal: {message}")

        if ser.in_waiting > 0:
            line = ser.readline().decode('utf-8').rstrip()
            arduino_data = line.split(",")
            print(f"Received: {line}")

        # Отправляем изображение клиенту
        socket.send(jpg_as_text, flags=zmq.SNDMORE)
        socket.send_json({"cpu_temperature": psutil.sensors_temperatures()["cpu_thermal"][0][1],
                          "cpu_usage": int(psutil.cpu_percent()),
                          "depth": arduino_data[0],
                          "gx": arduino_data[0],
                          "gy": arduino_data[0],
                          "in_temperature": arduino_data[0],
                          "in_humidity": arduino_data[0],
                          "in_pressure": arduino_data[0],
                          "out_temperature": arduino_data[0]})

        # STEP
        # depth_speed = depth_pid.compute(get_sensors('depth'), get_sensors('depth_target'))
        # roll_speed = roll_pid.compute(get_sensors('gx'), get_sensors('gx_target'))
        # pitch_speed = pitch_pid.compute(get_sensors('gy'), get_sensors('gy_target'))

        # servos[0].write(depth_speed - roll_speed + pitch_speed)  # lf
        # servos[1].write(depth_speed + roll_speed + pitch_speed)  # rf
        # servos[2].write(depth_speed - roll_speed - pitch_speed)  # lb
        # servos[3].write(depth_speed + roll_speed - pitch_speed)  # rb

        # Получаем текущий процесс
        process = psutil.Process(os.getpid())

        # Получаем использование памяти в байтах
        memory_info = process.memory_info()
        print(f"RSS: {memory_info.rss} bytes")
        print(f"VMS: {memory_info.vms} bytes")

    cap.release()
    socket.close()
    context.term()


if __name__ == "__main__":
    main()
