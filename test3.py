import zmq
import cv2
import numpy as np
import json
import time


def main():
    context = zmq.Context()

    # PUB-сокет для отправки видео + данных
    video_socket = context.socket(zmq.PUB)
    video_socket.bind("tcp://*:5555")

    # REP-сокет для приема команд от клиента
    command_socket = context.socket(zmq.REP)
    command_socket.bind("tcp://*:5556")

    cap = cv2.VideoCapture(0)

    if not cap.isOpened():
        print("Ошибка: не удалось открыть камеру")
        return

    print("Сервер запущен...")

    while True:
        ret, frame = cap.read()
        if not ret:
            print("Ошибка: не удалось получить кадр")
            break

        # Кодируем изображение в jpg и сериализуем
        _, buffer = cv2.imencode('.jpg', frame, [int(cv2.IMWRITE_JPEG_QUALITY), 80])
        frame_bytes = buffer.tobytes()

        # Отправляем видео и список данных
        data = {
            "timestamp": time.time(),
            "message": "Данные с сервера"
        }
        json_data = json.dumps(data).encode('utf-8')

        video_socket.send_multipart([frame_bytes, json_data])

        # Проверяем команды от клиента (не блокируем)
        try:
            if command_socket.poll(10):  # Проверяем входящие данные
                command = command_socket.recv_json()
                print(f"Получена команда от клиента: {command}")
                command_socket.send_json({"status": "ok"})
        except zmq.error.ZMQError:
            pass  # Игнорируем ошибки


if __name__ == "__main__":
    main()
