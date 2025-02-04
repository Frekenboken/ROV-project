import threading
import cv2
import sys
import pynmea2
import time
import psutil
import zmq
import cv2
import base64

cap = cv2.VideoCapture(0)
# cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
# cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)

context = zmq.Context()
socket = context.socket(zmq.PAIR)
socket.bind("tcp://*:5555")

context2 = zmq.Context()
socket2 = context.socket(zmq.PAIR)
socket2.bind("tcp://*:5556")


def th1():
    while True:
        suc, frame = cap.read()
        if not suc:
            print(1)
            break

        # Кодирование изображения в base64
        _, encoded_frame = cv2.imencode('.jpg', frame)
        image_str = base64.b64encode(encoded_frame.tobytes()).decode('utf-8')

        # Отправка данных
        data = {'image': image_str, 'data_dict': [1, 2, 3]}
        response = socket.recv_string()
        if response == 'c':
            print('Close connection.')
        socket.send_pyobj(data)
        # time.sleep(0.05)  # Задержка для управления частотой передачи кадров


def th2():
    while True:
        # Отправка данных
        response = socket2.recv_string()
        print(response)
        data = {'status': 'ok'}
        socket2.send_pyobj(data)


t1 = threading.Thread(target=th1)
t2 = threading.Thread(target=th2)
t1.start()
t2.start()
