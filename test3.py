import cv2
import zmq
import numpy as np

def main():
    context = zmq.Context()
    video_socket = context.socket(zmq.PUB)
    video_socket.bind("tcp://*:5555")  # Порт для передачи видео

    control_socket = context.socket(zmq.REP)
    control_socket.bind("tcp://*:5556")  # Порт для получения управляющих сигналов

    cap = cv2.VideoCapture(0)  # Захват видео с камеры

    print("Сервер запущен и ожидает запросы...")

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        # Отправляем изображение
        frame = cv2.resize(frame, (640, 480))  # Изменяем размер изображения для уменьшения объема данных
        image = cv2.imencode('.jpg', frame)[1].tobytes()
        video_socket.send(image)

        # Проверяем наличие управляющих сигналов
        if control_socket.poll(1000) >= 0:  # Таймаут 1 секунда
            control_message = control_socket.recv_pyobj()
            print(f"Получен управляющий сигнал: {control_message}")

            # Отправляем ответ клиенту (например, подтверждение получения сигнала)
            response = {"status": "received"}
            control_socket.send_pyobj(response)

    cap.release()
    video_socket.close()
    control_socket.close()
    context.term()

if __name__ == "__main__":
    main()
