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
    QLabel, QMainWindow, QPushButton, QSizePolicy,
    QSpacerItem, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1493, 1031)
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
        self.frame_41 = QFrame(self.monitorR_2)
        self.frame_41.setObjectName(u"frame_41")
        self.frame_41.setEnabled(True)
        sizePolicy1 = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.Maximum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
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

        self.gridLayout_3.addWidget(self.frame_41, 3, 1, 1, 1)

        self.cpuframe = QFrame(self.monitorR_2)
        self.cpuframe.setObjectName(u"cpuframe")
        self.cpuframe.setEnabled(True)
        sizePolicy1.setHeightForWidth(self.cpuframe.sizePolicy().hasHeightForWidth())
        self.cpuframe.setSizePolicy(sizePolicy1)
        self.cpuframe.setFont(font)
        self.cpuframe.setStyleSheet(u"border-radius: 7px;\n"
"padding-top: 0px;")
        self.cpuframe.setFrameShape(QFrame.StyledPanel)
        self.cpuframe.setFrameShadow(QFrame.Raised)
        self.gridLayout_44 = QGridLayout(self.cpuframe)
        self.gridLayout_44.setObjectName(u"gridLayout_44")
        self.label_41 = QLabel(self.cpuframe)
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
        self.label_41.setWordWrap(True)

        self.gridLayout_44.addWidget(self.label_41, 5, 0, 1, 1)

        self.label_50 = QLabel(self.cpuframe)
        self.label_50.setObjectName(u"label_50")
        sizePolicy2.setHeightForWidth(self.label_50.sizePolicy().hasHeightForWidth())
        self.label_50.setSizePolicy(sizePolicy2)
        self.label_50.setFont(font1)
        self.label_50.setStyleSheet(u"")
        self.label_50.setAlignment(Qt.AlignCenter)
        self.label_50.setWordWrap(True)

        self.gridLayout_44.addWidget(self.label_50, 3, 0, 1, 1)

        self.cputempframe = QFrame(self.cpuframe)
        self.cputempframe.setObjectName(u"cputempframe")
        self.cputempframe.setFrameShape(QFrame.StyledPanel)
        self.cputempframe.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.cputempframe)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")

        self.gridLayout_44.addWidget(self.cputempframe, 4, 0, 1, 1)

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

        self.gridLayout_44.addWidget(self.cpuusageframe, 2, 0, 1, 1)


        self.gridLayout_3.addWidget(self.cpuframe, 2, 1, 1, 1)

        self.frame_21 = QFrame(self.monitorR_2)
        self.frame_21.setObjectName(u"frame_21")
        self.frame_21.setEnabled(True)
        sizePolicy3 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Maximum)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.frame_21.sizePolicy().hasHeightForWidth())
        self.frame_21.setSizePolicy(sizePolicy3)
        self.frame_21.setMinimumSize(QSize(150, 0))
        self.frame_21.setFont(font)
        self.frame_21.setStyleSheet(u"background-color: rgb(53, 53, 53);\n"
"border-radius: 7px;\n"
"padding: 0px;")
        self.frame_21.setFrameShape(QFrame.StyledPanel)
        self.frame_21.setFrameShadow(QFrame.Raised)
        self.gridLayout_23 = QGridLayout(self.frame_21)
        self.gridLayout_23.setObjectName(u"gridLayout_23")
        self.gridLayout_23.setContentsMargins(7, 7, 7, 7)
        self.pushButton = QPushButton(self.frame_21)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setFont(font1)
        self.pushButton.setStyleSheet(u"background-color: rgb(7, 145, 92);\n"
"border-radius: 2px;\n"
"padding: 3px;\n"
"font-size: 17px;")

        self.gridLayout_23.addWidget(self.pushButton, 2, 0, 1, 1)

        self.frame_9 = QFrame(self.frame_21)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setEnabled(True)
        sizePolicy1.setHeightForWidth(self.frame_9.sizePolicy().hasHeightForWidth())
        self.frame_9.setSizePolicy(sizePolicy1)
        self.frame_9.setFont(font)
        self.frame_9.setStyleSheet(u"background-color: rgb(53, 53, 53);\n"
"border-radius: 2px;\n"
"padding-top: 0px;")
        self.frame_9.setFrameShape(QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Raised)
        self.verticalLayout_14 = QVBoxLayout(self.frame_9)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.verticalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.label_16 = QLabel(self.frame_9)
        self.label_16.setObjectName(u"label_16")
        sizePolicy4 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.label_16.sizePolicy().hasHeightForWidth())
        self.label_16.setSizePolicy(sizePolicy4)
        font2 = QFont()
        font2.setBold(False)
        self.label_16.setFont(font2)
        self.label_16.setStyleSheet(u"font-size: 19px;")
        self.label_16.setAlignment(Qt.AlignCenter)

        self.verticalLayout_14.addWidget(self.label_16)

        self.net = QLabel(self.frame_9)
        self.net.setObjectName(u"net")
        sizePolicy4.setHeightForWidth(self.net.sizePolicy().hasHeightForWidth())
        self.net.setSizePolicy(sizePolicy4)
        self.net.setMinimumSize(QSize(100, 0))
        self.net.setFont(font)
        self.net.setStyleSheet(u"font-size: 16px;\n"
"background-color: rgb(255, 255, 255);\n"
"color: rgb(34, 34, 34);")
        self.net.setAlignment(Qt.AlignCenter)

        self.verticalLayout_14.addWidget(self.net)


        self.gridLayout_23.addWidget(self.frame_9, 0, 0, 1, 1)

        self.frame_14 = QFrame(self.frame_21)
        self.frame_14.setObjectName(u"frame_14")
        self.frame_14.setEnabled(True)
        sizePolicy3.setHeightForWidth(self.frame_14.sizePolicy().hasHeightForWidth())
        self.frame_14.setSizePolicy(sizePolicy3)
        self.frame_14.setFont(font)
        self.frame_14.setStyleSheet(u"background-color: rgb(53, 53, 53);\n"
"border-radius: 2px;\n"
"padding-top: 0px;")
        self.frame_14.setFrameShape(QFrame.StyledPanel)
        self.frame_14.setFrameShadow(QFrame.Raised)
        self.verticalLayout_15 = QVBoxLayout(self.frame_14)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.verticalLayout_15.setContentsMargins(0, 0, 0, 0)
        self.label_17 = QLabel(self.frame_14)
        self.label_17.setObjectName(u"label_17")
        sizePolicy4.setHeightForWidth(self.label_17.sizePolicy().hasHeightForWidth())
        self.label_17.setSizePolicy(sizePolicy4)
        self.label_17.setFont(font2)
        self.label_17.setStyleSheet(u"font-size: 19px;")
        self.label_17.setAlignment(Qt.AlignCenter)

        self.verticalLayout_15.addWidget(self.label_17)

        self.status = QLabel(self.frame_14)
        self.status.setObjectName(u"status")
        sizePolicy4.setHeightForWidth(self.status.sizePolicy().hasHeightForWidth())
        self.status.setSizePolicy(sizePolicy4)
        self.status.setMinimumSize(QSize(100, 0))
        self.status.setFont(font)
        self.status.setStyleSheet(u"font-size: 16px;\n"
"background-color: rgb(255, 255, 255);\n"
"color: rgb(34, 34, 34);")
        self.status.setAlignment(Qt.AlignCenter)

        self.verticalLayout_15.addWidget(self.status)


        self.gridLayout_23.addWidget(self.frame_14, 1, 0, 1, 1)


        self.gridLayout_3.addWidget(self.frame_21, 0, 1, 1, 1)


        self.horizontalLayout.addWidget(self.monitorR_2)

        self.frame_3 = QFrame(self.centralwidget)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setEnabled(True)
        sizePolicy5 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.frame_3.sizePolicy().hasHeightForWidth())
        self.frame_3.setSizePolicy(sizePolicy5)
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_3)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 5, 0, 0)
        self.frame = QFrame(self.frame_3)
        self.frame.setObjectName(u"frame")
        sizePolicy5.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy5)
        self.frame.setMinimumSize(QSize(0, 0))
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.frame_2 = QFrame(self.frame)
        self.frame_2.setObjectName(u"frame_2")
        sizePolicy6 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy6.setHorizontalStretch(0)
        sizePolicy6.setVerticalStretch(0)
        sizePolicy6.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy6)
        self.frame_2.setMinimumSize(QSize(980, 560))
        self.frame_2.setMaximumSize(QSize(980, 560))
        self.frame_2.setAutoFillBackground(False)
        self.frame_2.setStyleSheet(u"background-color: rgb(53, 53, 53);\n"
"border-radius: 7px;\n"
"padding-top: 0px;")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.frame_2)
        self.label.setObjectName(u"label")
        sizePolicy7 = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.MinimumExpanding)
        sizePolicy7.setHorizontalStretch(0)
        sizePolicy7.setVerticalStretch(0)
        sizePolicy7.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy7)
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
        sizePolicy6.setHeightForWidth(self.RTframe.sizePolicy().hasHeightForWidth())
        self.RTframe.setSizePolicy(sizePolicy6)
        self.RTframe.setMinimumSize(QSize(0, 0))
        self.RTframe.setFrameShape(QFrame.StyledPanel)
        self.RTframe.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.RTframe)
        self.horizontalLayout_2.setSpacing(10)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame_13 = QFrame(self.RTframe)
        self.frame_13.setObjectName(u"frame_13")
        sizePolicy5.setHeightForWidth(self.frame_13.sizePolicy().hasHeightForWidth())
        self.frame_13.setSizePolicy(sizePolicy5)
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
        self.cpu_5 = QLabel(self.rollframe)
        self.cpu_5.setObjectName(u"cpu_5")
        sizePolicy2.setHeightForWidth(self.cpu_5.sizePolicy().hasHeightForWidth())
        self.cpu_5.setSizePolicy(sizePolicy2)
        self.cpu_5.setFont(font1)
        self.cpu_5.setStyleSheet(u"\n"
"border-radius: 7px;\n"
"padding-top: 0px;")
        self.cpu_5.setAlignment(Qt.AlignCenter)

        self.verticalLayout_5.addWidget(self.cpu_5)


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
        self.cpu_3 = QLabel(self.diffframe)
        self.cpu_3.setObjectName(u"cpu_3")
        sizePolicy2.setHeightForWidth(self.cpu_3.sizePolicy().hasHeightForWidth())
        self.cpu_3.setSizePolicy(sizePolicy2)
        self.cpu_3.setFont(font1)
        self.cpu_3.setStyleSheet(u"\n"
"border-radius: 7px;\n"
"padding-top: 0px;")
        self.cpu_3.setAlignment(Qt.AlignCenter)

        self.verticalLayout_4.addWidget(self.cpu_3)


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
        self.monitorR.setMinimumSize(QSize(200, 0))
        self.monitorR.setMaximumSize(QSize(250, 16777215))
        self.monitorR.setFont(font)
        self.monitorR.setFrameShape(QFrame.StyledPanel)
        self.monitorR.setFrameShadow(QFrame.Raised)
        self.monitorR.setMidLineWidth(0)
        self.gridLayout_2 = QGridLayout(self.monitorR)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(-1, 3, -1, 3)
        self.frame_8 = QFrame(self.monitorR)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setEnabled(True)
        sizePolicy3.setHeightForWidth(self.frame_8.sizePolicy().hasHeightForWidth())
        self.frame_8.setSizePolicy(sizePolicy3)
        self.frame_8.setMinimumSize(QSize(150, 0))
        self.frame_8.setFont(font)
        self.frame_8.setStyleSheet(u"background-color: rgb(53, 53, 53);\n"
"border-radius: 7px;\n"
"padding: 0px;")
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.gridLayout_15 = QGridLayout(self.frame_8)
        self.gridLayout_15.setObjectName(u"gridLayout_15")
        self.gridLayout_15.setContentsMargins(0, 0, 0, -1)
        self.frame_7 = QFrame(self.frame_8)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setEnabled(True)
        sizePolicy1.setHeightForWidth(self.frame_7.sizePolicy().hasHeightForWidth())
        self.frame_7.setSizePolicy(sizePolicy1)
        self.frame_7.setFont(font)
        self.frame_7.setStyleSheet(u"background-color: rgb(53, 53, 53);\n"
"border-radius: 2px;\n"
"padding-top: 0px;")
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.verticalLayout_12 = QVBoxLayout(self.frame_7)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.label_8 = QLabel(self.frame_7)
        self.label_8.setObjectName(u"label_8")
        sizePolicy8 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy8.setHorizontalStretch(0)
        sizePolicy8.setVerticalStretch(0)
        sizePolicy8.setHeightForWidth(self.label_8.sizePolicy().hasHeightForWidth())
        self.label_8.setSizePolicy(sizePolicy8)
        self.label_8.setFont(font2)
        self.label_8.setStyleSheet(u"font-size: 19px;")
        self.label_8.setAlignment(Qt.AlignCenter)

        self.verticalLayout_12.addWidget(self.label_8)

        self.speed = QLabel(self.frame_7)
        self.speed.setObjectName(u"speed")
        sizePolicy9 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Preferred)
        sizePolicy9.setHorizontalStretch(0)
        sizePolicy9.setVerticalStretch(0)
        sizePolicy9.setHeightForWidth(self.speed.sizePolicy().hasHeightForWidth())
        self.speed.setSizePolicy(sizePolicy9)
        self.speed.setMinimumSize(QSize(100, 0))
        self.speed.setFont(font)
        self.speed.setStyleSheet(u"font-size: 16px;")
        self.speed.setAlignment(Qt.AlignCenter)

        self.verticalLayout_12.addWidget(self.speed)


        self.gridLayout_15.addWidget(self.frame_7, 5, 0, 1, 1)

        self.frame_20 = QFrame(self.frame_8)
        self.frame_20.setObjectName(u"frame_20")
        self.frame_20.setEnabled(True)
        sizePolicy1.setHeightForWidth(self.frame_20.sizePolicy().hasHeightForWidth())
        self.frame_20.setSizePolicy(sizePolicy1)
        self.frame_20.setFont(font)
        self.frame_20.setStyleSheet(u"background-color: rgb(53, 53, 53);\n"
"border-radius: 2px;\n"
"padding-top: 0px;")
        self.frame_20.setFrameShape(QFrame.StyledPanel)
        self.frame_20.setFrameShadow(QFrame.Raised)
        self.gridLayout_22 = QGridLayout(self.frame_20)
        self.gridLayout_22.setObjectName(u"gridLayout_22")
        self.time = QLabel(self.frame_20)
        self.time.setObjectName(u"time")
        sizePolicy10 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Preferred)
        sizePolicy10.setHorizontalStretch(0)
        sizePolicy10.setVerticalStretch(0)
        sizePolicy10.setHeightForWidth(self.time.sizePolicy().hasHeightForWidth())
        self.time.setSizePolicy(sizePolicy10)
        self.time.setMinimumSize(QSize(100, 0))
        self.time.setFont(font)
        self.time.setStyleSheet(u"font-size: 16px;")
        self.time.setAlignment(Qt.AlignCenter)

        self.gridLayout_22.addWidget(self.time, 0, 0, 1, 1)


        self.gridLayout_15.addWidget(self.frame_20, 2, 0, 1, 1)

        self.frame_17 = QFrame(self.frame_8)
        self.frame_17.setObjectName(u"frame_17")
        self.frame_17.setEnabled(True)
        sizePolicy1.setHeightForWidth(self.frame_17.sizePolicy().hasHeightForWidth())
        self.frame_17.setSizePolicy(sizePolicy1)
        self.frame_17.setFont(font)
        self.frame_17.setStyleSheet(u"background-color: rgb(45, 45, 45);\n"
"border-radius: 2px;\n"
"padding-top: 0px;")
        self.frame_17.setFrameShape(QFrame.StyledPanel)
        self.frame_17.setFrameShadow(QFrame.Raised)
        self.gridLayout_28 = QGridLayout(self.frame_17)
        self.gridLayout_28.setObjectName(u"gridLayout_28")
        self.lat = QLabel(self.frame_17)
        self.lat.setObjectName(u"lat")
        sizePolicy10.setHeightForWidth(self.lat.sizePolicy().hasHeightForWidth())
        self.lat.setSizePolicy(sizePolicy10)
        self.lat.setMinimumSize(QSize(100, 0))
        self.lat.setFont(font)
        self.lat.setAlignment(Qt.AlignCenter)

        self.gridLayout_28.addWidget(self.lat, 0, 0, 1, 1)

        self.lon = QLabel(self.frame_17)
        self.lon.setObjectName(u"lon")
        sizePolicy10.setHeightForWidth(self.lon.sizePolicy().hasHeightForWidth())
        self.lon.setSizePolicy(sizePolicy10)
        self.lon.setMinimumSize(QSize(100, 0))
        self.lon.setFont(font)
        self.lon.setAlignment(Qt.AlignCenter)

        self.gridLayout_28.addWidget(self.lon, 1, 0, 1, 1)


        self.gridLayout_15.addWidget(self.frame_17, 1, 0, 1, 1)

        self.frame_6 = QFrame(self.frame_8)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setEnabled(True)
        sizePolicy1.setHeightForWidth(self.frame_6.sizePolicy().hasHeightForWidth())
        self.frame_6.setSizePolicy(sizePolicy1)
        self.frame_6.setFont(font)
        self.frame_6.setStyleSheet(u"background-color: rgb(53, 53, 53);\n"
"border-radius: 2px;\n"
"padding-top: 0px;")
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.verticalLayout_11 = QVBoxLayout(self.frame_6)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.label_7 = QLabel(self.frame_6)
        self.label_7.setObjectName(u"label_7")
        sizePolicy8.setHeightForWidth(self.label_7.sizePolicy().hasHeightForWidth())
        self.label_7.setSizePolicy(sizePolicy8)
        self.label_7.setFont(font2)
        self.label_7.setStyleSheet(u"font-size: 19px;")
        self.label_7.setAlignment(Qt.AlignCenter)

        self.verticalLayout_11.addWidget(self.label_7)

        self.sats = QLabel(self.frame_6)
        self.sats.setObjectName(u"sats")
        sizePolicy9.setHeightForWidth(self.sats.sizePolicy().hasHeightForWidth())
        self.sats.setSizePolicy(sizePolicy9)
        self.sats.setMinimumSize(QSize(100, 0))
        self.sats.setFont(font)
        self.sats.setStyleSheet(u"font-size: 16px;")
        self.sats.setAlignment(Qt.AlignCenter)

        self.verticalLayout_11.addWidget(self.sats)


        self.gridLayout_15.addWidget(self.frame_6, 4, 0, 1, 1)

        self.label_12 = QLabel(self.frame_8)
        self.label_12.setObjectName(u"label_12")
        sizePolicy2.setHeightForWidth(self.label_12.sizePolicy().hasHeightForWidth())
        self.label_12.setSizePolicy(sizePolicy2)
        self.label_12.setFont(font1)
        self.label_12.setStyleSheet(u"color: #FFF;\n"
"background-color: rgb(45, 45, 45);\n"
"border-radius: 7px;\n"
"padding-top: 5px;\n"
"padding-bottom: 4px;")
        self.label_12.setAlignment(Qt.AlignCenter)

        self.gridLayout_15.addWidget(self.label_12, 0, 0, 1, 1)


        self.gridLayout_2.addWidget(self.frame_8, 9, 1, 1, 1)

        self.frame_18 = QFrame(self.monitorR)
        self.frame_18.setObjectName(u"frame_18")
        self.frame_18.setEnabled(True)
        sizePolicy3.setHeightForWidth(self.frame_18.sizePolicy().hasHeightForWidth())
        self.frame_18.setSizePolicy(sizePolicy3)
        self.frame_18.setMinimumSize(QSize(150, 0))
        self.frame_18.setFont(font)
        self.frame_18.setStyleSheet(u"background-color: rgb(53, 53, 53);\n"
"border-radius: 7px;\n"
"padding: 0px;")
        self.frame_18.setFrameShape(QFrame.StyledPanel)
        self.frame_18.setFrameShadow(QFrame.Raised)
        self.gridLayout_20 = QGridLayout(self.frame_18)
        self.gridLayout_20.setObjectName(u"gridLayout_20")
        self.gridLayout_20.setContentsMargins(0, 0, 0, -1)
        self.frame_11 = QFrame(self.frame_18)
        self.frame_11.setObjectName(u"frame_11")
        self.frame_11.setEnabled(True)
        sizePolicy1.setHeightForWidth(self.frame_11.sizePolicy().hasHeightForWidth())
        self.frame_11.setSizePolicy(sizePolicy1)
        self.frame_11.setFont(font)
        self.frame_11.setStyleSheet(u"background-color: rgb(53, 53, 53);\n"
"border-radius: 2px;\n"
"padding-top: 0px;")
        self.frame_11.setFrameShape(QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frame_11)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_10 = QLabel(self.frame_11)
        self.label_10.setObjectName(u"label_10")
        sizePolicy8.setHeightForWidth(self.label_10.sizePolicy().hasHeightForWidth())
        self.label_10.setSizePolicy(sizePolicy8)
        self.label_10.setFont(font2)
        self.label_10.setStyleSheet(u"font-size: 19px;")
        self.label_10.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.label_10)

        self.depth_target = QLabel(self.frame_11)
        self.depth_target.setObjectName(u"depth_target")
        sizePolicy9.setHeightForWidth(self.depth_target.sizePolicy().hasHeightForWidth())
        self.depth_target.setSizePolicy(sizePolicy9)
        self.depth_target.setMinimumSize(QSize(100, 0))
        self.depth_target.setFont(font)
        self.depth_target.setStyleSheet(u"font-size: 16px;")
        self.depth_target.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.depth_target)


        self.gridLayout_20.addWidget(self.frame_11, 1, 0, 1, 1)

        self.frame_10 = QFrame(self.frame_18)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setEnabled(True)
        sizePolicy1.setHeightForWidth(self.frame_10.sizePolicy().hasHeightForWidth())
        self.frame_10.setSizePolicy(sizePolicy1)
        self.frame_10.setFont(font)
        self.frame_10.setStyleSheet(u"background-color: rgb(53, 53, 53);\n"
"border-radius: 2px;\n"
"padding-top: 0px;")
        self.frame_10.setFrameShape(QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.frame_10)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.label_9 = QLabel(self.frame_10)
        self.label_9.setObjectName(u"label_9")
        sizePolicy8.setHeightForWidth(self.label_9.sizePolicy().hasHeightForWidth())
        self.label_9.setSizePolicy(sizePolicy8)
        self.label_9.setFont(font2)
        self.label_9.setStyleSheet(u"font-size: 19px;")
        self.label_9.setAlignment(Qt.AlignCenter)

        self.verticalLayout_6.addWidget(self.label_9)

        self.depth = QLabel(self.frame_10)
        self.depth.setObjectName(u"depth")
        sizePolicy9.setHeightForWidth(self.depth.sizePolicy().hasHeightForWidth())
        self.depth.setSizePolicy(sizePolicy9)
        self.depth.setMinimumSize(QSize(100, 0))
        self.depth.setFont(font)
        self.depth.setStyleSheet(u"font-size: 16px;")
        self.depth.setAlignment(Qt.AlignCenter)

        self.verticalLayout_6.addWidget(self.depth)


        self.gridLayout_20.addWidget(self.frame_10, 2, 0, 1, 1)

        self.label_13 = QLabel(self.frame_18)
        self.label_13.setObjectName(u"label_13")
        sizePolicy2.setHeightForWidth(self.label_13.sizePolicy().hasHeightForWidth())
        self.label_13.setSizePolicy(sizePolicy2)
        self.label_13.setFont(font1)
        self.label_13.setStyleSheet(u"color: #FFF;\n"
"background-color: rgb(45, 45, 45);\n"
"border-radius: 7px;\n"
"padding-top: 5px;\n"
"padding-bottom: 4px;")
        self.label_13.setAlignment(Qt.AlignCenter)

        self.gridLayout_20.addWidget(self.label_13, 0, 0, 1, 1)


        self.gridLayout_2.addWidget(self.frame_18, 1, 1, 1, 1)

        self.frame_19 = QFrame(self.monitorR)
        self.frame_19.setObjectName(u"frame_19")
        self.frame_19.setEnabled(True)
        sizePolicy3.setHeightForWidth(self.frame_19.sizePolicy().hasHeightForWidth())
        self.frame_19.setSizePolicy(sizePolicy3)
        self.frame_19.setMinimumSize(QSize(150, 0))
        self.frame_19.setFont(font)
        self.frame_19.setStyleSheet(u"background-color: rgb(53, 53, 53);\n"
"border-radius: 7px;\n"
"padding: 0px;")
        self.frame_19.setFrameShape(QFrame.StyledPanel)
        self.frame_19.setFrameShadow(QFrame.Raised)
        self.gridLayout_21 = QGridLayout(self.frame_19)
        self.gridLayout_21.setObjectName(u"gridLayout_21")
        self.gridLayout_21.setContentsMargins(0, 0, 0, -1)
        self.frame_22 = QFrame(self.frame_19)
        self.frame_22.setObjectName(u"frame_22")
        self.frame_22.setEnabled(True)
        sizePolicy3.setHeightForWidth(self.frame_22.sizePolicy().hasHeightForWidth())
        self.frame_22.setSizePolicy(sizePolicy3)
        self.frame_22.setFont(font)
        self.frame_22.setStyleSheet(u"")
        self.frame_22.setFrameShape(QFrame.StyledPanel)
        self.frame_22.setFrameShadow(QFrame.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.frame_22)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.label_21 = QLabel(self.frame_22)
        self.label_21.setObjectName(u"label_21")
        sizePolicy8.setHeightForWidth(self.label_21.sizePolicy().hasHeightForWidth())
        self.label_21.setSizePolicy(sizePolicy8)
        self.label_21.setFont(font2)
        self.label_21.setStyleSheet(u"font-size: 19px;")
        self.label_21.setAlignment(Qt.AlignCenter)

        self.verticalLayout_8.addWidget(self.label_21)

        self.temp_on = QLabel(self.frame_22)
        self.temp_on.setObjectName(u"temp_on")
        sizePolicy9.setHeightForWidth(self.temp_on.sizePolicy().hasHeightForWidth())
        self.temp_on.setSizePolicy(sizePolicy9)
        self.temp_on.setMinimumSize(QSize(100, 0))
        self.temp_on.setFont(font)
        self.temp_on.setStyleSheet(u"font-size: 16px;")
        self.temp_on.setAlignment(Qt.AlignCenter)

        self.verticalLayout_8.addWidget(self.temp_on)


        self.gridLayout_21.addWidget(self.frame_22, 2, 0, 1, 1)

        self.frame_12 = QFrame(self.frame_19)
        self.frame_12.setObjectName(u"frame_12")
        self.frame_12.setEnabled(True)
        sizePolicy1.setHeightForWidth(self.frame_12.sizePolicy().hasHeightForWidth())
        self.frame_12.setSizePolicy(sizePolicy1)
        self.frame_12.setFont(font)
        self.frame_12.setStyleSheet(u"")
        self.frame_12.setFrameShape(QFrame.StyledPanel)
        self.frame_12.setFrameShadow(QFrame.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.frame_12)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.label_11 = QLabel(self.frame_12)
        self.label_11.setObjectName(u"label_11")
        sizePolicy8.setHeightForWidth(self.label_11.sizePolicy().hasHeightForWidth())
        self.label_11.setSizePolicy(sizePolicy8)
        self.label_11.setFont(font2)
        self.label_11.setStyleSheet(u"font-size: 19px;")
        self.label_11.setAlignment(Qt.AlignCenter)

        self.verticalLayout_9.addWidget(self.label_11)

        self.humidity_on = QLabel(self.frame_12)
        self.humidity_on.setObjectName(u"humidity_on")
        sizePolicy9.setHeightForWidth(self.humidity_on.sizePolicy().hasHeightForWidth())
        self.humidity_on.setSizePolicy(sizePolicy9)
        self.humidity_on.setMinimumSize(QSize(100, 0))
        self.humidity_on.setFont(font)
        self.humidity_on.setStyleSheet(u"font-size: 16px;")
        self.humidity_on.setAlignment(Qt.AlignCenter)

        self.verticalLayout_9.addWidget(self.humidity_on)


        self.gridLayout_21.addWidget(self.frame_12, 0, 0, 1, 1)

        self.frame_25 = QFrame(self.frame_19)
        self.frame_25.setObjectName(u"frame_25")
        self.frame_25.setEnabled(True)
        sizePolicy1.setHeightForWidth(self.frame_25.sizePolicy().hasHeightForWidth())
        self.frame_25.setSizePolicy(sizePolicy1)
        self.frame_25.setFont(font)
        self.frame_25.setStyleSheet(u"")
        self.frame_25.setFrameShape(QFrame.StyledPanel)
        self.frame_25.setFrameShadow(QFrame.Raised)
        self.verticalLayout_10 = QVBoxLayout(self.frame_25)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.label_14 = QLabel(self.frame_25)
        self.label_14.setObjectName(u"label_14")
        sizePolicy8.setHeightForWidth(self.label_14.sizePolicy().hasHeightForWidth())
        self.label_14.setSizePolicy(sizePolicy8)
        self.label_14.setFont(font2)
        self.label_14.setStyleSheet(u"font-size: 19px;")
        self.label_14.setAlignment(Qt.AlignCenter)
        self.label_14.setWordWrap(True)

        self.verticalLayout_10.addWidget(self.label_14)

        self.temp_out = QLabel(self.frame_25)
        self.temp_out.setObjectName(u"temp_out")
        sizePolicy9.setHeightForWidth(self.temp_out.sizePolicy().hasHeightForWidth())
        self.temp_out.setSizePolicy(sizePolicy9)
        self.temp_out.setMinimumSize(QSize(100, 0))
        self.temp_out.setFont(font)
        self.temp_out.setStyleSheet(u"font-size: 16px;")
        self.temp_out.setAlignment(Qt.AlignCenter)

        self.verticalLayout_10.addWidget(self.temp_out)


        self.gridLayout_21.addWidget(self.frame_25, 3, 0, 1, 1)

        self.frame_23 = QFrame(self.frame_19)
        self.frame_23.setObjectName(u"frame_23")
        self.frame_23.setEnabled(True)
        sizePolicy1.setHeightForWidth(self.frame_23.sizePolicy().hasHeightForWidth())
        self.frame_23.setSizePolicy(sizePolicy1)
        self.frame_23.setFont(font)
        self.frame_23.setStyleSheet(u"")
        self.frame_23.setFrameShape(QFrame.StyledPanel)
        self.frame_23.setFrameShadow(QFrame.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.frame_23)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.label_22 = QLabel(self.frame_23)
        self.label_22.setObjectName(u"label_22")
        sizePolicy8.setHeightForWidth(self.label_22.sizePolicy().hasHeightForWidth())
        self.label_22.setSizePolicy(sizePolicy8)
        self.label_22.setFont(font2)
        self.label_22.setStyleSheet(u"font-size: 19px;")
        self.label_22.setAlignment(Qt.AlignCenter)

        self.verticalLayout_7.addWidget(self.label_22)

        self.pressure_on = QLabel(self.frame_23)
        self.pressure_on.setObjectName(u"pressure_on")
        sizePolicy9.setHeightForWidth(self.pressure_on.sizePolicy().hasHeightForWidth())
        self.pressure_on.setSizePolicy(sizePolicy9)
        self.pressure_on.setMinimumSize(QSize(100, 0))
        self.pressure_on.setFont(font)
        self.pressure_on.setStyleSheet(u"font-size: 16px;")
        self.pressure_on.setAlignment(Qt.AlignCenter)

        self.verticalLayout_7.addWidget(self.pressure_on)


        self.gridLayout_21.addWidget(self.frame_23, 1, 0, 1, 1)


        self.gridLayout_2.addWidget(self.frame_19, 10, 1, 1, 1)


        self.horizontalLayout.addWidget(self.monitorR)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label_41.setText(QCoreApplication.translate("MainWindow", u"\u0422\u0435\u043c\u043f\u0435\u0440\u0430\u0442\u0443\u0440\u0430 CPU", None))
        self.label_50.setText(QCoreApplication.translate("MainWindow", u" \u0417\u0430\u0433\u0440\u0443\u0437\u043a\u0430 CPU", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"\u041f\u043e\u0434\u043a\u043b\u044e\u0447\u0438\u0442\u044c\u0441\u044f", None))
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"\u0421\u0435\u0442\u044c", None))
        self.net.setText(QCoreApplication.translate("MainWindow", u"N/A", None))
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"\u0421\u0442\u0430\u0442\u0443\u0441", None))
        self.status.setText(QCoreApplication.translate("MainWindow", u"N/A", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0442\u043a\u043b\u044e\u0447\u0435\u043d\u043e...", None))
        self.cpu_5.setText(QCoreApplication.translate("MainWindow", u"\u041a\u0440\u0435\u043d", None))
        self.cpu_3.setText(QCoreApplication.translate("MainWindow", u"\u0414\u0438\u0444\u0444\u0435\u0440\u0435\u043d\u0442", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"\u0421\u043a\u043e\u0440\u043e\u0441\u0442\u044c", None))
        self.speed.setText(QCoreApplication.translate("MainWindow", u"N/A", None))
        self.time.setText(QCoreApplication.translate("MainWindow", u"N/A", None))
        self.lat.setText(QCoreApplication.translate("MainWindow", u"N/A", None))
        self.lon.setText(QCoreApplication.translate("MainWindow", u"N/A", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"\u0421\u043f\u0443\u0442\u043d\u0438\u043a\u0438", None))
        self.sats.setText(QCoreApplication.translate("MainWindow", u"N/A", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"GPS", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"\u0426\u0435\u043b\u044c", None))
        self.depth_target.setText(QCoreApplication.translate("MainWindow", u"N/A", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"\u0422\u0435\u043a\u0443\u0449\u0430\u044f", None))
        self.depth.setText(QCoreApplication.translate("MainWindow", u"N/A", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"\u0413\u043b\u0443\u0431\u0438\u043d\u0430", None))
        self.label_21.setText(QCoreApplication.translate("MainWindow", u"\u0422\u0435\u043c\u043f\u0435\u0440\u0430\u0442\u0443\u0440\u0430", None))
        self.temp_on.setText(QCoreApplication.translate("MainWindow", u"N/A", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"\u0412\u043b\u0430\u0436\u043d\u043e\u0441\u0442\u044c", None))
        self.humidity_on.setText(QCoreApplication.translate("MainWindow", u"N/A", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"\u0422\u0435\u043c\u043f\u0435\u0440\u0430\u0442\u0443\u0440\u0430 \u0441\u043d\u0430\u0440\u0443\u0436\u0438", None))
        self.temp_out.setText(QCoreApplication.translate("MainWindow", u"N/A", None))
        self.label_22.setText(QCoreApplication.translate("MainWindow", u"\u0414\u0430\u0432\u043b\u0435\u043d\u0438\u0435", None))
        self.pressure_on.setText(QCoreApplication.translate("MainWindow", u"N/A", None))
    # retranslateUi

