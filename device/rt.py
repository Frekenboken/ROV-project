import socket
import cv2
import pickle
import struct
import threading

# Функция для отправки изображения
def send_image(client_socket, image):
    _, img_encoded = cv2.imencode('.jpg', image)
    data = pickle.dumps(img_encoded, protocol=3)
    size = struct.pack("L", len(data))
    client_socket.sendall(size + data)

# Функция для обработки клиентского соединения
def handle_client(client_socket):
    while True:
        # Отправляем какие-то данные
        data_to_send = [1, 2, 3, 4, 5]
        serialized_data = pickle.dumps(data_to_send)
        client_socket.sendall(struct.pack("L", len(serialized_data)) + serialized_data)

        # Считываем изображение с вебкамеры
        cap = cv2.VideoCapture(0)
        ret, frame = cap.read()
        cap.release()

        # Отправляем изображение
        send_image(client_socket, frame)

# Основная функция сервера
def main():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('', 8888))
    server_socket.listen(5)

    print("Сервер слушает на порту 8888...")

    while True:
        client_socket, addr = server_socket.accept()
        print(f"Подключение от {addr}")

        client_handler = threading.Thread(target=handle_client, args=(client_socket,))
        client_handler.start()

if __name__ == "__main__":
    main()
