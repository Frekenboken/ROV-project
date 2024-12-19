import cv2
from PySide6.QtCore import Qt, QThread, Signal, QPointF, QLineF
from PySide6.QtGui import QImage, QPixmap, QPen
from PySide6.QtWidgets import QApplication, QMainWindow
from UI import Ui_MainWindow
import sys
import serial
import pynmea2
import RPi.GPIO as gpio
from gpiozero import CPUTemperature
import time
import psutil
from widgets.CircularDial import Circular_dial

def millis():
    return round(time.time() * 1000)

class Gui(QMainWindow):
    def __init__(self):
        super(Gui, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        # self.ui.name.setText('TEST!')

        self.ui.btn_w.clicked.connect(lambda: VideoThread.asd())
        self.ui.btn_a.clicked.connect(lambda: print('a'))
        self.ui.btn_s.clicked.connect(lambda: print('s'))
        self.ui.btn_d.clicked.connect(lambda: print('d'))

        self.ui.dial.setMaximum(100)
        self.ui.dial.setPageStep(1) # При скроле мышкой от 1 до 3


        # Создаем и запускаем поток для видео
        self.video_thread = VideoThread()
        self.video_thread.change_pixmap_signal.connect(self.update_image)
        self.video_thread.start()

        self.control_thread = ControlThread()
        self.control_thread.start()
        
        self.compass_widget = Circular_dial(0)
        self.ui.monitor.layout().addWidget(self.compass_widget)


    def update_image(self, image):
        self.ui.name.setPixmap(QPixmap.fromImage(image))


class VideoThread(QThread):
    change_pixmap_signal = Signal(QImage)
    def run(self):
        cap = cv2.VideoCapture(0)
        
        while True:
            ret, frame = cap.read()
            if ret:
                gray_img = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
                #model = cv2.CascadeClassifier('recog-models/face.xml')
                #result = model.detectMultiScale(gray_img, scaleFactor=1.1, minNeighbors=1)
                #for (x, y, w, h) in result:
                    #cv2.rectangle(frame, (x, y), (x + w, y + h), (100, 100, 255), thickness=3)
                    #cv2.putText(frame, 'Face', (x, y - 10), cv2.FONT_HERSHEY_DUPLEX, w / 200, (255, 255, 255))
                rgb_image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                h, w, ch = rgb_image.shape
                bytes_per_line = ch * w
                convert_to_qt_format = QImage(rgb_image.data, w, h, bytes_per_line, QImage.Format_RGB888)
                p = convert_to_qt_format.scaled(640, 480, Qt.KeepAspectRatio)
                self.change_pixmap_signal.emit(p)
class ControlThread(QThread):
    def run(self):
        cpu = CPUTemperature()
        
        try:
            serArduino = serial.Serial('/dev/ttyUSB0', 38400, timeout=0.02)
            serArduino.flush()
        except:
            serArduino = False
        try:
            serGPS = serial.Serial('/dev/ttyACM0', 19200, timeout=0.011)
            serGPS.flush()
        except:
            serGPS = False
            
        curtime = date = 'NaN'
        gx = gy = tempOn = humidity = pressureIn = depth = opertime = 0
        t = millis()
        
        while True:
            if serGPS and serGPS.in_waiting > 0:
                lineGPS = serGPS.readline().decode('utf-8').rstrip()
                msg = pynmea2.parse(lineGPS)
                if isinstance(msg, pynmea2.GGA):
                    sats = msg.num_sats
                    print(f'Sats: {msg.num_sats} Time: {msg.timestamp} Lat: {msg.latitude} {msg.lat_dir} Lon: {msg.longitude} {msg.lon_dir}')
                    opertime += 1
                if isinstance(msg, pynmea2.VTG):
                    pass
                if isinstance(msg, pynmea2.RMC):
                    datetime = str(msg.datetime) #2024-01-17 16:17:30+00:00
                    if date == 'NaN':
                        date = datetime[:10]
                    time = datetime[11:19]
                
            if serArduino and serArduino.in_waiting > 0:
                arduinoData = serArduino.readline().decode('utf-8').rstrip().split(',')
                gx = float(arduinoData[0])
                gy = float(arduinoData[1])
                tempOn = float(arduinoData[2])
                humidity = float(arduinoData[3])
                pressureIn = int(arduinoData[4])
                depth = int(arduinoData[5])
                
            if millis() - t > 10000:
                with open(f'logs/{date}', 'a') as log:
                    logline = f'{curtime}: Sats: {sats}, CPUt: {int(cpu.temperature)}, CPU%: {psutil.cpu_percent()}' + '\n'
                    log.write(logline)
                print('SAVE LOG')
                t = millis()
            
            window.ui.temp_on.setText(str(tempOn) + '°C')
            window.ui.humidity_on.setText(str(humidity) + '%')
            window.ui.pressure_on.setText(str(pressureIn) + 'Pa')
            window.ui.temp_cpu.setText(str(int(cpu.temperature)) + '°C')
            window.ui.depth.setText(str(round(depth * 0.01 - 1, 2)) + 'm')


if __name__ == '__main__':      
    app = QApplication(sys.argv)
    window = Gui()
    window.show()
    sys.exit(app.exec())
