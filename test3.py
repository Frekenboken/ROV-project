import socket
import threading
import cv2
import pickle
import struct
import zlib

SERVER_IP = '192.168.0.9'
SERVER_PORT = 12345

def compress_image(image):
    encode_param = [int(cv2.IMWRITE_JPEG_QUALITY), 30]  # Уменьшаем качество для ускорения
    result, encimg = cv2.imencode('.jpg', image, encode_param)
    compressed_image = zlib.compress(encimg)
    return compressed_image

def handle_client(client_socket):
    cap = cv2.VideoCapture(0)
    while True:
        ret, frame = cap.read()
        if not ret:
            break

        compressed_frame = compress_image(frame)
        data = pickle.dumps({'image': compressed_frame, 'data': {'example_key': 'example_value'}})
        a = len(data)
        client_socket.sendall(struct.pack(">L", a) + data)

        # Receive control signal from client
        control_signal = client_socket.recv(1024).decode('utf-8')
        print(f"Received control signal: {control_signal}")

    cap.release()
    client_socket.close()

def start_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((SERVER_IP, SERVER_PORT))
    server_socket.listen(5)
    print(f"Server listening on {SERVER_IP}:{SERVER_PORT}")

    while True:
        client_socket, addr = server_socket.accept()
        print(f"Accepted connection from {addr}")
        client_thread = threading.Thread(target=handle_client, args=(client_socket,))
        client_thread.start()

if __name__ == "__main__":
    start_server()
