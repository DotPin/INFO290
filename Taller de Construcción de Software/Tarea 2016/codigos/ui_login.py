# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_login.ui'
#
# Created: Sat Aug 27 03:22:08 2016
#      by: pyside-uic 0.2.15 running on PySide 1.2.1
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_Noticias(object):
    def setupUi(self, Noticias):
        Noticias.setObjectName("Noticias")
        Noticias.resize(383, 282)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Noticias.sizePolicy().hasHeightForWidth())
        Noticias.setSizePolicy(sizePolicy)
        Noticias.setMinimumSize(QtCore.QSize(383, 282))
        Noticias.setMaximumSize(QtCore.QSize(383, 282))
        self.centralWidget = QtGui.QWidget(Noticias)
        self.centralWidget.setObjectName("centralWidget")
        self.label = QtGui.QLabel(self.centralWidget)
        self.label.setGeometry(QtCore.QRect(10, 20, 361, 81))
        self.label.setFrameShape(QtGui.QFrame.WinPanel)
        self.label.setFrameShadow(QtGui.QFrame.Raised)
        self.label.setLineWidth(2)
        self.label.setMidLineWidth(0)
        self.label.setTextFormat(QtCore.Qt.AutoText)
        self.label.setScaledContents(False)
        self.label.setWordWrap(False)
        self.label.setMargin(0)
        self.label.setIndent(0)
        self.label.setObjectName("label")
        self.lineEdit = QtGui.QLineEdit(self.centralWidget)
        self.lineEdit.setGeometry(QtCore.QRect(90, 150, 181, 23))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtGui.QLineEdit(self.centralWidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(90, 180, 181, 23))
        #self.lineEdit_2.setInputMethodHints(QtCore.Qt.ImhHiddenText|QtCore.Qt.ImhNoAutoUppercase|QtCore.Qt.ImhNoPredictiveText|QtCore.Qt.ImhSensitiveData)
        self.lineEdit_2.setEchoMode(QtGui.QLineEdit.Password)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.label_2 = QtGui.QLabel(self.centralWidget)
        self.label_2.setGeometry(QtCore.QRect(50, 110, 281, 20))
        self.label_2.setObjectName("label_2")
        self.pushButton = QtGui.QPushButton(self.centralWidget)
        self.pushButton.setGeometry(QtCore.QRect(70, 220, 101, 31))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtGui.QPushButton(self.centralWidget)
        self.pushButton_2.setGeometry(QtCore.QRect(190, 220, 101, 31))
        self.pushButton_2.setObjectName("pushButton_2")
        Noticias.setCentralWidget(self.centralWidget)

        self.retranslateUi(Noticias)
        QtCore.QMetaObject.connectSlotsByName(Noticias)

    def retranslateUi(self, Noticias):
        Noticias.setWindowTitle(QtGui.QApplication.translate("Noticias", "Noticias", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("Noticias", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:600; font-style:italic;\">Bienvenido al Software Administración </span></p><p align=\"center\"><span style=\" font-size:12pt; font-weight:600; font-style:italic;\">de Noticias!!!</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.lineEdit.setText(QtGui.QApplication.translate("Noticias", "Usuario", None, QtGui.QApplication.UnicodeUTF8))
        self.lineEdit_2.setText(QtGui.QApplication.translate("Noticias", "Contraseña", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("Noticias", "Para ingresar completa los campos de login", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton.setText(QtGui.QApplication.translate("Noticias", "Aceptar", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_2.setText(QtGui.QApplication.translate("Noticias", "Salir", None, QtGui.QApplication.UnicodeUTF8))

