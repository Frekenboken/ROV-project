import pickle
import threading
import struct
import cv2
import sys
# import serial
# import pynmea2
# import RPi.GPIO as gpio
# from gpiozero import CPUTemperature
import time
# import psutil
import zmq
import base64


def millis():
    return round(time.time() * 1000)


def GPS_init():
    try:
        serGPS = serial.Serial('/dev/ttyACM0', 19200, timeout=0.011)
        serGPS.flush()
        return serGPS
    except:
        return None


def arduino_init():
    try:
        serArduino = serial.Serial('/dev/ttyUSB0', 38400, timeout=0.02)
        serArduino.flush()
        return serArduino
    except:
        return None


def open_connection(client_address='*', server_port=5555):
    context = zmq.Context()
    socket = context.socket(zmq.PUB)
    socket.bind(f"tcp://{client_address}:{server_port}")
    return socket

def send_data(client_socket):
    while True:
        ret, frame = cap.read()

        # Пример списка данных (может быть вашим списком)
        data_list = ["some", "data", "to", "send"]

        # Кодирование изображения в base64
        _, encoded_frame = cv2.imencode('.jpg', frame)
        image_str = base64.b64encode(encoded_frame.tobytes()).decode('utf-8')

        # Отправка данных
        data = {'image': image_str, 'data_list': data_list}
        client_socket.send_pyobj(data)
        try:
            message = client_socket.recv_pyobj()
            print(f"Received message from client: {message}")
        except:
            print('Err')


        time.sleep(0.4)  # Задержка для управления частотой передачи кадров
def get_data(client_socket):
    while True:
        message = client_socket.recv_string()
        print(f"Received message from client: {message}")

        # Обработка полученного сообщения
        print(f"Server received: {message}")



def control():
    pass


if __name__ == '__main__':
    current_time = date = 'NaN'
    sensors = {name: 0 for name in
               ['gx', 'gy', 'tempOn', 'humidity', 'pressureOn', 'depth', 'satellites', 'lat', 'lon']}
    t = millis()

    # cpu = CPUTemperature()

    serGPS = GPS_init()
    serArduino = arduino_init()

    cap = cv2.VideoCapture(0)


    client_socket = open_connection()

    send_data_thread = threading.Thread(target=send_data, args=(client_socket,))
    get_data_thread = threading.Thread(target=get_data, args=(client_socket,))
    control_thread = threading.Thread(target=control)
    send_data_thread.start()
    # get_data_thread.start()
    control_thread.start()


