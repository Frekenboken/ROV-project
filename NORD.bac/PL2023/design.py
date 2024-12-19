# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'design.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QDial, QFrame,
    QGridLayout, QLCDNumber, QLabel, QMainWindow,
    QProgressBar, QPushButton, QRadioButton, QSizePolicy,
    QSlider, QTabWidget, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1357, 862)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout_3 = QGridLayout(self.centralwidget)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.frame_2 = QFrame(self.centralwidget)
        self.frame_2.setObjectName(u"frame_2")
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy)
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.gridLayout_4 = QGridLayout(self.frame_2)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.name = QLabel(self.frame_2)
        self.name.setObjectName(u"name")
        sizePolicy1 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.name.sizePolicy().hasHeightForWidth())
        self.name.setSizePolicy(sizePolicy1)
        self.name.setMinimumSize(QSize(640, 480))
        font = QFont()
        font.setPointSize(17)
        self.name.setFont(font)
        self.name.setAlignment(Qt.AlignCenter)

        self.gridLayout_4.addWidget(self.name, 0, 0, 1, 1)


        self.gridLayout_3.addWidget(self.frame_2, 0, 0, 1, 1)

        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tab_3 = QWidget()
        self.tab_3.setObjectName(u"tab_3")
        self.gridLayout_5 = QGridLayout(self.tab_3)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.frame_3 = QFrame(self.tab_3)
        self.frame_3.setObjectName(u"frame_3")
        sizePolicy2 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Minimum)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.frame_3.sizePolicy().hasHeightForWidth())
        self.frame_3.setSizePolicy(sizePolicy2)
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.gridLayout_2 = QGridLayout(self.frame_3)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.frame_7 = QFrame(self.frame_3)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setEnabled(True)
        sizePolicy3 = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.Maximum)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.frame_7.sizePolicy().hasHeightForWidth())
        self.frame_7.setSizePolicy(sizePolicy3)
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.gridLayout_11 = QGridLayout(self.frame_7)
        self.gridLayout_11.setObjectName(u"gridLayout_11")
        self.tempn = QLCDNumber(self.frame_7)
        self.tempn.setObjectName(u"tempn")
        sizePolicy1.setHeightForWidth(self.tempn.sizePolicy().hasHeightForWidth())
        self.tempn.setSizePolicy(sizePolicy1)

        self.gridLayout_11.addWidget(self.tempn, 0, 3, 1, 1)

        self.tempp = QProgressBar(self.frame_7)
        self.tempp.setObjectName(u"tempp")
        self.tempp.setValue(24)
        self.tempp.setTextVisible(False)

        self.gridLayout_11.addWidget(self.tempp, 0, 1, 1, 1)

        self.label_8 = QLabel(self.frame_7)
        self.label_8.setObjectName(u"label_8")
        sizePolicy4 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.label_8.sizePolicy().hasHeightForWidth())
        self.label_8.setSizePolicy(sizePolicy4)
        font1 = QFont()
        font1.setFamilies([u"Segoe UI"])
        font1.setBold(False)
        self.label_8.setFont(font1)

        self.gridLayout_11.addWidget(self.label_8, 0, 0, 1, 1)


        self.gridLayout_2.addWidget(self.frame_7, 1, 1, 1, 1)

        self.frame_6 = QFrame(self.frame_3)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setEnabled(True)
        sizePolicy3.setHeightForWidth(self.frame_6.sizePolicy().hasHeightForWidth())
        self.frame_6.setSizePolicy(sizePolicy3)
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.gridLayout_10 = QGridLayout(self.frame_6)
        self.gridLayout_10.setObjectName(u"gridLayout_10")
        self.timen = QLCDNumber(self.frame_6)
        self.timen.setObjectName(u"timen")
        sizePolicy1.setHeightForWidth(self.timen.sizePolicy().hasHeightForWidth())
        self.timen.setSizePolicy(sizePolicy1)

        self.gridLayout_10.addWidget(self.timen, 0, 3, 1, 1)

        self.timep = QProgressBar(self.frame_6)
        self.timep.setObjectName(u"timep")
        self.timep.setValue(24)
        self.timep.setTextVisible(False)

        self.gridLayout_10.addWidget(self.timep, 0, 1, 1, 1)

        self.label_7 = QLabel(self.frame_6)
        self.label_7.setObjectName(u"label_7")
        sizePolicy4.setHeightForWidth(self.label_7.sizePolicy().hasHeightForWidth())
        self.label_7.setSizePolicy(sizePolicy4)
        self.label_7.setFont(font1)

        self.gridLayout_10.addWidget(self.label_7, 0, 0, 1, 1)


        self.gridLayout_2.addWidget(self.frame_6, 2, 1, 1, 1)

        self.frame = QFrame(self.frame_3)
        self.frame.setObjectName(u"frame")
        self.frame.setEnabled(True)
        sizePolicy3.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy3)
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.gridLayout = QGridLayout(self.frame)
        self.gridLayout.setObjectName(u"gridLayout")
        self.depthn = QLCDNumber(self.frame)
        self.depthn.setObjectName(u"depthn")
        sizePolicy1.setHeightForWidth(self.depthn.sizePolicy().hasHeightForWidth())
        self.depthn.setSizePolicy(sizePolicy1)

        self.gridLayout.addWidget(self.depthn, 0, 3, 1, 1)

        self.depthp = QProgressBar(self.frame)
        self.depthp.setObjectName(u"depthp")
        self.depthp.setValue(24)
        self.depthp.setTextVisible(False)

        self.gridLayout.addWidget(self.depthp, 0, 1, 1, 1)

        self.label_2 = QLabel(self.frame)
        self.label_2.setObjectName(u"label_2")
        sizePolicy4.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy4)
        self.label_2.setFont(font1)

        self.gridLayout.addWidget(self.label_2, 0, 0, 1, 1)


        self.gridLayout_2.addWidget(self.frame, 0, 1, 1, 1)


        self.gridLayout_5.addWidget(self.frame_3, 0, 1, 1, 1)

        self.frame_8 = QFrame(self.tab_3)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.slider = QSlider(self.frame_8)
        self.slider.setObjectName(u"slider")
        self.slider.setGeometry(QRect(20, 20, 31, 241))
        self.slider.setOrientation(Qt.Vertical)
        self.btn_w = QPushButton(self.frame_8)
        self.btn_w.setObjectName(u"btn_w")
        self.btn_w.setGeometry(QRect(160, 60, 75, 24))
        self.btn_s = QPushButton(self.frame_8)
        self.btn_s.setObjectName(u"btn_s")
        self.btn_s.setGeometry(QRect(160, 90, 75, 24))
        self.btn_d = QPushButton(self.frame_8)
        self.btn_d.setObjectName(u"btn_d")
        self.btn_d.setGeometry(QRect(240, 90, 75, 24))
        self.btn_a = QPushButton(self.frame_8)
        self.btn_a.setObjectName(u"btn_a")
        self.btn_a.setGeometry(QRect(80, 90, 75, 24))
        self.rbtn = QRadioButton(self.frame_8)
        self.rbtn.setObjectName(u"rbtn")
        self.rbtn.setGeometry(QRect(130, 160, 89, 20))
        self.cbtn = QCheckBox(self.frame_8)
        self.cbtn.setObjectName(u"cbtn")
        self.cbtn.setGeometry(QRect(130, 220, 151, 20))
        self.dial = QDial(self.frame_8)
        self.dial.setObjectName(u"dial")
        self.dial.setGeometry(QRect(110, 320, 151, 141))

        self.gridLayout_5.addWidget(self.frame_8, 0, 0, 1, 1)

        self.tabWidget.addTab(self.tab_3, "")
        self.tab_4 = QWidget()
        self.tab_4.setObjectName(u"tab_4")
        self.tabWidget.addTab(self.tab_4, "")

        self.gridLayout_3.addWidget(self.tabWidget, 0, 1, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.name.setText(QCoreApplication.translate("MainWindow", u"Loading the camera...", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"\u0422\u0435\u043c\u043f\u0435\u0440\u0430\u0442\u0443\u0440\u0430", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"\u0412\u0440\u0435\u043c\u044f \u0440\u0430\u0431\u043e\u0442\u044b", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"\u0413\u043b\u0443\u0431\u0438\u043d\u0430", None))
        self.btn_w.setText(QCoreApplication.translate("MainWindow", u"W", None))
#if QT_CONFIG(shortcut)
        self.btn_w.setShortcut(QCoreApplication.translate("MainWindow", u"W", None))
#endif // QT_CONFIG(shortcut)
        self.btn_s.setText(QCoreApplication.translate("MainWindow", u"S", None))
#if QT_CONFIG(shortcut)
        self.btn_s.setShortcut(QCoreApplication.translate("MainWindow", u"S", None))
#endif // QT_CONFIG(shortcut)
        self.btn_d.setText(QCoreApplication.translate("MainWindow", u"D", None))
#if QT_CONFIG(shortcut)
        self.btn_d.setShortcut(QCoreApplication.translate("MainWindow", u"D", None))
#endif // QT_CONFIG(shortcut)
        self.btn_a.setText(QCoreApplication.translate("MainWindow", u"A", None))
#if QT_CONFIG(shortcut)
        self.btn_a.setShortcut(QCoreApplication.translate("MainWindow", u"A", None))
#endif // QT_CONFIG(shortcut)
        self.rbtn.setText(QCoreApplication.translate("MainWindow", u"\u0412\u044b\u043a\u043b", None))
        self.cbtn.setText(QCoreApplication.translate("MainWindow", u"0 \u043d\u0430 \u0442\u0435\u043c\u043f\u0435\u0440\u0430\u0442\u0443\u0440\u0435", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), QCoreApplication.translate("MainWindow", u"Indicators/\u041f\u043e\u043a\u0430\u0437\u0430\u0442\u0435\u043b\u0438", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), QCoreApplication.translate("MainWindow", u"Options/\u041d\u0430\u0441\u0442\u0440\u043e\u0439\u043a\u0438", None))
    # retranslateUi

