import cv2
import zmq
import pickle
import time
import asyncio
import threading

# Настройки для ZeroMQ
context = zmq.Context()
socket = context.socket(zmq.PUB)
socket.bind("tcp://0.0.0.0:5555")
socket.setsockopt(zmq.SNDHWM, 1)  # Буфер для отправки

camera = cv2.VideoCapture(0)
camera.set(cv2.CAP_PROP_FPS, 30)  # Настройка на 30 FPS

# Функция захвата изображения
def capture_frame():
    while True:
        ret, frame = camera.read()
        if ret:
            _, buffer = cv2.imencode(".jpg", frame, [cv2.IMWRITE_JPEG_QUALITY, 50])
            img_bytes = buffer.tobytes()
            response = {
                "info": {"temp": 22.5, "status": "active"},
                "image": img_bytes,
            }
            socket.send(pickle.dumps(response))  # Отправляем через ZeroMQ
        time.sleep(0.03)  # Ожидание 30 FPS

# Запуск многопоточности для захвата кадров
thread = threading.Thread(target=capture_frame)
thread.daemon = True
thread.start()

# Асинхронная часть для работы с ZMQ
async def main():
    while True:
        await asyncio.sleep(0.1)

try:
    asyncio.run(main())
except KeyboardInterrupt:
    print("Сервер остановлен")
finally:
    camera.release()
