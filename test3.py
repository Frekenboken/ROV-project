import socket
import cv2
import pickle
import struct
import threading

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
            cap = cv2.VideoCapture(0)
            while True:
                ret, frame = cap.read()
                if not ret:
                    break

                # Serialize frame
                data = pickle.dumps(frame)
                message_size = struct.pack("L", len(data))

                # Send frame to client
                with self.lock:
                    client_socket.sendall(message_size + data)

                # Receive control signals from client
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