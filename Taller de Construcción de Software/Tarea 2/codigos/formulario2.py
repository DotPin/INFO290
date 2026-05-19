# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'formulario2.ui'
#
# Created: Mon Sep  5 23:09:39 2016
#      by: pyside-uic 0.2.15 running on PySide 1.2.1
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_formulario2(object):
    def setupUi(self, formulario2):
        formulario2.setObjectName("formulario2")
        formulario2.resize(288, 114)
        formulario2.setMinimumSize(QtCore.QSize(288, 114))
        formulario2.setMaximumSize(QtCore.QSize(288, 114))
        self.centralWidget = QtGui.QWidget(formulario2)
        self.centralWidget.setObjectName("centralWidget")
        self.label = QtGui.QLabel(self.centralWidget)
        self.label.setGeometry(QtCore.QRect(10, 20, 271, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setFrameShape(QtGui.QFrame.Box)
        self.label.setFrameShadow(QtGui.QFrame.Plain)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.add = QtGui.QLineEdit(self.centralWidget)
        self.add.setGeometry(QtCore.QRect(10, 70, 131, 23))
        self.add.setObjectName("add")
        self.ok = QtGui.QPushButton(self.centralWidget)
        self.ok.setGeometry(QtCore.QRect(150, 70, 51, 23))
        self.ok.setObjectName("ok")
        self.cancelar = QtGui.QPushButton(self.centralWidget)
        self.cancelar.setGeometry(QtCore.QRect(210, 70, 71, 23))
        self.cancelar.setObjectName("cancelar")
        formulario2.setCentralWidget(self.centralWidget)

        self.retranslateUi(formulario2)
        QtCore.QMetaObject.connectSlotsByName(formulario2)

    def retranslateUi(self, formulario2):
        formulario2.setWindowTitle(QtGui.QApplication.translate("formulario2", "formulario2", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("formulario2", "Ingrese Categoría nueva", None, QtGui.QApplication.UnicodeUTF8))
        self.add.setPlaceholderText(QtGui.QApplication.translate("formulario2", "Nombre Categoría", None, QtGui.QApplication.UnicodeUTF8))
        self.ok.setText(QtGui.QApplication.translate("formulario2", "Ok", None, QtGui.QApplication.UnicodeUTF8))
        self.cancelar.setText(QtGui.QApplication.translate("formulario2", "Cancelar", None, QtGui.QApplication.UnicodeUTF8))

