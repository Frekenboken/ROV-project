import sys
from PySide6.QtCore import *
from PySide6.QtGui import QPainter, QFont, QPen, QPalette, QColor, QPolygon
from PySide6.QtWidgets import QWidget


class QAngleBar(QWidget):

    def __init__(self, parent=None):

        QWidget.__init__(self, parent)

        self._angle = 0.0
        self._unit = '°'
        self._offset = 0
        self._margins = 10
        self._min = 0
        self._max = 359
        self._leftLetter = ''
        self._rightLetter = ''
        self._pointText = {0: "N", 45: "NE", 90: "E", 135: "SE", 180: "S",
                           225: "SW", 270: "W", 315: "NW"}

    def paintEvent(self, event):

        painter = QPainter()
        painter.begin(self)
        painter.setRenderHint(QPainter.Antialiasing)

        painter.fillRect(event.rect(), self.palette().brush(QPalette.Window))
        self.drawMarkings(painter)
        self.drawNeedle(painter)

        painter.end()

    def drawMarkings(self, painter):

        painter.save()
        painter.translate(self.width() / 2, self.height() / 2)
        scale = min((self.width() - self._margins) / 120.0,
                    (self.height() - self._margins) / 120.0)
        painter.scale(scale, scale)

        font = QFont(self.font())
        font.setPixelSize(15)
        font.setBold(400)
        painter.setFont(font)
        painter.setBrush(self.palette().brush(QPalette.Highlight))
        painter.setPen(QPen(QColor(255, 255, 255), 1.5))  # цвет и толщина линии

        i = 0
        while i < 360:

            if i % 45 == 0:
                painter.drawLine(0, -40, 0, -50)
                # painter.drawText(-8 / 2.0, -52,
                #                  self._pointText[i])
            # if (i + self._offset) % 180 == 0:
            #     painter.drawText(-8 / 2.0, -52, self._LR[i])
            else:
                painter.drawLine(0, -45, 0, -50)

            painter.rotate(15)
            i += 15
        painter.drawText(-64, 6, self._leftLetter)
        painter.drawText(54, 6, self._rightLetter)

        font.setPixelSize(17)
        font.setBold(0)
        painter.setFont(font)

        valueStr = str(abs(round(self._angle, 1))) + self._unit
        # Вычисляем координаты, чтобы текст был по центру виджета
        x = painter.boundingRect(self.rect(), 0, valueStr).width() / 2
        painter.drawText(-x, -17, valueStr)
        painter.restore()

    def drawNeedle(self, painter):

        painter.save()
        painter.translate(self.width() / 2, self.height() / 2)
        painter.rotate(self.__remap(self._angle, self._min, self._max, 0, 359) + self._offset)
        scale = min((self.width() - self._margins) / 120.0,
                    (self.height() - self._margins) / 120.0)
        painter.scale(scale, scale)

        painter.setPen(QPen(Qt.NoPen))
        # painter.setBrush(self.palette().brush(QPalette.Shadow))
        painter.setBrush(QColor(215, 38, 56))

        painter.drawPolygon(
            QPolygon([QPoint(-6, 0), QPoint(0, -45), QPoint(6, 0),
                      QPoint(0, 45), QPoint(-6, 0)])
        )

        painter.restore()

    def sizeHint(self):
        return QSize(150, 150)

    def angle(self):
        return self._angle

    def setAngle(self, angle):
        if angle != self._angle:
            self._angle = angle
            self.update()

    def setOffset(self, offset):
        self._offset = offset

    def setLetters(self, left, right):
        self._leftLetter = left
        self._rightLetter = right

    def setRange(self, min, max):
        self._min = min
        self._max = max

    def setUnit(self, unit):
        self._unit = unit

    def __remap(self, x, in_min, in_max, out_min, out_max):
        return (x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min
