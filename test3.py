import socket
import cv2
import pickle
import struct
import threading

def send_frame(client_socket):
    cap = cv2.VideoCapture(0)
    while True:
        ret, frame = cap.read()
        if not ret:
            break
        encode_param = [int(cv2.IMWRITE_JPEG_QUALITY), 90]
        result, frame = cv2.imencode('.jpg', frame, encode_param)
        data = pickle.dumps(frame, 0)
        size = len(data)

        try:
            client_socket.sendall(struct.pack(">L", size) + data)
        except:
            break

def receive_data(client_socket):
    while True:
        try:
            data = client_socket.recv(1024)
            if not data:
                break
            print(f"Received data: {data.decode('utf-8')}")
        except:
            break

def handle_client(client_socket):
    send_thread = threading.Thread(target=send_frame, args=(client_socket,))
    receive_thread = threading.Thread(target=receive_data, args=(client_socket,))
    send_thread.start()
    receive_thread.start()
    send_thread.join()
    receive_thread.join()
    client_socket.close()

def main():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('0.0.0.0', 8485))
    server_socket.listen(5)
    print("Server listening on port 8485")

    while True:
        client_socket, addr = server_socket.accept()
        print(f"Connection from {addr}")
        client_handler = threading.Thread(target=handle_client, args=(client_socket,))
        client_handler.start()

if __name__ == "__main__":
    main()
