import cv2
import zmq
import json
import time

# Настройка ZeroMQ
context = zmq.Context()
socket = context.socket(zmq.REP)  # Ответный сокет
socket.bind("tcp://0.0.0.0:5555")  # Сервер слушает на порту 5555

camera = cv2.VideoCapture(0)  # Открываем камеру
camera.set(cv2.CAP_PROP_FPS, 30)  # Попытка выставить 30 FPS
print("Сервер запущен на порту 5555")

while True:
    try:
        message = socket.recv_json()  # Ждём запрос от клиента
        command = message.get("command", "noop")

        ret, frame = camera.read()  # Захватываем кадр
        if not ret:
            continue  # Если не удалось получить кадр — пропускаем

        _, buffer = cv2.imencode(".jpg", frame, [cv2.IMWRITE_JPEG_QUALITY, 50])
        img_bytes = buffer.tobytes()  # Кодируем в JPEG

        # Ответ клиенту
        response = {
            "status": "ok",
            "command_received": command,
            "info": {"temp": 22.5, "status": "active"},
            "image": img_bytes.hex(),  # Преобразуем в HEX
        }
        socket.send_json(response)  # Отправляем ответ
    except Exception as e:
        print(f"Ошибка: {e}")
        time.sleep(1)  # Мини-пауза при ошибке
