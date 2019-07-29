# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui.ui'
#
# Created by: PyQt5 UI code generator 5.12
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 300)
        self.nooc = QtWidgets.QSpinBox(Dialog)
        self.nooc.setGeometry(QtCore.QRect(220, 10, 161, 31))
        self.nooc.setMinimum(1)
        self.nooc.setMaximum(999999999)
        self.nooc.setObjectName("nooc")
        self.bondui = QtWidgets.QSlider(Dialog)
        self.bondui.setGeometry(QtCore.QRect(220, 60, 160, 22))
        self.bondui.setMinimum(1)
        self.bondui.setMaximum(3)
        self.bondui.setPageStep(1)
        self.bondui.setOrientation(QtCore.Qt.Horizontal)
        self.bondui.setTickPosition(QtWidgets.QSlider.TicksBothSides)
        self.bondui.setTickInterval(1)
        self.bondui.setObjectName("bondui")
        self.output = QtWidgets.QTextEdit(Dialog)
        self.output.setGeometry(QtCore.QRect(10, 90, 381, 141))
        self.output.setObjectName("output")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(220, 250, 75, 23))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(Dialog)
        self.pushButton_2.setGeometry(QtCore.QRect(300, 250, 75, 23))
        self.pushButton_2.setObjectName("pushButton_2")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "carboncompunds - by srevinsaju"))
        self.pushButton.setText(_translate("Dialog", "COMPUTE"))
        self.pushButton_2.setText(_translate("Dialog", "QUIT"))
