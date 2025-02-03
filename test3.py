import socket
import cv2
import pickle
import struct

# Настройки сервера
HOST = '192.168.0.9'
PORT = 65432

# Создание сокета
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((HOST, PORT))
server_socket.listen(5)
print(f"Сервер слушает на {HOST}:{PORT}")

# Захват видео с камеры
cap = cv2.VideoCapture(0)

# Функция для отправки данных клиенту
def send_data(client_socket, data):
    data_pickle = pickle.dumps(data)
    a = len(data_pickle)
    a1 = struct.pack(">I", a)
    client_socket.sendall(a1 + data_pickle)

# Функция для получения данных от клиента
def recv_data(client_socket):
    data = b""
    payload_size = struct.calcsize(">I")
    while len(data) < payload_size:
        packet = client_socket.recv(4 * 1024)  # 4K
        if not packet:
            return None
        data += packet
    packed_msg_size = data[:payload_size]
    data = data[payload_size:]
    msg_size = struct.unpack(">I", packed_msg_size)[0]
    while len(data) < msg_size:
        data += client_socket.recv(4 * 1024)
    frame_data = data[:msg_size]
    data = data[msg_size:]
    frame = pickle.loads(frame_data)
    return frame

while True:
    client_socket, addr = server_socket.accept()
    print(f"Подключение от {addr}")

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        # Отправка изображения клиенту
        send_data(client_socket, frame)

        # Получение управляющих сигналов от клиента
        control_signal = recv_data(client_socket)
        if control_signal is None:
            break
        print(f"Получен управляющий сигнал: {control_signal}")

    client_socket.close()

cap.release()
server_socket.close()
