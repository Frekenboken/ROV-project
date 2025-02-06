import numpy as np
from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QGridLayout, QFrame, QPushButton, QHBoxLayout
from PyQt6.QtGui import QFont, QImage, QPixmap
from PyQt6.QtCore import QThread, pyqtSignal, pyqtSlot, Qt, QSize, QTimer

import sys
from widgets.CircularBar import QCircularBar
from widgets.AngleBar import QAngleBar
import cv2
from numpy import frombuffer, uint8
import base64
import time
import zmq
import subprocess
import os

from widgets.Joystick import JoystickWidget

class TnpaControlUI(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Управление ТНПА")
        # self.showFullScreen()
        self.setStyleSheet("background-color: #010107; color: white;")

        main_layout = QHBoxLayout()

        # Фрейм для видео
        self.video_label = QLabel()
        self.video_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.video_label.setStyleSheet("border: none; border: 2px solid black;")
        self.video_label.setFixedSize(960, 720)  # Фон черный
        main_layout.addWidget(self.video_label, alignment=Qt.AlignmentFlag.AlignCenter)

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
            "Температура CPU": QLabel("0°C"),
            "Загрузка CPU": QLabel("0%"),
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
        #
        # self.btn_forward = QPushButton("▲")
        # self.btn_backward = QPushButton("▼")
        # self.btn_left = QPushButton("⇦")
        # self.btn_right = QPushButton("⇨")
        # self.btn_turn_left = QPushButton("↺")
        # self.btn_turn_right = QPushButton("↻")
        # self.btn_stop = QPushButton("■")

        self.joystick = JoystickWidget()
        control_layout.addWidget(self.joystick, alignment=Qt.AlignmentFlag.AlignCenter)

        # movement_layout.addWidget(self.btn_forward, 0, 1)
        # movement_layout.addWidget(self.btn_left, 1, 0)
        # movement_layout.addWidget(self.btn_stop, 1, 1)
        # movement_layout.addWidget(self.btn_right, 1, 2)
        # movement_layout.addWidget(self.btn_backward, 2, 1)

        servo_layout = QGridLayout()

        self.servo_buttons = {
            "Servo1+": QPushButton("▲"), "Servo1-": QPushButton("▼"),
            "Servo2+": QPushButton("▲"), "Servo2-": QPushButton("▼"),
            "Servo3+": QPushButton("▲"), "Servo3-": QPushButton("▼"),
            "Servo4+": QPushButton("▲"), "Servo4-": QPushButton("▼"),
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
        self.btn_connect = QPushButton("Подключиться")

        for btn in list(self.servo_buttons.values()):
            btn.setFont(QFont("Arial", 12, QFont.Weight.Bold))
            btn.setStyleSheet("background-color: #333; color: white; border-radius: 5px")
            btn.setFixedSize(50, 50)

        control_layout.addLayout(movement_layout)
        control_layout.addLayout(servo_layout)

        self.btn_exit.setFont(QFont("Arial", 12, QFont.Weight.Bold))
        self.btn_exit.setStyleSheet("background-color: #333; color: white; padding: 5px;")
        control_layout.addWidget(self.btn_exit, alignment=Qt.AlignmentFlag.AlignCenter)
        self.btn_connect.setFont(QFont("Arial", 12, QFont.Weight.Bold))
        self.btn_connect.setStyleSheet("background-color: #333; color: white; padding: 5px;")
        control_layout.addWidget(self.btn_connect, alignment=Qt.AlignmentFlag.AlignCenter)

        right_panel.addLayout(control_layout)

        main_layout.addLayout(right_panel)

        self.btn_exit.clicked.connect(self.close)
        self.btn_connect.clicked.connect(self.start_client)

        self.setLayout(main_layout)

        self.cam_thread = CamThread()
        self.cam_thread.change_pixmap_signal.connect(self.update_image)
        self.cam_thread.update_sensors_display.connect(self.update_sensor)

        self.control_thread = ControlThread()

        self.joystick.valueChanged.connect(lambda x, y: self.control_thread.receive_data.emit({'x': f'{x:.2f}', 'y':f'{y:.2f}'}))
        self.servo_buttons["Servo1+"].clicked.connect(lambda: self.control_thread.receive_data.emit({'s1': '145'}))
        self.servo_buttons["Servo1-"].clicked.connect(lambda: self.control_thread.receive_data.emit({'s1': '35'}))
        self.servo_buttons["Servo2+"].clicked.connect(lambda: self.control_thread.receive_data.emit({'s2': '145'}))
        self.servo_buttons["Servo2-"].clicked.connect(lambda: self.control_thread.receive_data.emit({'s2': '35'}))
        self.servo_buttons["Servo3+"].clicked.connect(lambda: self.control_thread.receive_data.emit({'s3': '145'}))
        self.servo_buttons["Servo3-"].clicked.connect(lambda: self.control_thread.receive_data.emit({'s3': '35'}))
        self.servo_buttons["Servo4+"].clicked.connect(lambda: self.control_thread.receive_data.emit({'s4': '145'}))
        self.servo_buttons["Servo4-"].clicked.connect(lambda: self.control_thread.receive_data.emit({'s4': '35'}))

        self.servo_buttons["Servo1+"].released.connect(lambda: self.control_thread.receive_data.emit({'s1': '90'}))
        self.servo_buttons["Servo1-"].released.connect(lambda: self.control_thread.receive_data.emit({'s1': '90'}))
        self.servo_buttons["Servo2+"].released.connect(lambda: self.control_thread.receive_data.emit({'s2': '90'}))
        self.servo_buttons["Servo2-"].released.connect(lambda: self.control_thread.receive_data.emit({'s2': '90'}))
        self.servo_buttons["Servo3+"].released.connect(lambda: self.control_thread.receive_data.emit({'s3': '90'}))
        self.servo_buttons["Servo3-"].released.connect(lambda: self.control_thread.receive_data.emit({'s3': '90'}))
        self.servo_buttons["Servo4+"].released.connect(lambda: self.control_thread.receive_data.emit({'s4': '90'}))
        self.servo_buttons["Servo4-"].released.connect(lambda: self.control_thread.receive_data.emit({'s4': '90'}))

    def update_image(self, image):
        self.video_label.setPixmap(QPixmap.fromImage(image))

    def update_sensor(self, sensor_name, value):
        if sensor_name in self.sensors:
            self.sensors[sensor_name].setText(value)

    def start_client(self):
        self.cam_thread.start()  # Запускаем поток
        self.control_thread.start()

    def closeEvent(self, event):
        if self.cam_thread.isRunning():
            self.cam_thread.stop()
        if self.control_thread.isRunning():
            self.control_thread.stop()
        super().closeEvent(event)



class CamThread(QThread):
    change_pixmap_signal = pyqtSignal(QImage)
    update_sensors_display = pyqtSignal(str, str)

    def __init__(self):
        super(CamThread, self).__init__()
        self.context = zmq.Context()
        self.socket = self.context.socket(zmq.PAIR)
        self.socket.connect("tcp://192.168.0.9:5555")

        self.running = True

    def run(self):
        while self.running:
            try:
                self.socket.send_string("check")
                data = self.socket.recv_pyobj()

                # Декодирование изображения из base64
                image_bytes = base64.b64decode(data['image'])
                frame = cv2.imdecode(frombuffer(image_bytes, uint8), cv2.IMREAD_COLOR)

                frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                h, w, ch = frame.shape
                bytes_per_line = ch * w
                convert_to_qt_format = QImage(frame.data, w, h, bytes_per_line, QImage.Format.Format_RGB888)
                p = convert_to_qt_format.scaled(1280, 720, Qt.AspectRatioMode.KeepAspectRatio)
                self.change_pixmap_signal.emit(p)

                data_dict = data['data']
                # print("Received Data Dict:", data_dict)

                if all(data_dict.values()):
                    self.update_sensors_display.emit("Глубина", data_dict['depth'])
                    self.update_sensors_display.emit("Ось X", data_dict['dx'])
                    self.update_sensors_display.emit("Ось Y", data_dict['dy'])
                    self.update_sensors_display.emit("Температура на борту", data_dict['temperature_in'])
                    self.update_sensors_display.emit("Температура за бортом", data_dict['temperature_out'])
                    self.update_sensors_display.emit("Влажность", data_dict['humidity_in'])
                    self.update_sensors_display.emit("Давление на борту", data_dict['pressure_in'])
                    self.update_sensors_display.emit("Температура CPU", data_dict['cpu_temperature'])
                    self.update_sensors_display.emit("Загрузка CPU", data_dict['cpu_usage'])

            except Exception as e:
                print(e)

        self.socket.close()
        self.context.term()

    def stop(self):
        self.running = False
        self.wait()


class ControlThread(QThread):
    receive_data = pyqtSignal(dict)

    def __init__(self):
        super(ControlThread, self).__init__()
        self.context = zmq.Context()
        self.socket = self.context.socket(zmq.PAIR)
        self.socket.connect("tcp://192.168.0.9:5556")

        self.control_data = {'x': '0', 'y': '0', 'target_depth': '100', 's1': '90', 's2': '90', 's3': '90', 's4': '90'}

        self.running = True

        self.receive_data.connect(self.handle_data)

    def run(self):
        while self.running:
            try:
                self.socket.send_pyobj(self.control_data)
                data = self.socket.recv_pyobj()

            except Exception as e:
                print(e)

        self.socket.close()
        self.context.term()

    @pyqtSlot(dict)
    def handle_data(self, data: dict):
        for key, value in data.items():
            self.control_data[key] = value
        print(self.control_data)

    def stop(self):
        self.running = False
        self.wait()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = TnpaControlUI()
    window.show()
    sys.exit(app.exec())
