# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainWindow.ui'
#
# Created: Mon Jun 12 13:13:49 2017
#      by: pyside-uic 0.2.15 running on PySide 1.2.1
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(608, 453)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 30, 241, 16))
        self.label.setObjectName("label")
        self.text_transiciones = QtGui.QTextEdit(self.centralwidget)
        self.text_transiciones.setGeometry(QtCore.QRect(20, 50, 381, 201))
        self.text_transiciones.setObjectName("text_transiciones")
        self.btn_verTrans = QtGui.QPushButton(self.centralwidget)
        self.btn_verTrans.setGeometry(QtCore.QRect(450, 80, 94, 24))
        self.btn_verTrans.setObjectName("btn_verTrans")
        self.btn_verEstIni = QtGui.QPushButton(self.centralwidget)
        self.btn_verEstIni.setGeometry(QtCore.QRect(450, 140, 94, 24))
        self.btn_verEstIni.setObjectName("btn_verEstIni")
        self.btn_verEstFin = QtGui.QPushButton(self.centralwidget)
        self.btn_verEstFin.setGeometry(QtCore.QRect(450, 200, 94, 24))
        self.btn_verEstFin.setObjectName("btn_verEstFin")
        self.btn_ingresar = QtGui.QPushButton(self.centralwidget)
        self.btn_ingresar.setGeometry(QtCore.QRect(260, 290, 94, 24))
        self.btn_ingresar.setObjectName("btn_ingresar")
        self.line_inicial = QtGui.QLineEdit(self.centralwidget)
        self.line_inicial.setGeometry(QtCore.QRect(130, 270, 113, 23))
        self.line_inicial.setObjectName("line_inicial")
        self.line_final = QtGui.QLineEdit(self.centralwidget)
        self.line_final.setGeometry(QtCore.QRect(130, 310, 113, 23))
        self.line_final.setObjectName("line_final")
        self.line_palabra = QtGui.QLineEdit(self.centralwidget)
        self.line_palabra.setGeometry(QtCore.QRect(30, 370, 541, 23))
        self.line_palabra.setObjectName("line_palabra")
        self.label_2 = QtGui.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(40, 270, 81, 21))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtGui.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(40, 310, 81, 21))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtGui.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(410, 60, 141, 21))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtGui.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(410, 120, 151, 21))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtGui.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(410, 180, 141, 20))
        self.label_6.setObjectName("label_6")
        self.label_7 = QtGui.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(50, 350, 131, 21))
        self.label_7.setObjectName("label_7")
        self.btn_verificar = QtGui.QPushButton(self.centralwidget)
        self.btn_verificar.setGeometry(QtCore.QRect(240, 400, 94, 24))
        self.btn_verificar.setObjectName("btn_verificar")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "Simulador Maquina de Turing 1-Cinta by Caloguerea-Rojas-Sanchez", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("MainWindow", "Transiciones (Simbolo blanco = \'B\')", None, QtGui.QApplication.UnicodeUTF8))
        self.btn_verTrans.setText(QtGui.QApplication.translate("MainWindow", "Ver", None, QtGui.QApplication.UnicodeUTF8))
        self.btn_verEstIni.setText(QtGui.QApplication.translate("MainWindow", "Ver", None, QtGui.QApplication.UnicodeUTF8))
        self.btn_verEstFin.setText(QtGui.QApplication.translate("MainWindow", "Ver", None, QtGui.QApplication.UnicodeUTF8))
        self.btn_ingresar.setText(QtGui.QApplication.translate("MainWindow", "Ingresar", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("MainWindow", "Estado Inicial", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("MainWindow", "Estado Final", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("MainWindow", "Ejemplo de transición:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setText(QtGui.QApplication.translate("MainWindow", "Ejemplo de Estado Inicial:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_6.setText(QtGui.QApplication.translate("MainWindow", "Ejemplo de Estado Final:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_7.setText(QtGui.QApplication.translate("MainWindow", "Palabra de Entrada:", None, QtGui.QApplication.UnicodeUTF8))
        self.btn_verificar.setText(QtGui.QApplication.translate("MainWindow", "Verificar", None, QtGui.QApplication.UnicodeUTF8))

