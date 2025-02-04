import zmq
import cv2
import pickle
import time

def server():
    context = zmq.Context()

    # Сокет для отправки изображений и данных
    sender = context.socket(zmq.PUB)
    sender.bind("tcp://*:5555")

    # Сокет для получения команд
    receiver = context.socket(zmq.SUB)
    receiver.bind("tcp://*:5556")
    receiver.setsockopt_string(zmq.SUBSCRIBE, '')

    # Инициализация камеры
    cap = cv2.VideoCapture(0)

    while True:
        # Чтение изображения с камеры
        ret, frame = cap.read()
        if not ret:
            break

        # Сериализация изображения
        serialized_frame = pickle.dumps(frame)

        # Пример данных
        data = {"temperature": 25.5, "humidity": 60}
        serialized_data = pickle.dumps(data)

        # Отправка изображения и данных
        sender.send_multipart([b'image', serialized_frame, serialized_data])

        # Получение команд
        try:
            command = receiver.recv_string(flags=zmq.NOBLOCK)
            print(f"Received command: {command}")
        except zmq.Again:
            pass

        # Задержка для симуляции реального времени
        time.sleep(0.1)

    cap.release()

if __name__ == "__main__":
    server()
