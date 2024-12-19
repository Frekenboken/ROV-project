# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'UI.ui'
##
## Created by: Qt User Interface Compiler version 6.6.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QHBoxLayout,
    QLabel, QMainWindow, QSizePolicy, QSpacerItem,
    QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1515, 1031)
        MainWindow.setMinimumSize(QSize(0, 0))
        font = QFont()
        MainWindow.setFont(font)
        MainWindow.setStyleSheet(u"background-color: rgb(14, 17, 22);\n"
"color: #FFF;\n"
"font-size: 20px;")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.monitorR_2 = QFrame(self.centralwidget)
        self.monitorR_2.setObjectName(u"monitorR_2")
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.monitorR_2.sizePolicy().hasHeightForWidth())
        self.monitorR_2.setSizePolicy(sizePolicy)
        self.monitorR_2.setFont(font)
        self.monitorR_2.setStyleSheet(u"\n"
"border-radius: 7px;\n"
"padding-top: 0px;")
        self.monitorR_2.setFrameShape(QFrame.StyledPanel)
        self.monitorR_2.setFrameShadow(QFrame.Raised)
        self.gridLayout_3 = QGridLayout(self.monitorR_2)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.cpuframe = QFrame(self.monitorR_2)
        self.cpuframe.setObjectName(u"cpuframe")
        self.cpuframe.setEnabled(True)
        sizePolicy1 = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.Maximum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.cpuframe.sizePolicy().hasHeightForWidth())
        self.cpuframe.setSizePolicy(sizePolicy1)
        self.cpuframe.setFont(font)
        self.cpuframe.setStyleSheet(u"border-radius: 7px;\n"
"padding-top: 0px;")
        self.cpuframe.setFrameShape(QFrame.StyledPanel)
        self.cpuframe.setFrameShadow(QFrame.Raised)
        self.gridLayout_44 = QGridLayout(self.cpuframe)
        self.gridLayout_44.setObjectName(u"gridLayout_44")
        self.cputempframe = QFrame(self.cpuframe)
        self.cputempframe.setObjectName(u"cputempframe")
        self.cputempframe.setFrameShape(QFrame.StyledPanel)
        self.cputempframe.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.cputempframe)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.label_41 = QLabel(self.cputempframe)
        self.label_41.setObjectName(u"label_41")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.label_41.sizePolicy().hasHeightForWidth())
        self.label_41.setSizePolicy(sizePolicy2)
        font1 = QFont()
        font1.setBold(True)
        self.label_41.setFont(font1)
        self.label_41.setAlignment(Qt.AlignCenter)

        self.verticalLayout_3.addWidget(self.label_41)


        self.gridLayout_44.addWidget(self.cputempframe, 5, 0, 1, 1)

        self.cpuusageframe = QFrame(self.cpuframe)
        self.cpuusageframe.setObjectName(u"cpuusageframe")
        self.cpuusageframe.setEnabled(True)
        sizePolicy1.setHeightForWidth(self.cpuusageframe.sizePolicy().hasHeightForWidth())
        self.cpuusageframe.setSizePolicy(sizePolicy1)
        self.cpuusageframe.setFont(font)
        self.cpuusageframe.setStyleSheet(u"border-radius: 7px;\n"
"padding-top: 0px;")
        self.cpuusageframe.setFrameShape(QFrame.StyledPanel)
        self.cpuusageframe.setFrameShadow(QFrame.Raised)
        self.gridLayout_51 = QGridLayout(self.cpuusageframe)
        self.gridLayout_51.setObjectName(u"gridLayout_51")
        self.label_50 = QLabel(self.cpuusageframe)
        self.label_50.setObjectName(u"label_50")
        sizePolicy2.setHeightForWidth(self.label_50.sizePolicy().hasHeightForWidth())
        self.label_50.setSizePolicy(sizePolicy2)
        self.label_50.setFont(font1)
        self.label_50.setStyleSheet(u"")
        self.label_50.setAlignment(Qt.AlignCenter)

        self.gridLayout_51.addWidget(self.label_50, 0, 0, 1, 1)


        self.gridLayout_44.addWidget(self.cpuusageframe, 4, 0, 1, 1)

        self.frame_16 = QFrame(self.cpuframe)
        self.frame_16.setObjectName(u"frame_16")
        self.frame_16.setEnabled(True)
        sizePolicy1.setHeightForWidth(self.frame_16.sizePolicy().hasHeightForWidth())
        self.frame_16.setSizePolicy(sizePolicy1)
        self.frame_16.setFont(font)
        self.frame_16.setStyleSheet(u"background-color: rgb(134, 110, 255);\n"
"border-radius: 13px;\n"
"padding-top: 0px;")
        self.frame_16.setFrameShape(QFrame.StyledPanel)
        self.frame_16.setFrameShadow(QFrame.Raised)
        self.gridLayout_18 = QGridLayout(self.frame_16)
        self.gridLayout_18.setObjectName(u"gridLayout_18")
        self.cpu = QLabel(self.frame_16)
        self.cpu.setObjectName(u"cpu")
        sizePolicy2.setHeightForWidth(self.cpu.sizePolicy().hasHeightForWidth())
        self.cpu.setSizePolicy(sizePolicy2)
        self.cpu.setFont(font1)
        self.cpu.setStyleSheet(u"background-color: rgb(134, 110, 255);\n"
"border-radius: 7px;\n"
"padding-top: 0px;")
        self.cpu.setAlignment(Qt.AlignCenter)

        self.gridLayout_18.addWidget(self.cpu, 0, 0, 1, 1)


        self.gridLayout_44.addWidget(self.frame_16, 0, 0, 1, 1)


        self.gridLayout_3.addWidget(self.cpuframe, 1, 1, 1, 1)

        self.frame_41 = QFrame(self.monitorR_2)
        self.frame_41.setObjectName(u"frame_41")
        self.frame_41.setEnabled(True)
        sizePolicy1.setHeightForWidth(self.frame_41.sizePolicy().hasHeightForWidth())
        self.frame_41.setSizePolicy(sizePolicy1)
        self.frame_41.setFont(font)
        self.frame_41.setStyleSheet(u"background-color: rgb(14, 17, 22);\n"
"border-radius: 7px;\n"
"padding-top: 0px;")
        self.frame_41.setFrameShape(QFrame.StyledPanel)
        self.frame_41.setFrameShadow(QFrame.Raised)
        self.gridLayout_45 = QGridLayout(self.frame_41)
        self.gridLayout_45.setObjectName(u"gridLayout_45")

        self.gridLayout_3.addWidget(self.frame_41, 2, 1, 1, 1)


        self.horizontalLayout.addWidget(self.monitorR_2)

        self.frame_3 = QFrame(self.centralwidget)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setEnabled(True)
        sizePolicy3 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.frame_3.sizePolicy().hasHeightForWidth())
        self.frame_3.setSizePolicy(sizePolicy3)
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_3)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 5, 0, 0)
        self.frame = QFrame(self.frame_3)
        self.frame.setObjectName(u"frame")
        sizePolicy3.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy3)
        self.frame.setMinimumSize(QSize(0, 0))
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.frame_2 = QFrame(self.frame)
        self.frame_2.setObjectName(u"frame_2")
        sizePolicy4 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy4)
        self.frame_2.setMinimumSize(QSize(980, 560))
        self.frame_2.setMaximumSize(QSize(980, 560))
        self.frame_2.setStyleSheet(u"background-color: rgb(134, 110, 255);\n"
"border-radius: 13px;\n"
"padding-top: 0px;")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.frame_2)
        self.label.setObjectName(u"label")
        sizePolicy5 = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.MinimumExpanding)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy5)
        self.label.setMinimumSize(QSize(960, 540))
        self.label.setMaximumSize(QSize(960, 540))
        self.label.setFont(font1)
        self.label.setMouseTracking(False)
        self.label.setAlignment(Qt.AlignCenter)
        self.label.setMargin(0)
        self.label.setIndent(0)

        self.horizontalLayout_3.addWidget(self.label)


        self.horizontalLayout_4.addWidget(self.frame_2)


        self.verticalLayout_2.addWidget(self.frame)

        self.RTframe = QFrame(self.frame_3)
        self.RTframe.setObjectName(u"RTframe")
        sizePolicy4.setHeightForWidth(self.RTframe.sizePolicy().hasHeightForWidth())
        self.RTframe.setSizePolicy(sizePolicy4)
        self.RTframe.setMinimumSize(QSize(640, 300))
        self.RTframe.setFrameShape(QFrame.StyledPanel)
        self.RTframe.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.RTframe)
        self.horizontalLayout_2.setSpacing(10)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame_13 = QFrame(self.RTframe)
        self.frame_13.setObjectName(u"frame_13")
        sizePolicy3.setHeightForWidth(self.frame_13.sizePolicy().hasHeightForWidth())
        self.frame_13.setSizePolicy(sizePolicy3)
        self.frame_13.setFrameShape(QFrame.StyledPanel)
        self.frame_13.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.frame_13)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_4)

        self.rollframe = QFrame(self.frame_13)
        self.rollframe.setObjectName(u"rollframe")
        self.rollframe.setStyleSheet(u"padding-inline: 20px;")
        self.rollframe.setFrameShape(QFrame.StyledPanel)
        self.rollframe.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.rollframe)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.frame_27 = QFrame(self.rollframe)
        self.frame_27.setObjectName(u"frame_27")
        self.frame_27.setEnabled(True)
        sizePolicy1.setHeightForWidth(self.frame_27.sizePolicy().hasHeightForWidth())
        self.frame_27.setSizePolicy(sizePolicy1)
        self.frame_27.setMinimumSize(QSize(0, 0))
        self.frame_27.setFont(font)
        self.frame_27.setStyleSheet(u"background-color: rgb(134, 110, 255);\n"
"border-radius: 7px;\n"
"padding-top: 0px;")
        self.frame_27.setFrameShape(QFrame.StyledPanel)
        self.frame_27.setFrameShadow(QFrame.Raised)
        self.gridLayout_27 = QGridLayout(self.frame_27)
        self.gridLayout_27.setObjectName(u"gridLayout_27")
        self.cpu_5 = QLabel(self.frame_27)
        self.cpu_5.setObjectName(u"cpu_5")
        sizePolicy2.setHeightForWidth(self.cpu_5.sizePolicy().hasHeightForWidth())
        self.cpu_5.setSizePolicy(sizePolicy2)
        self.cpu_5.setFont(font1)
        self.cpu_5.setStyleSheet(u"background-color: rgb(134, 110, 255);\n"
"border-radius: 7px;\n"
"padding-top: 0px;")
        self.cpu_5.setAlignment(Qt.AlignCenter)

        self.gridLayout_27.addWidget(self.cpu_5, 0, 0, 1, 1)


        self.verticalLayout_5.addWidget(self.frame_27)


        self.horizontalLayout_5.addWidget(self.rollframe)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_3)


        self.horizontalLayout_2.addWidget(self.frame_13)

        self.frame_5 = QFrame(self.RTframe)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setMinimumSize(QSize(0, 0))
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.frame_5)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer)

        self.diffframe = QFrame(self.frame_5)
        self.diffframe.setObjectName(u"diffframe")
        self.diffframe.setFrameShape(QFrame.StyledPanel)
        self.diffframe.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.diffframe)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.frame_26 = QFrame(self.diffframe)
        self.frame_26.setObjectName(u"frame_26")
        self.frame_26.setEnabled(True)
        sizePolicy1.setHeightForWidth(self.frame_26.sizePolicy().hasHeightForWidth())
        self.frame_26.setSizePolicy(sizePolicy1)
        self.frame_26.setMinimumSize(QSize(0, 0))
        self.frame_26.setMaximumSize(QSize(200, 16777215))
        self.frame_26.setFont(font)
        self.frame_26.setStyleSheet(u"background-color: rgb(134, 110, 255);\n"
"border-radius: 7px;\n"
"padding-top: 0px;")
        self.frame_26.setFrameShape(QFrame.StyledPanel)
        self.frame_26.setFrameShadow(QFrame.Raised)
        self.gridLayout_26 = QGridLayout(self.frame_26)
        self.gridLayout_26.setObjectName(u"gridLayout_26")
        self.cpu_3 = QLabel(self.frame_26)
        self.cpu_3.setObjectName(u"cpu_3")
        sizePolicy2.setHeightForWidth(self.cpu_3.sizePolicy().hasHeightForWidth())
        self.cpu_3.setSizePolicy(sizePolicy2)
        self.cpu_3.setFont(font1)
        self.cpu_3.setStyleSheet(u"background-color: rgb(134, 110, 255);\n"
"border-radius: 7px;\n"
"padding-top: 0px;")
        self.cpu_3.setAlignment(Qt.AlignCenter)

        self.gridLayout_26.addWidget(self.cpu_3, 0, 0, 1, 1)


        self.verticalLayout_4.addWidget(self.frame_26)


        self.horizontalLayout_6.addWidget(self.diffframe)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_2)


        self.horizontalLayout_2.addWidget(self.frame_5)


        self.verticalLayout_2.addWidget(self.RTframe)


        self.horizontalLayout.addWidget(self.frame_3)

        self.monitorR = QFrame(self.centralwidget)
        self.monitorR.setObjectName(u"monitorR")
        sizePolicy.setHeightForWidth(self.monitorR.sizePolicy().hasHeightForWidth())
        self.monitorR.setSizePolicy(sizePolicy)
        self.monitorR.setFont(font)
        self.monitorR.setFrameShape(QFrame.StyledPanel)
        self.monitorR.setFrameShadow(QFrame.Raised)
        self.gridLayout_2 = QGridLayout(self.monitorR)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.frame_8 = QFrame(self.monitorR)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setEnabled(True)
        sizePolicy1.setHeightForWidth(self.frame_8.sizePolicy().hasHeightForWidth())
        self.frame_8.setSizePolicy(sizePolicy1)
        self.frame_8.setFont(font)
        self.frame_8.setStyleSheet(u"background-color: rgb(134, 110, 255);\n"
"border-radius: 13px;\n"
"padding-top: 0px;")
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.gridLayout_15 = QGridLayout(self.frame_8)
        self.gridLayout_15.setObjectName(u"gridLayout_15")
        self.frame_7 = QFrame(self.frame_8)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setEnabled(True)
        sizePolicy1.setHeightForWidth(self.frame_7.sizePolicy().hasHeightForWidth())
        self.frame_7.setSizePolicy(sizePolicy1)
        self.frame_7.setFont(font)
        self.frame_7.setStyleSheet(u"background-color: rgb(14, 17, 22);\n"
"border-radius: 7px;\n"
"padding-top: 0px;")
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.gridLayout_11 = QGridLayout(self.frame_7)
        self.gridLayout_11.setObjectName(u"gridLayout_11")
        self.speed = QLabel(self.frame_7)
        self.speed.setObjectName(u"speed")
        sizePolicy6 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Preferred)
        sizePolicy6.setHorizontalStretch(0)
        sizePolicy6.setVerticalStretch(0)
        sizePolicy6.setHeightForWidth(self.speed.sizePolicy().hasHeightForWidth())
        self.speed.setSizePolicy(sizePolicy6)
        self.speed.setMinimumSize(QSize(100, 0))
        self.speed.setFont(font)
        self.speed.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_11.addWidget(self.speed, 0, 1, 1, 1)

        self.label_8 = QLabel(self.frame_7)
        self.label_8.setObjectName(u"label_8")
        sizePolicy2.setHeightForWidth(self.label_8.sizePolicy().hasHeightForWidth())
        self.label_8.setSizePolicy(sizePolicy2)
        self.label_8.setFont(font)

        self.gridLayout_11.addWidget(self.label_8, 0, 0, 1, 1)


        self.gridLayout_15.addWidget(self.frame_7, 4, 0, 1, 1)

        self.frame_6 = QFrame(self.frame_8)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setEnabled(True)
        sizePolicy1.setHeightForWidth(self.frame_6.sizePolicy().hasHeightForWidth())
        self.frame_6.setSizePolicy(sizePolicy1)
        self.frame_6.setFont(font)
        self.frame_6.setStyleSheet(u"background-color: rgb(14, 17, 22);\n"
"border-radius: 7px;\n"
"padding-top: 0px;")
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.gridLayout_10 = QGridLayout(self.frame_6)
        self.gridLayout_10.setObjectName(u"gridLayout_10")
        self.sats = QLabel(self.frame_6)
        self.sats.setObjectName(u"sats")
        sizePolicy6.setHeightForWidth(self.sats.sizePolicy().hasHeightForWidth())
        self.sats.setSizePolicy(sizePolicy6)
        self.sats.setMinimumSize(QSize(100, 0))
        self.sats.setFont(font)
        self.sats.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_10.addWidget(self.sats, 0, 1, 1, 1)

        self.label_7 = QLabel(self.frame_6)
        self.label_7.setObjectName(u"label_7")
        sizePolicy2.setHeightForWidth(self.label_7.sizePolicy().hasHeightForWidth())
        self.label_7.setSizePolicy(sizePolicy2)
        self.label_7.setFont(font)

        self.gridLayout_10.addWidget(self.label_7, 0, 0, 1, 1)


        self.gridLayout_15.addWidget(self.frame_6, 3, 0, 1, 1)

        self.label_12 = QLabel(self.frame_8)
        self.label_12.setObjectName(u"label_12")
        sizePolicy2.setHeightForWidth(self.label_12.sizePolicy().hasHeightForWidth())
        self.label_12.setSizePolicy(sizePolicy2)
        self.label_12.setFont(font1)
        self.label_12.setStyleSheet(u"color: #FFF;")
        self.label_12.setAlignment(Qt.AlignCenter)

        self.gridLayout_15.addWidget(self.label_12, 0, 0, 1, 1)

        self.frame_17 = QFrame(self.frame_8)
        self.frame_17.setObjectName(u"frame_17")
        self.frame_17.setEnabled(True)
        sizePolicy1.setHeightForWidth(self.frame_17.sizePolicy().hasHeightForWidth())
        self.frame_17.setSizePolicy(sizePolicy1)
        self.frame_17.setFont(font)
        self.frame_17.setStyleSheet(u"background-color: rgb(14, 17, 22);\n"
"border-radius: 7px;\n"
"padding-top: 0px;")
        self.frame_17.setFrameShape(QFrame.StyledPanel)
        self.frame_17.setFrameShadow(QFrame.Raised)
        self.gridLayout_28 = QGridLayout(self.frame_17)
        self.gridLayout_28.setObjectName(u"gridLayout_28")
        self.lat = QLabel(self.frame_17)
        self.lat.setObjectName(u"lat")
        sizePolicy6.setHeightForWidth(self.lat.sizePolicy().hasHeightForWidth())
        self.lat.setSizePolicy(sizePolicy6)
        self.lat.setMinimumSize(QSize(100, 0))
        self.lat.setFont(font)
        self.lat.setAlignment(Qt.AlignCenter)

        self.gridLayout_28.addWidget(self.lat, 0, 0, 1, 1)


        self.gridLayout_15.addWidget(self.frame_17, 1, 0, 1, 1)

        self.frame_19 = QFrame(self.frame_8)
        self.frame_19.setObjectName(u"frame_19")
        self.frame_19.setEnabled(True)
        sizePolicy1.setHeightForWidth(self.frame_19.sizePolicy().hasHeightForWidth())
        self.frame_19.setSizePolicy(sizePolicy1)
        self.frame_19.setFont(font)
        self.frame_19.setStyleSheet(u"background-color: rgb(14, 17, 22);\n"
"border-radius: 7px;\n"
"padding-top: 0px;")
        self.frame_19.setFrameShape(QFrame.StyledPanel)
        self.frame_19.setFrameShadow(QFrame.Raised)
        self.gridLayout_29 = QGridLayout(self.frame_19)
        self.gridLayout_29.setObjectName(u"gridLayout_29")
        self.lon = QLabel(self.frame_19)
        self.lon.setObjectName(u"lon")
        sizePolicy6.setHeightForWidth(self.lon.sizePolicy().hasHeightForWidth())
        self.lon.setSizePolicy(sizePolicy6)
        self.lon.setMinimumSize(QSize(100, 0))
        self.lon.setFont(font)
        self.lon.setAlignment(Qt.AlignCenter)

        self.gridLayout_29.addWidget(self.lon, 0, 0, 1, 1)


        self.gridLayout_15.addWidget(self.frame_19, 2, 0, 1, 1)


        self.gridLayout_2.addWidget(self.frame_8, 11, 1, 1, 1)

        self.frame_18 = QFrame(self.monitorR)
        self.frame_18.setObjectName(u"frame_18")
        self.frame_18.setEnabled(True)
        sizePolicy1.setHeightForWidth(self.frame_18.sizePolicy().hasHeightForWidth())
        self.frame_18.setSizePolicy(sizePolicy1)
        self.frame_18.setFont(font)
        self.frame_18.setStyleSheet(u"background-color: rgb(134, 110, 255);\n"
"border-radius: 13px;\n"
"padding-top: 0px;")
        self.frame_18.setFrameShape(QFrame.StyledPanel)
        self.frame_18.setFrameShadow(QFrame.Raised)
        self.gridLayout_20 = QGridLayout(self.frame_18)
        self.gridLayout_20.setObjectName(u"gridLayout_20")
        self.label_17 = QLabel(self.frame_18)
        self.label_17.setObjectName(u"label_17")
        sizePolicy2.setHeightForWidth(self.label_17.sizePolicy().hasHeightForWidth())
        self.label_17.setSizePolicy(sizePolicy2)
        self.label_17.setFont(font1)
        self.label_17.setStyleSheet(u"color: #FFF;")
        self.label_17.setAlignment(Qt.AlignCenter)

        self.gridLayout_20.addWidget(self.label_17, 0, 0, 1, 1)

        self.frame_11 = QFrame(self.frame_18)
        self.frame_11.setObjectName(u"frame_11")
        self.frame_11.setEnabled(True)
        sizePolicy1.setHeightForWidth(self.frame_11.sizePolicy().hasHeightForWidth())
        self.frame_11.setSizePolicy(sizePolicy1)
        self.frame_11.setFont(font)
        self.frame_11.setStyleSheet(u"background-color: rgb(14, 17, 22);\n"
"border-radius: 7px;\n"
"padding-top: 0px;")
        self.frame_11.setFrameShape(QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QFrame.Raised)
        self.gridLayout_13 = QGridLayout(self.frame_11)
        self.gridLayout_13.setObjectName(u"gridLayout_13")
        self.depth_target = QLabel(self.frame_11)
        self.depth_target.setObjectName(u"depth_target")
        sizePolicy6.setHeightForWidth(self.depth_target.sizePolicy().hasHeightForWidth())
        self.depth_target.setSizePolicy(sizePolicy6)
        self.depth_target.setMinimumSize(QSize(100, 0))
        self.depth_target.setFont(font)
        self.depth_target.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_13.addWidget(self.depth_target, 0, 1, 1, 1)

        self.label_10 = QLabel(self.frame_11)
        self.label_10.setObjectName(u"label_10")
        sizePolicy2.setHeightForWidth(self.label_10.sizePolicy().hasHeightForWidth())
        self.label_10.setSizePolicy(sizePolicy2)
        self.label_10.setFont(font)

        self.gridLayout_13.addWidget(self.label_10, 0, 0, 1, 1)


        self.gridLayout_20.addWidget(self.frame_11, 1, 0, 1, 1)

        self.frame_10 = QFrame(self.frame_18)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setEnabled(True)
        sizePolicy1.setHeightForWidth(self.frame_10.sizePolicy().hasHeightForWidth())
        self.frame_10.setSizePolicy(sizePolicy1)
        self.frame_10.setFont(font)
        self.frame_10.setStyleSheet(u"background-color: rgb(14, 17, 22);\n"
"border-radius: 7px;\n"
"padding-top: 0px;")
        self.frame_10.setFrameShape(QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QFrame.Raised)
        self.gridLayout_12 = QGridLayout(self.frame_10)
        self.gridLayout_12.setObjectName(u"gridLayout_12")
        self.label_9 = QLabel(self.frame_10)
        self.label_9.setObjectName(u"label_9")
        sizePolicy2.setHeightForWidth(self.label_9.sizePolicy().hasHeightForWidth())
        self.label_9.setSizePolicy(sizePolicy2)
        self.label_9.setFont(font)

        self.gridLayout_12.addWidget(self.label_9, 0, 0, 1, 1)

        self.depth = QLabel(self.frame_10)
        self.depth.setObjectName(u"depth")
        sizePolicy6.setHeightForWidth(self.depth.sizePolicy().hasHeightForWidth())
        self.depth.setSizePolicy(sizePolicy6)
        self.depth.setMinimumSize(QSize(100, 0))
        self.depth.setFont(font)
        self.depth.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_12.addWidget(self.depth, 0, 1, 1, 1)


        self.gridLayout_20.addWidget(self.frame_10, 2, 0, 1, 1)


        self.gridLayout_2.addWidget(self.frame_18, 1, 1, 1, 1)

        self.frame_21 = QFrame(self.monitorR)
        self.frame_21.setObjectName(u"frame_21")
        self.frame_21.setEnabled(True)
        sizePolicy1.setHeightForWidth(self.frame_21.sizePolicy().hasHeightForWidth())
        self.frame_21.setSizePolicy(sizePolicy1)
        self.frame_21.setFont(font)
        self.frame_21.setStyleSheet(u"background-color: rgb(134, 110, 255);\n"
"border-radius: 13px;\n"
"padding-top: 0px;")
        self.frame_21.setFrameShape(QFrame.StyledPanel)
        self.frame_21.setFrameShadow(QFrame.Raised)
        self.gridLayout_23 = QGridLayout(self.frame_21)
        self.gridLayout_23.setObjectName(u"gridLayout_23")
        self.frame_22 = QFrame(self.frame_21)
        self.frame_22.setObjectName(u"frame_22")
        self.frame_22.setEnabled(True)
        sizePolicy1.setHeightForWidth(self.frame_22.sizePolicy().hasHeightForWidth())
        self.frame_22.setSizePolicy(sizePolicy1)
        self.frame_22.setFont(font)
        self.frame_22.setStyleSheet(u"background-color: rgb(14, 17, 22);\n"
"border-radius: 7px;\n"
"padding-top: 0px;")
        self.frame_22.setFrameShape(QFrame.StyledPanel)
        self.frame_22.setFrameShadow(QFrame.Raised)
        self.gridLayout_24 = QGridLayout(self.frame_22)
        self.gridLayout_24.setObjectName(u"gridLayout_24")
        self.label_21 = QLabel(self.frame_22)
        self.label_21.setObjectName(u"label_21")
        sizePolicy2.setHeightForWidth(self.label_21.sizePolicy().hasHeightForWidth())
        self.label_21.setSizePolicy(sizePolicy2)
        self.label_21.setFont(font)

        self.gridLayout_24.addWidget(self.label_21, 0, 0, 1, 1)

        self.temp_on = QLabel(self.frame_22)
        self.temp_on.setObjectName(u"temp_on")
        sizePolicy6.setHeightForWidth(self.temp_on.sizePolicy().hasHeightForWidth())
        self.temp_on.setSizePolicy(sizePolicy6)
        self.temp_on.setMinimumSize(QSize(100, 0))
        self.temp_on.setFont(font)
        self.temp_on.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_24.addWidget(self.temp_on, 0, 1, 1, 1)


        self.gridLayout_23.addWidget(self.frame_22, 1, 0, 1, 1)

        self.frame_23 = QFrame(self.frame_21)
        self.frame_23.setObjectName(u"frame_23")
        self.frame_23.setEnabled(True)
        sizePolicy1.setHeightForWidth(self.frame_23.sizePolicy().hasHeightForWidth())
        self.frame_23.setSizePolicy(sizePolicy1)
        self.frame_23.setFont(font)
        self.frame_23.setStyleSheet(u"background-color: rgb(14, 17, 22);\n"
"border-radius: 7px;\n"
"padding-top: 0px;")
        self.frame_23.setFrameShape(QFrame.StyledPanel)
        self.frame_23.setFrameShadow(QFrame.Raised)
        self.gridLayout_25 = QGridLayout(self.frame_23)
        self.gridLayout_25.setObjectName(u"gridLayout_25")
        self.pressure_on = QLabel(self.frame_23)
        self.pressure_on.setObjectName(u"pressure_on")
        sizePolicy6.setHeightForWidth(self.pressure_on.sizePolicy().hasHeightForWidth())
        self.pressure_on.setSizePolicy(sizePolicy6)
        self.pressure_on.setMinimumSize(QSize(100, 0))
        self.pressure_on.setFont(font)
        self.pressure_on.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_25.addWidget(self.pressure_on, 0, 1, 1, 1)

        self.label_22 = QLabel(self.frame_23)
        self.label_22.setObjectName(u"label_22")
        sizePolicy2.setHeightForWidth(self.label_22.sizePolicy().hasHeightForWidth())
        self.label_22.setSizePolicy(sizePolicy2)
        self.label_22.setFont(font)

        self.gridLayout_25.addWidget(self.label_22, 0, 0, 1, 1)


        self.gridLayout_23.addWidget(self.frame_23, 2, 0, 1, 1)

        self.label_20 = QLabel(self.frame_21)
        self.label_20.setObjectName(u"label_20")
        sizePolicy2.setHeightForWidth(self.label_20.sizePolicy().hasHeightForWidth())
        self.label_20.setSizePolicy(sizePolicy2)
        self.label_20.setFont(font1)
        self.label_20.setStyleSheet(u"color: #FFF;")
        self.label_20.setAlignment(Qt.AlignCenter)

        self.gridLayout_23.addWidget(self.label_20, 0, 0, 1, 1)

        self.frame_12 = QFrame(self.frame_21)
        self.frame_12.setObjectName(u"frame_12")
        self.frame_12.setEnabled(True)
        sizePolicy1.setHeightForWidth(self.frame_12.sizePolicy().hasHeightForWidth())
        self.frame_12.setSizePolicy(sizePolicy1)
        self.frame_12.setFont(font)
        self.frame_12.setStyleSheet(u"background-color: rgb(14, 17, 22);\n"
"border-radius: 7px;\n"
"padding-top: 0px;")
        self.frame_12.setFrameShape(QFrame.StyledPanel)
        self.frame_12.setFrameShadow(QFrame.Raised)
        self.gridLayout_14 = QGridLayout(self.frame_12)
        self.gridLayout_14.setObjectName(u"gridLayout_14")
        self.label_11 = QLabel(self.frame_12)
        self.label_11.setObjectName(u"label_11")
        sizePolicy2.setHeightForWidth(self.label_11.sizePolicy().hasHeightForWidth())
        self.label_11.setSizePolicy(sizePolicy2)
        self.label_11.setFont(font)

        self.gridLayout_14.addWidget(self.label_11, 0, 0, 1, 1)

        self.humidity_on = QLabel(self.frame_12)
        self.humidity_on.setObjectName(u"humidity_on")
        sizePolicy6.setHeightForWidth(self.humidity_on.sizePolicy().hasHeightForWidth())
        self.humidity_on.setSizePolicy(sizePolicy6)
        self.humidity_on.setMinimumSize(QSize(100, 0))
        self.humidity_on.setFont(font)
        self.humidity_on.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_14.addWidget(self.humidity_on, 0, 1, 1, 1)


        self.gridLayout_23.addWidget(self.frame_12, 3, 0, 1, 1)


        self.gridLayout_2.addWidget(self.frame_21, 2, 1, 1, 1)

        self.frame_9 = QFrame(self.monitorR)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setEnabled(True)
        sizePolicy1.setHeightForWidth(self.frame_9.sizePolicy().hasHeightForWidth())
        self.frame_9.setSizePolicy(sizePolicy1)
        self.frame_9.setFont(font)
        self.frame_9.setStyleSheet(u"background-color: rgb(134, 110, 255);\n"
"border-radius: 13px;\n"
"padding-top: 0px;")
        self.frame_9.setFrameShape(QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Raised)
        self.gridLayout_9 = QGridLayout(self.frame_9)
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.label_6 = QLabel(self.frame_9)
        self.label_6.setObjectName(u"label_6")
        sizePolicy2.setHeightForWidth(self.label_6.sizePolicy().hasHeightForWidth())
        self.label_6.setSizePolicy(sizePolicy2)
        self.label_6.setFont(font1)
        self.label_6.setStyleSheet(u"color: #FFF;")
        self.label_6.setAlignment(Qt.AlignCenter)

        self.gridLayout_9.addWidget(self.label_6, 0, 0, 1, 1)

        self.frame_20 = QFrame(self.frame_9)
        self.frame_20.setObjectName(u"frame_20")
        self.frame_20.setEnabled(True)
        sizePolicy1.setHeightForWidth(self.frame_20.sizePolicy().hasHeightForWidth())
        self.frame_20.setSizePolicy(sizePolicy1)
        self.frame_20.setFont(font)
        self.frame_20.setStyleSheet(u"background-color: rgb(14, 17, 22);\n"
"border-radius: 7px;\n"
"padding-top: 0px;")
        self.frame_20.setFrameShape(QFrame.StyledPanel)
        self.frame_20.setFrameShadow(QFrame.Raised)
        self.gridLayout_22 = QGridLayout(self.frame_20)
        self.gridLayout_22.setObjectName(u"gridLayout_22")
        self.time = QLabel(self.frame_20)
        self.time.setObjectName(u"time")
        sizePolicy6.setHeightForWidth(self.time.sizePolicy().hasHeightForWidth())
        self.time.setSizePolicy(sizePolicy6)
        self.time.setMinimumSize(QSize(100, 0))
        self.time.setFont(font)
        self.time.setAlignment(Qt.AlignCenter)

        self.gridLayout_22.addWidget(self.time, 0, 0, 1, 1)


        self.gridLayout_9.addWidget(self.frame_20, 1, 0, 1, 1)


        self.gridLayout_2.addWidget(self.frame_9, 8, 1, 1, 1)

        self.frame_24 = QFrame(self.monitorR)
        self.frame_24.setObjectName(u"frame_24")
        self.frame_24.setEnabled(True)
        sizePolicy1.setHeightForWidth(self.frame_24.sizePolicy().hasHeightForWidth())
        self.frame_24.setSizePolicy(sizePolicy1)
        self.frame_24.setFont(font)
        self.frame_24.setStyleSheet(u"background-color: rgb(134, 110, 255);\n"
"border-radius: 13px;\n"
"padding-top: 0px;")
        self.frame_24.setFrameShape(QFrame.StyledPanel)
        self.frame_24.setFrameShadow(QFrame.Raised)
        self.gridLayout_19 = QGridLayout(self.frame_24)
        self.gridLayout_19.setObjectName(u"gridLayout_19")
        self.frame_25 = QFrame(self.frame_24)
        self.frame_25.setObjectName(u"frame_25")
        self.frame_25.setEnabled(True)
        sizePolicy1.setHeightForWidth(self.frame_25.sizePolicy().hasHeightForWidth())
        self.frame_25.setSizePolicy(sizePolicy1)
        self.frame_25.setFont(font)
        self.frame_25.setStyleSheet(u"background-color: rgb(14, 17, 22);\n"
"border-radius: 7px;\n"
"padding-top: 0px;")
        self.frame_25.setFrameShape(QFrame.StyledPanel)
        self.frame_25.setFrameShadow(QFrame.Raised)
        self.gridLayout_30 = QGridLayout(self.frame_25)
        self.gridLayout_30.setObjectName(u"gridLayout_30")
        self.label_14 = QLabel(self.frame_25)
        self.label_14.setObjectName(u"label_14")
        sizePolicy2.setHeightForWidth(self.label_14.sizePolicy().hasHeightForWidth())
        self.label_14.setSizePolicy(sizePolicy2)
        font2 = QFont()
        font2.setBold(False)
        self.label_14.setFont(font2)
        self.label_14.setStyleSheet(u"color: #FFF;")

        self.gridLayout_30.addWidget(self.label_14, 0, 0, 1, 1)

        self.temp_out = QLabel(self.frame_25)
        self.temp_out.setObjectName(u"temp_out")
        sizePolicy6.setHeightForWidth(self.temp_out.sizePolicy().hasHeightForWidth())
        self.temp_out.setSizePolicy(sizePolicy6)
        self.temp_out.setMinimumSize(QSize(100, 0))
        self.temp_out.setFont(font)
        self.temp_out.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_30.addWidget(self.temp_out, 0, 1, 1, 1)


        self.gridLayout_19.addWidget(self.frame_25, 1, 0, 1, 1)

        self.label_15 = QLabel(self.frame_24)
        self.label_15.setObjectName(u"label_15")
        sizePolicy2.setHeightForWidth(self.label_15.sizePolicy().hasHeightForWidth())
        self.label_15.setSizePolicy(sizePolicy2)
        self.label_15.setFont(font1)
        self.label_15.setStyleSheet(u"color: #FFF;")
        self.label_15.setAlignment(Qt.AlignCenter)

        self.gridLayout_19.addWidget(self.label_15, 0, 0, 1, 1)


        self.gridLayout_2.addWidget(self.frame_24, 3, 1, 1, 1)


        self.horizontalLayout.addWidget(self.monitorR)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label_41.setText(QCoreApplication.translate("MainWindow", u"\u0422\u0435\u043c\u043f\u0435\u0440\u0430\u0442\u0443\u0440\u0430", None))
        self.label_50.setText(QCoreApplication.translate("MainWindow", u" \u0417\u0430\u0433\u0440\u0443\u0437\u043a\u0430", None))
        self.cpu.setText(QCoreApplication.translate("MainWindow", u"CPU", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u0417\u0430\u0433\u0440\u0443\u0437\u043a\u0430 \u043a\u0430\u043c\u0435\u0440\u044b...", None))
        self.cpu_5.setText(QCoreApplication.translate("MainWindow", u"\u041a\u0440\u0435\u043d", None))
        self.cpu_3.setText(QCoreApplication.translate("MainWindow", u"\u0414\u0438\u0444\u0444\u0435\u0440\u0435\u043d\u0442", None))
        self.speed.setText(QCoreApplication.translate("MainWindow", u"N/A", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"\u0421\u043a\u043e\u0440\u043e\u0441\u0442\u044c", None))
        self.sats.setText(QCoreApplication.translate("MainWindow", u"N/A", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"\u0421\u043f\u0443\u0442\u043d\u0438\u043a\u0438", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"GPS", None))
        self.lat.setText(QCoreApplication.translate("MainWindow", u"N/A", None))
        self.lon.setText(QCoreApplication.translate("MainWindow", u"N/A", None))
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"\u0413\u043b\u0443\u0431\u0438\u043d\u0430", None))
        self.depth_target.setText(QCoreApplication.translate("MainWindow", u"N/A", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"\u0426\u0435\u043b\u044c", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"\u0422\u0435\u043a\u0443\u0449\u0430\u044f", None))
        self.depth.setText(QCoreApplication.translate("MainWindow", u"N/A", None))
        self.label_21.setText(QCoreApplication.translate("MainWindow", u"\u0422\u0435\u043c\u043f\u0435\u0440\u0430\u0442\u0443\u0440\u0430", None))
        self.temp_on.setText(QCoreApplication.translate("MainWindow", u"N/A", None))
        self.pressure_on.setText(QCoreApplication.translate("MainWindow", u"N/A", None))
        self.label_22.setText(QCoreApplication.translate("MainWindow", u"\u0414\u0430\u0432\u043b\u0435\u043d\u0438\u0435", None))
        self.label_20.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0430 \u0431\u043e\u0440\u0442\u0443", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"\u0412\u043b\u0430\u0436\u043d\u043e\u0441\u0442\u044c", None))
        self.humidity_on.setText(QCoreApplication.translate("MainWindow", u"N/A", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"\u0412\u0440\u0435\u043c\u044f", None))
        self.time.setText(QCoreApplication.translate("MainWindow", u"N/A", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"\u0422\u0435\u043c\u043f\u0435\u0440\u0430\u0442\u0443\u0440\u0430", None))
        self.temp_out.setText(QCoreApplication.translate("MainWindow", u"N/A", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"\u0417\u0430 \u0431\u043e\u0440\u0442\u043e\u043c", None))
    # retranslateUi

