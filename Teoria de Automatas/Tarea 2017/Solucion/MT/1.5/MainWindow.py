# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainWindow2.ui'
#
# Created: Tue Jun 13 01:42:25 2017
#      by: pyside-uic 0.2.15 running on PySide 1.2.1
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(857, 636)
        MainWindow.setMinimumSize(QtCore.QSize(857, 636))
        MainWindow.setMaximumSize(QtCore.QSize(857, 636))
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 10, 241, 16))
        self.label.setObjectName("label")
        self.text_transiciones = QtGui.QTextEdit(self.centralwidget)
        self.text_transiciones.setGeometry(QtCore.QRect(20, 30, 381, 201))
        self.text_transiciones.setObjectName("text_transiciones")
        self.btn_verTrans = QtGui.QPushButton(self.centralwidget)
        self.btn_verTrans.setGeometry(QtCore.QRect(450, 50, 94, 24))
        self.btn_verTrans.setObjectName("btn_verTrans")
        self.btn_verEstIni = QtGui.QPushButton(self.centralwidget)
        self.btn_verEstIni.setGeometry(QtCore.QRect(450, 110, 94, 24))
        self.btn_verEstIni.setObjectName("btn_verEstIni")
        self.btn_verEstFin = QtGui.QPushButton(self.centralwidget)
        self.btn_verEstFin.setGeometry(QtCore.QRect(450, 170, 94, 24))
        self.btn_verEstFin.setObjectName("btn_verEstFin")
        self.btn_ingresar = QtGui.QPushButton(self.centralwidget)
        self.btn_ingresar.setGeometry(QtCore.QRect(260, 260, 94, 24))
        self.btn_ingresar.setObjectName("btn_ingresar")
        self.line_inicial = QtGui.QLineEdit(self.centralwidget)
        self.line_inicial.setGeometry(QtCore.QRect(130, 240, 113, 23))
        self.line_inicial.setObjectName("line_inicial")
        self.line_final = QtGui.QLineEdit(self.centralwidget)
        self.line_final.setGeometry(QtCore.QRect(130, 280, 113, 23))
        self.line_final.setObjectName("line_final")
        self.line_palabra = QtGui.QLineEdit(self.centralwidget)
        self.line_palabra.setGeometry(QtCore.QRect(30, 340, 541, 23))
        self.line_palabra.setObjectName("line_palabra")
        self.label_2 = QtGui.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(40, 240, 81, 21))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtGui.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(40, 280, 81, 21))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtGui.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(410, 30, 141, 21))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtGui.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(410, 90, 151, 21))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtGui.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(410, 150, 141, 20))
        self.label_6.setObjectName("label_6")
        self.label_7 = QtGui.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(50, 320, 131, 21))
        self.label_7.setObjectName("label_7")
        self.btn_verificar = QtGui.QPushButton(self.centralwidget)
        self.btn_verificar.setGeometry(QtCore.QRect(240, 370, 94, 24))
        self.btn_verificar.setObjectName("btn_verificar")
        self.matriz = QtGui.QTableView(self.centralwidget)
        self.matriz.setGeometry(QtCore.QRect(20, 410, 561, 192))
        self.matriz.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.matriz.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.matriz.setObjectName("matriz")
        self.label_8 = QtGui.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(40, 386, 141, 20))
        self.label_8.setObjectName("label_8")
        self.salir = QtGui.QPushButton(self.centralwidget)
        self.salir.setGeometry(QtCore.QRect(410, 250, 141, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setWeight(75)
        font.setBold(True)
        self.salir.setFont(font)
        self.salir.setObjectName("salir")
        self.roteador = QtGui.QTextEdit(self.centralwidget)
        self.roteador.setEnabled(True)
        self.roteador.setGeometry(QtCore.QRect(610, 30, 221, 571))
        self.roteador.setReadOnly(True)
        self.roteador.setObjectName("roteador")
        self.label_9 = QtGui.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(620, 10, 141, 21))
        self.label_9.setObjectName("label_9")
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
        self.label_4.setText(QtGui.QApplication.translate("MainWindow", "Ejemplo de transici??n:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setText(QtGui.QApplication.translate("MainWindow", "Ejemplo de Estado Inicial:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_6.setText(QtGui.QApplication.translate("MainWindow", "Ejemplo de Estado Final:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_7.setText(QtGui.QApplication.translate("MainWindow", "Palabra de Entrada:", None, QtGui.QApplication.UnicodeUTF8))
        self.btn_verificar.setText(QtGui.QApplication.translate("MainWindow", "Verificar", None, QtGui.QApplication.UnicodeUTF8))
        self.label_8.setText(QtGui.QApplication.translate("MainWindow", "Matriz de Transiciones:", None, QtGui.QApplication.UnicodeUTF8))
        self.salir.setText(QtGui.QApplication.translate("MainWindow", "TERMINAR", None, QtGui.QApplication.UnicodeUTF8))
        self.label_9.setText(QtGui.QApplication.translate("MainWindow", "Proceso de Lectura:", None, QtGui.QApplication.UnicodeUTF8))

