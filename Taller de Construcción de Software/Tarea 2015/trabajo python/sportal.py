# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'sportal.ui'
#
# Created: Sun Aug 30 21:30:25 2015
#      by: pyside-uic 0.2.15 running on PySide 1.2.1
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_inicio(object):
    def setupUi(self, inicio):
        inicio.setObjectName("inicio")
        inicio.resize(386, 310)
        inicio.setMinimumSize(QtCore.QSize(386, 310))
        inicio.setMaximumSize(QtCore.QSize(386, 310))
        self.label = QtGui.QLabel(inicio)
        self.label.setGeometry(QtCore.QRect(80, 0, 291, 101))
        self.label.setAccessibleName("")
        self.label.setObjectName("label")
        self.exit_i = QtGui.QPushButton(inicio)
        self.exit_i.setGeometry(QtCore.QRect(150, 240, 85, 27))
        self.exit_i.setObjectName("exit_i")
        self.verticalLayoutWidget = QtGui.QWidget(inicio)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(79, 100, 231, 95))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtGui.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.pc_i = QtGui.QPushButton(self.verticalLayoutWidget)
        self.pc_i.setObjectName("pc_i")
        self.verticalLayout.addWidget(self.pc_i)
        self.pp_i = QtGui.QPushButton(self.verticalLayoutWidget)
        self.pp_i.setObjectName("pp_i")
        self.verticalLayout.addWidget(self.pp_i)
        self.pm_i = QtGui.QPushButton(self.verticalLayoutWidget)
        self.pm_i.setObjectName("pm_i")
        self.verticalLayout.addWidget(self.pm_i)

        self.retranslateUi(inicio)
        QtCore.QMetaObject.connectSlotsByName(inicio)

    def retranslateUi(self, inicio):
        inicio.setWindowTitle(QtGui.QApplication.translate("inicio", "Welcome", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("inicio", "Seleccione el portal que desea administrar", None, QtGui.QApplication.UnicodeUTF8))
        self.exit_i.setText(QtGui.QApplication.translate("inicio", "Volver", None, QtGui.QApplication.UnicodeUTF8))
        self.pc_i.setText(QtGui.QApplication.translate("inicio", "Portal Citas", None, QtGui.QApplication.UnicodeUTF8))
        self.pp_i.setText(QtGui.QApplication.translate("inicio", "Portal Pacientes", None, QtGui.QApplication.UnicodeUTF8))
        self.pm_i.setText(QtGui.QApplication.translate("inicio", "Portal Medicos", None, QtGui.QApplication.UnicodeUTF8))

