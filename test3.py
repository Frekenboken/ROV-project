import cv2
import pickle
import zmq


def server(host='192.168.0.9', port=5000):
    context = zmq.Context()
    socket = context.socket(zmq.REP)  # REP-сокет должен сначала получать запрос
    socket.bind(f"tcp://{host}:{port}")
    print(f"Сервер запущен на {host}:{port}, ожидаем подключение...")

    cap = cv2.VideoCapture(0)
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

    while True:
        # Сначала ждем запрос от клиента (иначе будет ошибка)
        request = socket.recv()

        ret, frame = cap.read()
        if not ret:
            break

        data_list = ["command1", "command2", 42]  # Пример списка данных

        # Сериализация данных (изображение + список)
        data = pickle.dumps((frame, data_list))

        # Отправка данных клиенту
        socket.send(data)

    cap.release()
    socket.close()
    context.term()
    print("Сервер завершил работу.")


if __name__ == "__main__":
    server()
