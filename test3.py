import zmq
import cv2
import numpy as np
import ujson as json  # Быстрая версия JSON
import time


def main():
    context = zmq.Context()

    # PUSH-сокет для отправки данных
    video_socket = context.socket(zmq.PUSH)
    video_socket.bind("tcp://*:5555")

    # REP-сокет для приема команд
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

        # Конвертируем кадр в bytes (BGR -> raw)
        frame_bytes = frame.tobytes()

        # Создаем JSON-объект
        data = {
            "timestamp": time.time(),
            "message": "Данные с сервера",
            "shape": frame.shape  # Нужно для восстановления изображения
        }
        json_data = json.dumps(data).encode('utf-8')

        # Отправляем кадр и JSON
        video_socket.send_multipart([frame_bytes, json_data], zmq.NOBLOCK)

        # Проверяем входящие команды
        try:
            if command_socket.poll(10):  # Ждем входящий запрос (10 мс)
                command = command_socket.recv_json()
                print(f"Получена команда: {command}")
                command_socket.send_json({"status": "ok"})
        except zmq.ZMQError:
            pass  # Игнорируем ошибки


if __name__ == "__main__":
    main()
