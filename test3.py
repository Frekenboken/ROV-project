import zmq
import cv2
import numpy as np

def main():
    context = zmq.Context()
    socket = context.socket(zmq.REP)
    socket.bind("tcp://*:5555")

    cap = cv2.VideoCapture(0)

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        # Преобразуем изображение в формат, подходящий для передачи
        _, buffer = cv2.imencode('.jpg', frame)
        jpg_as_text = buffer.tobytes()

        # Принимаем управляющий сигнал от клиента
        message = socket.recv_json()
        print(f"Received control signal: {message}")

        # Отправляем изображение клиенту
        socket.send(jpg_as_text, flags=zmq.SNDMORE)
        socket.send_json({"status": "ok"})

    cap.release()
    socket.close()
    context.term()

if __name__ == "__main__":
    main()
