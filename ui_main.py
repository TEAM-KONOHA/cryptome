# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'maintnQeBK.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
from PySide2.QtWidgets import QFileDialog


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"Cryptome")
        MainWindow.resize(600, 380)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setStyleSheet(u"QFrame{\n"
"\n"
"\n"
"		background-color: rgb(56, 58, 89);	;\n"
"}")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.input = QPushButton(self.frame)
        self.input.setObjectName(u"input")
        self.input.setGeometry(QRect(140, 240, 111, 61))
        self.input.setStyleSheet(u"background-color: rgb(255, 51,102);\n"
"font: System 87 11pt \"\";\n"
"color: rgb(0, 0, 0);")
        self.input.clicked.connect(self.Input_data)
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(160, 10, 321, 171))
        self.label.setStyleSheet(u"color: rgb(254, 121, 199);")
        self.pushButton_2 = QPushButton(self.frame)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(360, 240, 111, 61))
        self.pushButton_2.setStyleSheet(u";background-color: rgb(255, 51,102);\n"
"font: System 87 11pt \"old\";\n"
"color: rgb(0, ,0,0);")
        self.horizontalLayout.addWidget(self.frame)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Cryptome", None))
        self.input.setText(QCoreApplication.translate("MainWindow", u"Input \n"
" Database", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:36pt; font-weight:600;\">CRYPTOME</span></p></body></html>", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"Testing", None))
    # retranslateUi
    def Input_data(self):
        folder = str(QFileDialog.getExistingDirectory(None, "Select Directory"))
