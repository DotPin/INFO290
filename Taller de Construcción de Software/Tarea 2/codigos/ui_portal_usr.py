# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_portal_usr.ui'
#
# Created: Mon Sep  5 17:50:58 2016
#      by: pyside-uic 0.2.15 running on PySide 1.2.1
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_mostrador(object):
    def setupUi(self, mostrador):
        mostrador.setObjectName("mostrador")
        mostrador.resize(659, 462)
        mostrador.setMinimumSize(QtCore.QSize(659, 462))
        mostrador.setMaximumSize(QtCore.QSize(659, 462))
        self.label = QtGui.QLabel(mostrador)
        self.label.setGeometry(QtCore.QRect(10, 10, 641, 81))
        self.label.setFrameShape(QtGui.QFrame.Box)
        self.label.setFrameShadow(QtGui.QFrame.Sunken)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.filtro = QtGui.QLineEdit(mostrador)
        self.filtro.setGeometry(QtCore.QRect(40, 160, 181, 23))
        self.filtro.setObjectName("filtro")
        self.groupBox = QtGui.QGroupBox(mostrador)
        self.groupBox.setGeometry(QtCore.QRect(260, 100, 261, 80))
        self.groupBox.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.groupBox.setAlignment(QtCore.Qt.AlignCenter)
        self.groupBox.setObjectName("groupBox")
        self.horizontalLayoutWidget = QtGui.QWidget(self.groupBox)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(19, 19, 221, 61))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtGui.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.si = QtGui.QCheckBox(self.horizontalLayoutWidget)
        self.si.setObjectName("si")
        self.horizontalLayout.addWidget(self.si)
        self.no = QtGui.QCheckBox(self.horizontalLayoutWidget)
        self.no.setObjectName("no")
        self.horizontalLayout.addWidget(self.no)
        self.label_2 = QtGui.QLabel(mostrador)
        self.label_2.setGeometry(QtCore.QRect(40, 110, 181, 41))
        self.label_2.setFrameShape(QtGui.QFrame.Box)
        self.label_2.setFrameShadow(QtGui.QFrame.Sunken)
        self.label_2.setTextFormat(QtCore.Qt.AutoText)
        self.label_2.setScaledContents(False)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setMargin(0)
        self.label_2.setObjectName("label_2")
        self.volver = QtGui.QPushButton(mostrador)
        self.volver.setGeometry(QtCore.QRect(530, 130, 111, 41))
        self.volver.setObjectName("volver")
        self.tabla = QtGui.QListView(mostrador)
        self.tabla.setGeometry(QtCore.QRect(10, 190, 641, 261))
        self.tabla.setLocale(QtCore.QLocale(QtCore.QLocale.Spanish, QtCore.QLocale.Chile))
        self.tabla.setObjectName("tabla")

        self.retranslateUi(mostrador)
        QtCore.QMetaObject.connectSlotsByName(mostrador)

    def retranslateUi(self, mostrador):
        mostrador.setWindowTitle(QtGui.QApplication.translate("mostrador", "Listado Noticias", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("mostrador", "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; font-weight:600; font-style:italic; color:#20197f;\">Bienvenido al Revisor de Noticias!</span></p><p align=\"center\"><span style=\" font-size:12pt; font-style:italic;\">Filtre según contenido o publicaciones</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox.setTitle(QtGui.QApplication.translate("mostrador", "Estado Noticias", None, QtGui.QApplication.UnicodeUTF8))
        self.si.setText(QtGui.QApplication.translate("mostrador", "Publicada", None, QtGui.QApplication.UnicodeUTF8))
        self.no.setText(QtGui.QApplication.translate("mostrador", "No Publicada", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("mostrador", "<html><head/><body><p align=\"center\"><span style=\" font-size:10pt; font-style:italic;\">Filtro por Contenido</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.volver.setText(QtGui.QApplication.translate("mostrador", "Volver", None, QtGui.QApplication.UnicodeUTF8))

