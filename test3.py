import socket
import cv2
import struct
import threading
import numpy as np

class Server:
    def __init__(self, host='192.168.0.9', port=5000):
        self.host = host
        self.port = port
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.bind((self.host, self.port))
        self.server_socket.listen(5)
        self.clients = []
        self.lock = threading.Lock()

    def handle_client(self, client_socket):
        try:
            cap = cv2.VideoCapture(0)  # Используйте 0 для веб-камеры или путь к видеофайлу
            while True:
                ret, frame = cap.read()
                if not ret:
                    break

                # Кодируем кадр в JPEG
                _, buffer = cv2.imencode('.jpg', frame, [cv2.IMWRITE_JPEG_QUALITY, 80])
                data = buffer.tobytes()

                # Отправляем размер данных и сами данные
                message_size = struct.pack("L", len(data))
                with self.lock:
                    client_socket.sendall(message_size + data)

                # Принимаем управляющие сигналы от клиента
                control_data = client_socket.recv(1024)
                if control_data:
                    print(f"Received control data: {control_data.decode()}")

        except ConnectionResetError:
            print("Client disconnected")
        finally:
            cap.release()
            client_socket.close()

    def start(self):
        print(f"Server started on {self.host}:{self.port}")
        while True:
            client_socket, addr = self.server_socket.accept()
            print(f"Connected by {addr}")
            self.clients.append(client_socket)
            threading.Thread(target=self.handle_client, args=(client_socket,)).start()

if __name__ == "__main__":
    server = Server()
    server.start()