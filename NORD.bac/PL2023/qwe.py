import socket
from PySide6.QtCore import QThread, Signal, QSize
from PySide6.QtGui import QImage, QPixmap, QColor, Qt, QIntList
from PySide6.QtWidgets import QApplication, QMainWindow, QSizePolicy
from UI import Ui_MainWindow
import sys
from Widgetss.CircularBar import QCircularBar
from Widgetss.AngleBar import QAngleBar
import cv2
from numpy import frombuffer, uint8
import base64
import time
import zmq


class Gui(QMainWindow):
    def __init__(self):
        super(Gui, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        # self.ui.name.setText('TEST!')

        self.cpu_usage_bar = QCircularBar()
        self.cpu_temp_bar = QCircularBar()
        self.roll_indicator = QAngleBar()
        self.diff_indicator = QAngleBar()

        self.cpu_temp_bar.setFixedSize(QSize(150, 150))
        self.cpu_usage_bar.setFixedSize(QSize(150, 150))
        self.cpu_temp_bar.setDataColors([
            (0.0, QColor(0, 120, 255)),  # Красный цвет
            (1.0, QColor(215, 38, 56))  # Синий цвет
        ])
        self.cpu_usage_bar.setDataColors([
            (0.0, QColor(0, 120, 255)),  # Красный цвет
            (1.0, QColor(215, 38, 56))  # Синий цвет
        ])
        self.roll_indicator.setOffset(90)
        self.diff_indicator.setOffset(90)

        self.roll_indicator.setLetters('L', 'R')
        self.diff_indicator.setLetters('B', 'F')

        self.roll_indicator.setFixedSize(QSize(210, 200))
        self.diff_indicator.setFixedSize(QSize(210, 200))

        self.ui.cpuusageframe.layout().addWidget(self.cpu_usage_bar)
        self.ui.cputempframe.layout().addWidget(self.cpu_temp_bar)
        self.ui.rollframe.layout().addWidget(self.roll_indicator)
        self.ui.diffframe.layout().addWidget(self.diff_indicator)

        # Создаем и запускаем поток для видео
        self.receive_thread = ReceiveThread()
        self.receive_thread.change_pixmap_signal.connect(self.update_image)
        self.receive_thread.update_data_signal.connect(self.update_data)
        self.receive_thread.start()

    def update_image(self, image):
        self.ui.label.setPixmap(QPixmap.fromImage(image))

    def update_data(self, data):
        self.roll_indicator.setAngle(data['gx'])
        self.diff_indicator.setAngle(data['gy'])
        self.cpu_temp_bar.setValue(data['cpu_temp'])
        self.cpu_usage_bar.setValue(data['cpu_usage'])

        self.ui.lat.setText(str(data['lat']))
        self.ui.lon.setText(str(data['lon']))
        self.ui.speed.setText(str(data['speed']))
        self.ui.sats.setText(str(data['satellites']))

        self.ui.depth.setText(str(data['depth']))
        self.ui.depth_target.setText(str(data['depth_target']))

        self.ui.time.setText(str(data['time']))

        self.ui.humidity_on.setText(str(data['humidity_on']))
        self.ui.pressure_on.setText(str(data['pressure_on']))
        self.ui.temp_on.setText(str(data['temp_on']))

        self.ui.temp_out.setText(str(data['temp_out']))

    def closeEvent(self, event):
        print('close')
        self.receive_thread.close_connection()
        super().closeEvent(event)


class ReceiveThread(QThread):
    change_pixmap_signal = Signal(QImage)
    update_data_signal = Signal(dict)

    def __init__(self):
        super(ReceiveThread, self).__init__()
        self.socket, self.context = self.open_connection()
        self.response = 'ok'

    def run(self):
        try:
            while True:
                self.socket.send_string(self.response)
                data = self.socket.recv_pyobj()

                # Декодирование изображения из base64
                image_bytes = base64.b64decode(data['image'])
                frame = cv2.imdecode(frombuffer(image_bytes, uint8), cv2.IMREAD_COLOR)

                # Используйте данные из списка, например:
                data_dict = data['data_list']
                print("Received Data List:", data_dict)

                # Отображение изображения
                # time.sleep(0.1)

                rgb_image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                h, w, ch = rgb_image.shape
                bytes_per_line = ch * w
                convert_to_qt_format = QImage(rgb_image.data, w, h, bytes_per_line, QImage.Format_RGB888)
                p = convert_to_qt_format.scaled(960, 540, Qt.KeepAspectRatio)
                self.change_pixmap_signal.emit(p)
                self.update_data_signal.emit(data_dict)
        except zmq.ZMQError as e:
            print(f"Ошибка ZeroMQ: {e}")
    def set_response(self, response):
        self.response = response

    def open_connection(self):
        context = zmq.Context()
        socket = context.socket(zmq.PAIR)
        socket.connect("tcp://10.42.0.1:5555")
        return socket, context

    def close_connection(self):
        # self.set_response('c')
        time.sleep(0.3)
        self.socket.setsockopt(zmq.LINGER, 0)
        self.socket.close()
        self.context.term()
        self.wait()  # Ждем завершения потока
        self.quit()



app = QApplication(sys.argv)
window = Gui()
window.show()
sys.exit(app.exec())
