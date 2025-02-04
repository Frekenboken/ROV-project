import cv2
import zmq
import pickle
import time

context = zmq.Context()
socket = context.socket(zmq.PUB)
socket.bind("tcp://0.0.0.0:5555")
socket.setsockopt(zmq.SNDHWM, 1)

camera = cv2.VideoCapture(0)
camera.set(cv2.CAP_PROP_FPS, 30)
print("Сервер запущен на порту 5555")

while True:
    ret, frame = camera.read()
    if not ret:
        continue

    _, buffer = cv2.imencode(".jpg", frame, [cv2.IMWRITE_JPEG_QUALITY, 50])
    img_bytes = buffer.tobytes()

    # Упаковываем данные с использованием pickle
    response = {
        "info": {"temp": 22.5, "status": "active"},
        "image": img_bytes,
    }

    socket.send(pickle.dumps(response))  # Отправляем в бинарном формате
    time.sleep(0.03)
