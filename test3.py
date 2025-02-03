import socket
import cv2
import pickle
import struct


def server(host='192.168.0.9', port=5000):
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)  # Позволяет повторно использовать порт
    server_socket.bind((host, port))
    server_socket.listen(5)
    print(f"Сервер запущен на {host}:{port}, ожидаем подключение...")

    cap = cv2.VideoCapture(0)
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

    while True:
        conn, addr = server_socket.accept()
        print(f"Клиент подключился: {addr}")

        try:
            while True:
                ret, frame = cap.read()
                if not ret:
                    break

                # Сжатие изображения (JPEG, качество 50)
                _, buffer = cv2.imencode('.jpg', frame, [cv2.IMWRITE_JPEG_QUALITY, 50])
                data_list = ["command1", "command2", 42]  # Пример передаваемых данных

                # Сериализация данных (сжатое изображение + список)
                data = pickle.dumps((buffer, data_list))
                message_size = struct.pack("Q", len(data))

                # Отправка данных клиенту
                conn.sendall(message_size + data)

                # Получение управляющих сигналов
                control_data_size = struct.unpack("Q", conn.recv(8))[0]
                control_data = conn.recv(control_data_size)
                control_signals = pickle.loads(control_data)
                print(f"Получены управляющие сигналы: {control_signals}")
        except Exception as e:
            print(f"Соединение разорвано: {e}")
        finally:
            conn.close()
            print("Ожидание нового подключения...")

    cap.release()
    server_socket.close()
    print("Сервер завершил работу.")


if __name__ == "__main__":
    server()
