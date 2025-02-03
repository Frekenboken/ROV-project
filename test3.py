import socket
import cv2
import pickle
import struct

def server(host='192.168.0.9', port=5000):
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(5)
    print(f"Сервер запущен на {host}:{port}, ожидаем подключение...")

    conn, addr = server_socket.accept()
    print(f"Клиент подключился: {addr}")

    cap = cv2.VideoCapture(0)
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        data_list = ["command1", "command2", 42]

        data = pickle.dumps((frame, data_list))
        message_size = struct.pack("Q", len(data))

        try:
            conn.sendall(message_size + data)

            control_data_size = struct.unpack("Q", conn.recv(8))[0]
            control_data = conn.recv(control_data_size)
            control_signals = pickle.loads(control_data)
            print(f"Получены управляющие сигналы: {control_signals}")
        except:
            break

    cap.release()
    conn.close()
    server_socket.close()
    print("Сервер завершил работу.")

if __name__ == "__main__":
    server()
