import zmq
import cv2
import pickle
import struct


def main():
    context = zmq.Context()

    # Сокет для отправки изображения и данных
    image_socket = context.socket(zmq.PUB)
    image_socket.bind("tcp://*:5555")

    # Сокет для получения команд
    command_socket = context.socket(zmq.REP)
    command_socket.bind("tcp://*:5556")

    cap = cv2.VideoCapture(0)  # Открываем камеру

    while True:
        ret, frame = cap.read()
        if not ret:
            continue

        # Кодируем изображение в jpeg
        _, buffer = cv2.imencode(".jpg", frame)

        # Создаём словарь с данными
        data = {"message": "Hello from server", "frame_size": buffer.shape[0]}

        # Сериализуем данные
        packet = pickle.dumps((buffer.tobytes(), data))

        # Отправляем данные клиенту
        image_socket.send(packet)

        # Получаем команду от клиента
        try:
            command = command_socket.recv(zmq.NOBLOCK)  # Читаем без блокировки
            commands = pickle.loads(command)
            print("Полученные команды:", commands)

            # Отправляем подтверждение
            command_socket.send(b"OK")
        except zmq.Again:
            pass  # Нет новых команд


if __name__ == "__main__":
    main()
