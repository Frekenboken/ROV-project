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
import numpy as np

from PID import PIDController

def main():
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

        # Отправляем изображение клиенту
        socket.send(jpg_as_text, flags=zmq.SNDMORE)
        socket.send_json({"cpu_temperature": psutil.sensors_temperatures(),
                          "cpu_usage": int(psutil.cpu_percent())})

        if ser.in_waiting > 0:
            line = ser.readline().decode('utf-8').rstrip()
            print(f"Received: {line}")

        # STEP
        # depth_speed = depth_pid.compute(get_sensors('depth'), get_sensors('depth_target'))
        # roll_speed = roll_pid.compute(get_sensors('gx'), get_sensors('gx_target'))
        # pitch_speed = pitch_pid.compute(get_sensors('gy'), get_sensors('gy_target'))

        # servos[0].write(depth_speed - roll_speed + pitch_speed)  # lf
        # servos[1].write(depth_speed + roll_speed + pitch_speed)  # rf
        # servos[2].write(depth_speed - roll_speed - pitch_speed)  # lb
        # servos[3].write(depth_speed + roll_speed - pitch_speed)  # rb

    cap.release()
    socket.close()
    context.term()

if __name__ == "__main__":
    main()
