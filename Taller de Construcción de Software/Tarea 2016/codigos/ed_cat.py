# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ed_cat.ui'
#
# Created: Tue Sep  6 03:36:24 2016
#      by: pyside-uic 0.2.15 running on PySide 1.2.1
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_ed_cat(object):
    def setupUi(self, ed_cat):
        ed_cat.setObjectName("ed_cat")
        ed_cat.resize(400, 300)
        ed_cat.setMinimumSize(QtCore.QSize(400, 300))
        ed_cat.setMaximumSize(QtCore.QSize(400, 300))
        self.centralWidget = QtGui.QWidget(ed_cat)
        self.centralWidget.setObjectName("centralWidget")
        self.label = QtGui.QLabel(self.centralWidget)
        self.label.setGeometry(QtCore.QRect(90, 20, 211, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label.setFont(font)
        self.label.setFrameShape(QtGui.QFrame.WinPanel)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.label_2 = QtGui.QLabel(self.centralWidget)
        self.label_2.setGeometry(QtCore.QRect(30, 80, 171, 16))
        self.label_2.setFrameShape(QtGui.QFrame.Panel)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtGui.QLabel(self.centralWidget)
        self.label_3.setGeometry(QtCore.QRect(230, 120, 161, 20))
        self.label_3.setFrameShape(QtGui.QFrame.Panel)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.brr = QtGui.QPushButton(self.centralWidget)
        self.brr.setGeometry(QtCore.QRect(260, 180, 101, 31))
        self.brr.setObjectName("brr")
        self.canc = QtGui.QPushButton(self.centralWidget)
        self.canc.setGeometry(QtCore.QRect(260, 220, 101, 31))
        self.canc.setObjectName("canc")
        self.tabla = QtGui.QTableView(self.centralWidget)
        self.tabla.setGeometry(QtCore.QRect(10, 101, 211, 181))
        self.tabla.setObjectName("tabla")
        self.nuevo = QtGui.QLineEdit(self.centralWidget)
        self.nuevo.setGeometry(QtCore.QRect(250, 150, 113, 23))
        self.nuevo.setObjectName("nuevo")
        ed_cat.setCentralWidget(self.centralWidget)

        self.retranslateUi(ed_cat)
        QtCore.QMetaObject.connectSlotsByName(ed_cat)

    def retranslateUi(self, ed_cat):
        ed_cat.setWindowTitle(QtGui.QApplication.translate("ed_cat", "Eliminar Categoria", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("ed_cat", "Editar Categoria", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("ed_cat", "Categorias Disponibles", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("ed_cat", "Seleccione y Confirme", None, QtGui.QApplication.UnicodeUTF8))
        self.brr.setText(QtGui.QApplication.translate("ed_cat", "Confirmar", None, QtGui.QApplication.UnicodeUTF8))
        self.canc.setText(QtGui.QApplication.translate("ed_cat", "Cancelar", None, QtGui.QApplication.UnicodeUTF8))

