from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QGridLayout, QFrame, QPushButton, QHBoxLayout
from PyQt6.QtGui import QFont
from PyQt6.QtCore import Qt
import sys

import zmq


class TnpaControlUI(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Управление ТНПА")
        self.showFullScreen()
        self.setStyleSheet("background-color: #1E1E1E; color: white;")

        main_layout = QHBoxLayout()

        # Фрейм для видео
        self.video_frame = QFrame()
        self.video_frame.setStyleSheet("border: 2px solid white;")
        self.video_frame.setFixedSize(1280, 720)  # Формат 16:9
        main_layout.addWidget(self.video_frame, alignment=Qt.AlignmentFlag.AlignCenter)

        right_panel = QVBoxLayout()

        # Грид для датчиков
        sensor_layout = QGridLayout()

        self.sensors = {
            "Глубина": QLabel("0 м"),
            "Ось X": QLabel("0°"),
            "Ось Y": QLabel("0°"),
            "Температура на борту": QLabel("0°C"),
            "Температура за бортом": QLabel("0°C"),
            "Влажность": QLabel("0%"),
            "Давление на борту": QLabel("0 Па"),
        }

        row, col = 0, 0
        for name, label in self.sensors.items():
            title = QLabel(name)
            title.setFont(QFont("Arial", 10, QFont.Weight.Bold))
            label.setFont(QFont("Arial", 12))
            label.setAlignment(Qt.AlignmentFlag.AlignCenter)

            sensor_layout.addWidget(title, row, col)
            sensor_layout.addWidget(label, row + 1, col)

            col += 1
            if col > 1:
                col = 0
                row += 2

        right_panel.addLayout(sensor_layout)

        # Элементы управления ТНПА
        control_layout = QVBoxLayout()

        movement_layout = QGridLayout()

        self.btn_forward = QPushButton("▲")
        self.btn_backward = QPushButton("▼")
        self.btn_left = QPushButton("⇦")
        self.btn_right = QPushButton("⇨")
        self.btn_turn_left = QPushButton("↺")
        self.btn_turn_right = QPushButton("↻")
        self.btn_stop = QPushButton("■")

        movement_layout.addWidget(self.btn_forward, 0, 1)
        movement_layout.addWidget(self.btn_left, 1, 0)
        movement_layout.addWidget(self.btn_stop, 1, 1)
        movement_layout.addWidget(self.btn_right, 1, 2)
        movement_layout.addWidget(self.btn_backward, 2, 1)

        servo_layout = QGridLayout()

        self.servo_buttons = {
            "Servo1+": QPushButton("↗"), "Servo1-": QPushButton("↙"),
            "Servo2+": QPushButton("↖"), "Servo2-": QPushButton("↘"),
            "Servo3+": QPushButton("↖"), "Servo3-": QPushButton("↘"),
            "Servo4+": QPushButton("↗"), "Servo4-": QPushButton("↙"),
        }

        servo_layout.addWidget(self.servo_buttons["Servo1+"], 0, 0)
        servo_layout.addWidget(self.servo_buttons["Servo1-"], 1, 0)
        servo_layout.addWidget(self.servo_buttons["Servo2+"], 0, 1)
        servo_layout.addWidget(self.servo_buttons["Servo2-"], 1, 1)
        servo_layout.addWidget(self.servo_buttons["Servo3+"], 2, 0)
        servo_layout.addWidget(self.servo_buttons["Servo3-"], 3, 0)
        servo_layout.addWidget(self.servo_buttons["Servo4+"], 2, 1)
        servo_layout.addWidget(self.servo_buttons["Servo4-"], 3, 1)

        self.btn_exit = QPushButton("Выход")

        for btn in [self.btn_forward, self.btn_backward, self.btn_left, self.btn_right, self.btn_turn_left,
                    self.btn_turn_right, self.btn_stop] + list(self.servo_buttons.values()):
            btn.setFont(QFont("Arial", 12, QFont.Weight.Bold))
            btn.setStyleSheet("background-color: #333; color: white;")
            btn.setFixedSize(50, 50)

        control_layout.addLayout(movement_layout)
        control_layout.addLayout(servo_layout)

        self.btn_exit.setFont(QFont("Arial", 12, QFont.Weight.Bold))
        self.btn_exit.setStyleSheet("background-color: #333; color: white; padding: 5px;")
        control_layout.addWidget(self.btn_exit, alignment=Qt.AlignmentFlag.AlignCenter)

        right_panel.addLayout(control_layout)

        main_layout.addLayout(right_panel)

        self.btn_exit.clicked.connect(self.close)

        self.setLayout(main_layout)

    def update_sensor(self, sensor_name, value):
        if sensor_name in self.sensors:
            self.sensors[sensor_name].setText(value)


class ReceiveThread(QThread):
    change_pixmap_signal = Signal(QImage)
    update_data_signal = Signal(dict)

    def __init__(self, address):
        super(ReceiveThread, self).__init__()
        self.socket = self.context = None
        self.address = address
        self.response = 'ok'
        self.req = False
        self.connection = False
        self.cl = False

    def connect_device(self):
        self.req = True

    def disconnect_device(self):
        self.connection = False

    def run(self):
        try:
            context = zmq.Context()
            socket = context.socket(zmq.REQ)
            socket.connect("tcp://localhost:5555")  # Подключаемся к серверу на порту 5555
            while True:
                # Пример списка данных для отправки
                data_list = [1, 2, 3, 4, 5]

                # Отправляем запрос серверу
                socket.send_pyobj(data_list)
                print(f"Отправлен запрос: {data_list}")

                # Получаем ответ от сервера
                response = socket.recv_pyobj()
                print(f"Получен ответ: {response}")

                # print('go')
                # # time.sleep(0.4)
                # print('кидаю респонс')
                # self.socket.send_string(self.response)
                # print('скинул респонс')
                # print('получаю дату')
                # data = self.socket.recv_pyobj()
                # print('Получил дату')
                #
                # # Декодирование изображения из base64
                # image_bytes = base64.b64decode(data['image'])
                # frame = cv2.imdecode(frombuffer(image_bytes, uint8), cv2.IMREAD_COLOR)
                #
                # # Используйте данные из списка, например:
                # data_dict = data['data_dict']
                # print("Received Data List:", data_dict)
                #
                # # Отображение изображения
                # # time.sleep(0.1)
                #
                # rgb_image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                # h, w, ch = rgb_image.shape
                # bytes_per_line = ch * w
                # convert_to_qt_format = QImage(rgb_image.data, w, h, bytes_per_line, QImage.Format_RGB888)
                # p = convert_to_qt_format.scaled(960, 540, Qt.KeepAspectRatio)
                # self.change_pixmap_signal.emit(p)
                # self.update_data_signal.emit(data_dict)
        except zmq.ZMQError as e:
            print(f"Ошибка ZeroMQ: {e}")

    def set_response(self, response):
        self.response = response

    def zmq_connect_to(self, address):
        context = zmq.Context()
        socket = context.socket(zmq.PAIR)
        socket.connect(address)
        return socket, context

    def close(self):
        # self.set_response('c')
        # time.sleep(0.3)
        self.cl = True
        self.socket.setsockopt(zmq.LINGER, 0)
        self.socket.close()
        self.context.term()
        self.wait()  # Ждем завершения потока
        self.quit()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = TnpaControlUI()
    window.show()
    sys.exit(app.exec())
