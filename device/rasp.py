import zmq
import cv2
import base64
import struct
import time

context = zmq.Context()
socket = context.socket(zmq.PAIR)
socket.bind("tcp://*:5555")

cap = cv2.VideoCapture(0)  # 0 означает использование встроенной вебкамеры
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)

while True:
    ret, frame = cap.read()

    # Пример списка данных (может быть вашим списком)
    data_list = ("some", "data", "to", "send")

    # Кодирование изображения в base64
    _, encoded_frame = cv2.imencode('.jpg', frame)
    image_str = base64.b64encode(encoded_frame.tobytes()).decode('utf-8')

    # Отправка данных
    data = {'image': image_str, 'data_list': data_list}
    print('Wait')
    response = socket.recv_string()
    if response == 'c':
        print('Close connection.')
        break
    socket.send_pyobj(data)
    # time.sleep(0.1)  # Задержка для управления частотой передачи кадров
