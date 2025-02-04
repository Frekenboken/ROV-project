import cv2
import zmq
import json
import time

context = zmq.Context()
socket = context.socket(zmq.PUB)  # Паблишер (широковещательная передача)
socket.bind("tcp://0.0.0.0:5555")
socket.setsockopt(zmq.SNDHWM, 1)  # Ограничиваем буфер до 1 сообщения

camera = cv2.VideoCapture(0)
camera.set(cv2.CAP_PROP_FPS, 30)
print("Сервер запущен на порту 5555")

while True:
    ret, frame = camera.read()
    if not ret:
        continue

    _, buffer = cv2.imencode(".jpg", frame, [cv2.IMWRITE_JPEG_QUALITY, 50])
    img_bytes = buffer.tobytes()

    # Данные для отправки
    response = {
        "info": {"temp": 22.5, "status": "active"},
        "image": img_bytes,  # Передаём в чистом `bytes`, без HEX!
    }

    socket.send_json(response)  # Отправляем последним клиентам
    time.sleep(0.03)  # Ограничиваем до 30 FPS
