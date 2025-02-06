from PyQt6.QtWidgets import QWidget, QApplication
from PyQt6.QtCore import pyqtSignal, Qt, QPointF, QTimer
from PyQt6.QtGui import QPainter, QBrush, QPen, QColor
import sys


class JoystickWidget(QWidget):
    valueChanged = pyqtSignal(float, float)  # Сигнал передает x и y

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setFixedSize(150, 150)
        self.joystick_pos = QPointF(0, 0)
        self.radius = 30  # Радиус джойстика
        self.control_area = 1.0  # Коэффициент области управления (1.0 = вся доступная зона)
        self.grabbed = False
        self.timer = QTimer()
        self.timer.timeout.connect(self.return_to_center)
        self.timer.setInterval(5)

    def set_control_area(self, scale: float):
        """Изменяет размер области управления джойстиком (0.5 - половина, 1.0 - вся область, >1.0 - больше экрана)."""
        self.control_area = max(0.2, min(scale, 2.0))  # Ограничиваем диапазон

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.RenderHint.Antialiasing)

        # Рисуем фон
        painter.setBrush(QBrush(QColor(50, 50, 50)))
        painter.setPen(QPen(QColor(40, 40, 40), 5))
        painter.drawEllipse(5, 5, self.width() - 10, self.height() - 10)

        # Рисуем джойстик
        joystick_x = self.width() / 2 + self.joystick_pos.x() * (self.width() / 2 - self.radius) * self.control_area
        joystick_y = self.height() / 2 + self.joystick_pos.y() * (self.height() / 2 - self.radius) * self.control_area

        painter.setBrush(QBrush(QColor(240, 240, 230)))
        painter.setPen(QPen(QColor(220, 220, 200), 5))
        painter.drawEllipse(QPointF(joystick_x, joystick_y), self.radius, self.radius)

    def mousePressEvent(self, event):
        if event.button() == Qt.MouseButton.LeftButton:
            self.grabbed = True
            self.update_position(event.pos())

    def mouseMoveEvent(self, event):
        if self.grabbed:
            self.update_position(event.pos())

    def mouseReleaseEvent(self, event):
        if event.button() == Qt.MouseButton.LeftButton:
            self.grabbed = False
            self.timer.start()

    def update_position(self, pos):
        dx = (pos.x() - self.width() / 2) / ((self.width() / 2 - self.radius) * self.control_area)
        dy = (pos.y() - self.height() / 2) / ((self.height() / 2 - self.radius) * self.control_area)
        distance = (dx ** 2 + dy ** 2) ** 0.5
        if distance > 1:
            dx /= distance
            dy /= distance
        self.joystick_pos = QPointF(dx, dy)
        self.valueChanged.emit(dx, -dy)
        self.update()

    def return_to_center(self):
        """Более быстрое возвращение в центр"""
        self.joystick_pos.setX(self.joystick_pos.x() * 0.7)
        self.joystick_pos.setY(self.joystick_pos.y() * 0.7)
        if abs(self.joystick_pos.x()) < 0.02 and abs(self.joystick_pos.y()) < 0.02:
            self.joystick_pos = QPointF(0, 0)
            self.timer.stop()
        self.valueChanged.emit(self.joystick_pos.x(), -self.joystick_pos.y())
        self.update()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = JoystickWidget()

    # Пример изменения области управления
    window.set_control_area(1.2)  # Увеличим область управления на 20%

    window.valueChanged.connect(lambda x, y: print(f"Joystick: {x:.2f}, {y:.2f}"))
    window.show()
    sys.exit(app.exec())
