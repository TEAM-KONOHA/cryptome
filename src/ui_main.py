################################################################################
## Form generated from reading UI file 'maintnQeBK.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################
import os
import sys
from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
from PySide2.QtWidgets import QFileDialog
import re
import shutil

# import realtime_face_recognition
Root = os.getcwd()


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
        self.frame.setStyleSheet(
            u"QFrame{\n" "\n" "\n" "		background-color: rgb(56, 58, 89);	;\n" "}"
        )
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.input = QPushButton(self.frame)
        self.input.setObjectName(u"input")
        self.input.setGeometry(QRect(140, 240, 111, 61))
        self.input.setStyleSheet(
            u"background-color: rgb(255, 51,102);\n"
            "font:75 8pt Tahoma;\n"
            "color: rgb(0, 0, 0);"
        )
        self.input.clicked.connect(self.Input_data)
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(160, 10, 321, 171))
        self.label.setStyleSheet(u"color: rgb(254, 121, 199);")
        self.pushButton_2 = QPushButton(self.frame)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(360, 240, 111, 61))
        self.pushButton_2.setStyleSheet(
            u";background-color: rgb(255, 51,102);\n"
            'font: 75 8pt Tahoma "old";\n'
            "color: rgb(0,0,0);"
        )
        self.pushButton_2.clicked.connect(self.facial_recognition)

        self.horizontalLayout.addWidget(self.frame)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)

    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(
            QCoreApplication.translate("MainWindow", u"Cryptome", None)
        )
        self.input.setText(
            QCoreApplication.translate("MainWindow", u"Input \n" " Database", None)
        )
        self.label.setText(
            QCoreApplication.translate(
                "MainWindow",
                u'<html><head/><body><p><span style=" font-size:36pt; font-weight:600;">CRYPTOME</span></p></body></html>',
                None,
            )
        )
        self.pushButton_2.setText(
            QCoreApplication.translate("MainWindow", u"Testing", None)
        )

    # retranslateUi
    def Input_data(self):
        # file selector
        folder = str(
            QFileDialog.getOpenFileName(
                None, "Select Image", "c:\\", "Image files (*.jpg *.gif)"
            )
        )
        # to remove white spaces
        arr = list(folder.split(","))
        global fileloc
        local = arr[0]
        fileloc = local.replace("/", "\\")
        fileloc = fileloc.replace("'", "")
        # for i in range(num-1,0,-1):
        # 	if arr[0][i]=="/":
        # 		start=i
        # 		break
        # foldername=arr[0][start,num]
        # print(foldername)
        self.window = QMainWindow()
        self.ui2 = Ui_Form()
        self.ui2.setupUi(self.window)
        self.window.show()

    def facial_recognition(self):
        os.system("python.exe realtime_face_recognition.py")


class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(400, 300)
        self.pushButton = QPushButton(Form)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(70, 150, 75, 23))
        self.pushButton_2 = QPushButton(Form)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(240, 150, 75, 23))
        self.label = QLabel(Form)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(150, 20, 151, 41))
        self.textEdit = QTextEdit(Form)
        self.textEdit.setObjectName(u"textEdit")
        self.textEdit.setGeometry(QRect(110, 80, 171, 31))
        self.pushButton.clicked.connect(self.FolderCreation)
        self.pushButton_2.clicked.connect(Form.close)
        self.retranslateUi(Form)
        QMetaObject.connectSlotsByName(Form)

    def FolderCreation(self):
        mytext = self.textEdit.toPlainText()
        newface = Root + "\\images\\known_faces\\" + mytext
        os.mkdir(newface)
        obj = Ui_MainWindow()
        print(fileloc[1:])
        dest = shutil.copy(fileloc[1:], newface)

    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.pushButton.setText(QCoreApplication.translate("Form", u"Ok", None))
        self.pushButton_2.setText(QCoreApplication.translate("Form", u"Cancel", None))
        self.label.setText(QCoreApplication.translate("Form", u"Input Unique Id", None))

    # retranslateUi
