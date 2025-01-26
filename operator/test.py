import sys
from PySide6.QtWidgets import (QApplication, QMainWindow, QVBoxLayout, QHBoxLayout,
                               QWidget, QLabel, QMenuBar, QMenu, QGroupBox, QGridLayout)
from PySide6.QtGui import QFont, QAction
from PySide6.QtCore import Qt

class SubmarineControlInterface(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Submarine Control Interface")
        self.setGeometry(100, 100, 1920, 1080)

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        self.layout = QHBoxLayout(self.central_widget)

        self.create_menu()
        self.create_camera_view()
        self.create_sensor_monitor()

    def create_menu(self):
        menu_bar = self.menuBar()
        connect_menu = menu_bar.addMenu("Connect")

        wifi_action = QAction("Connect via Wi-Fi", self)
        connect_menu.addAction(wifi_action)

    def create_camera_view(self):
        camera_view = QLabel("Camera View")
        camera_view.setAlignment(Qt.AlignCenter)
        camera_view.setStyleSheet("background-color: black; color: white; font-size: 20px;")
        camera_view.setFixedSize(1280, 720)
        self.layout.addWidget(camera_view)

    def create_sensor_monitor(self):
        sensor_monitor = QGroupBox("Sensor Monitor")
        sensor_monitor.setStyleSheet("QGroupBox { font-weight: bold; }")
        sensor_layout = QGridLayout()

        sensors = [
            ("Temperature", "20°C"),
            ("Pressure", "1.5 bar"),
            ("Depth", "100 m"),
            ("Battery", "85%"),
            ("Oxygen", "90%"),
            ("Salinity", "35 PSU"),
            ("Speed", "5 knots"),
            ("Heading", "180°"),
            ("Pitch", "5°"),
            ("Roll", "2°")
        ]

        for i, (sensor, value) in enumerate(sensors):
            sensor_label = QLabel(sensor)
            sensor_label.setStyleSheet("font-size: 16px;")
            value_label = QLabel(value)
            value_label.setStyleSheet("font-size: 16px; font-weight: bold;")
            sensor_layout.addWidget(sensor_label, i, 0)
            sensor_layout.addWidget(value_label, i, 1)

        sensor_monitor.setLayout(sensor_layout)
        self.layout.addWidget(sensor_monitor)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = SubmarineControlInterface()
    window.show()
    sys.exit(app.exec())
