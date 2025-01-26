from PySide6.QtCore import QThread, Signal, QSize
from PySide6.QtGui import QImage, QPixmap, QColor, Qt
from PySide6.QtWidgets import QApplication, QMainWindow

from designs.UI import Ui_MainWindow

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



def get_current_wifi():
    try:
        result = subprocess.check_output(['netsh', 'wlan', 'show', 'interfaces'])
        result = result.decode('latin-1', errors='ignore')
        for line in result.split('\n'):
            if 'SSID' in line and 'BSSID' not in line:
                return line.split(':')[1].strip()
    except subprocess.CalledProcessError:
        return None

def available_wifi():
    result = subprocess.check_output(['netsh', 'wlan', 'show', 'networks'], encoding='cp1251', errors='ignore')
    networks = []
    for line in result.split('\n'):
        if 'SSID ' in line:
            ssid = line.split(':')[1].strip()
            if ssid:  # Добавляем только непустые SSID
                networks.append(ssid)
    return networks


class Gui(QMainWindow):
    def __init__(self):
        super(Gui, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowTitle('NORD Monitor')
        self.showMaximized()

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
        self.cpu_temp_bar.set_unit('°C')

        self.roll_indicator.setOffset(90)
        self.diff_indicator.setOffset(90)

        self.roll_indicator.setLetters('L', 'R')
        self.diff_indicator.setLetters('B', 'F')

        self.roll_indicator.setFixedSize(QSize(170, 170))
        self.diff_indicator.setFixedSize(QSize(170, 170))

        self.ui.cpuusageframe.layout().addWidget(self.cpu_usage_bar)
        self.ui.cputempframe.layout().addWidget(self.cpu_temp_bar)
        self.ui.rollframe.layout().addWidget(self.roll_indicator)
        self.ui.diffframe.layout().addWidget(self.diff_indicator)

        # Создаем и запускаем поток для видео
        self.receive_thread = ReceiveThread("tcp://10.42.0.1:5555")
        self.receive_thread.change_pixmap_signal.connect(self.update_image)
        self.receive_thread.update_data_signal.connect(self.update_data)
        self.receive_thread.start()

        self.connection = False
        self.ui.pushButton.clicked.connect(self.switch_connect_to_device)
        self.ui.net.setText(get_current_wifi())
        self.prev_network = get_current_wifi()

    def switch_connect_to_device(self):
        if not self.connection:
            if get_current_wifi() != 'raspberry':
                if 'raspberry' not in available_wifi():
                    self.ui.status.setText('Сеть не найдена.')
                    return None

                os.system(f'''cmd /c "netsh wlan connect name={'raspberry'}"''')
                for i in range(100):
                    time.sleep(0.05)
                    if get_current_wifi() == 'raspberry':
                        break
                else:
                    self.ui.status.setText('Время ожидания истекло.')
                    return None
                self.ui.net.setText(get_current_wifi())

            self.receive_thread.connect_device()
            self.connection = True
            self.ui.pushButton.setText('Отключиться')
            self.ui.pushButton.setStyleSheet(u"background-color: rgb(230, 72, 60);\n"
                                             "border-radius: 2px;\n"
                                             "padding: 3px;\n"
                                             "font-size: 17px;")
            self.ui.status.setText('OK')
        else:
            self.receive_thread.disconnect_device()
            self.connection = False
            self.ui.pushButton.setText('Подключиться')
            self.ui.pushButton.setStyleSheet(u"background-color: rgb(7, 145, 92);\n"
                                             "border-radius: 2px;\n"
                                             "padding: 3px;\n"
                                             "font-size: 17px;")
            if self.prev_network:
                os.system(f'''cmd /c "netsh wlan connect name={self.prev_network}"''')
                for i in range(100):
                    time.sleep(0.05)
                    if get_current_wifi() == self.prev_network:
                        break
                else:
                    self.ui.status.setText('Время ожидания истекло.')

            self.ui.net.setText(get_current_wifi())

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
        self.ui.sats.setText(str(data['sat']))

        self.ui.depth.setText(str(data['depth']))
        self.ui.depth_target.setText(str(data['depth_target']))

        self.ui.time.setText(str(data['time']))

        self.ui.humidity_on.setText(str(data['humidity_on']))
        self.ui.pressure_on.setText(str(data['pressure_on']))
        self.ui.temp_on.setText(str(data['temp_on']))

        self.ui.temp_out.setText(str(data['temp_out']))

    def closeEvent(self, event):
        print('close')
        self.receive_thread.close()
        super().closeEvent(event)


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
            while True:
                if self.cl:
                    break
                if self.req:
                    self.socket, self.context = self.zmq_connect_to(self.address)
                    print('new')
                    self.req = False
                    self.connection = True
                if not self.connection:
                    continue

                print('go')
                # time.sleep(0.4)
                print('кидаю респонс')
                self.socket.send_string(self.response)
                print('скинул респонс')
                print('получаю дату')
                data = self.socket.recv_pyobj()
                print('Получил дату')

                # Декодирование изображения из base64
                image_bytes = base64.b64decode(data['image'])
                frame = cv2.imdecode(frombuffer(image_bytes, uint8), cv2.IMREAD_COLOR)

                # Используйте данные из списка, например:
                data_dict = data['data_dict']
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


app = QApplication(sys.argv)
window = Gui()
window.show()
sys.exit(app.exec())
