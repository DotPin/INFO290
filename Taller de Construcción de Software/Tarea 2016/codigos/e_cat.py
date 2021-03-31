# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'e_cat.ui'
#
# Created: Tue Sep  6 01:30:07 2016
#      by: pyside-uic 0.2.15 running on PySide 1.2.1
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_e_cat(object):
    def setupUi(self, e_cat):
        e_cat.setObjectName("e_cat")
        e_cat.resize(400, 300)
        e_cat.setMinimumSize(QtCore.QSize(400, 300))
        e_cat.setMaximumSize(QtCore.QSize(400, 300))
        self.centralWidget = QtGui.QWidget(e_cat)
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
        self.brr.setGeometry(QtCore.QRect(260, 150, 101, 31))
        self.brr.setObjectName("brr")
        self.canc = QtGui.QPushButton(self.centralWidget)
        self.canc.setGeometry(QtCore.QRect(260, 190, 101, 31))
        self.canc.setObjectName("canc")
        self.tabla = QtGui.QTableView(self.centralWidget)
        self.tabla.setGeometry(QtCore.QRect(10, 101, 211, 181))
        self.tabla.setObjectName("tabla")
        e_cat.setCentralWidget(self.centralWidget)

        self.retranslateUi(e_cat)
        QtCore.QMetaObject.connectSlotsByName(e_cat)

    def retranslateUi(self, e_cat):
        e_cat.setWindowTitle(QtGui.QApplication.translate("e_cat", "Eliminar Categoria", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("e_cat", "Eliminar Categoria", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("e_cat", "Categorias Disponibles", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("e_cat", "Seleccione y Confirme", None, QtGui.QApplication.UnicodeUTF8))
        self.brr.setText(QtGui.QApplication.translate("e_cat", "Confirmar", None, QtGui.QApplication.UnicodeUTF8))
        self.canc.setText(QtGui.QApplication.translate("e_cat", "Cancelar", None, QtGui.QApplication.UnicodeUTF8))

