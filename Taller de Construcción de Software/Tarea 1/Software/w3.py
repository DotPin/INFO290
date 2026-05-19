# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'w3.ui'
#
# Created: Sun Aug 30 19:07:10 2015
#      by: pyside-uic 0.2.15 running on PySide 1.2.1
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_login(object):
    def setupUi(self, login):
        login.setObjectName("login")
        login.resize(386, 310)
        login.setMinimumSize(QtCore.QSize(386, 310))
        login.setMaximumSize(QtCore.QSize(386, 310))
        self.formLayoutWidget = QtGui.QWidget(login)
        self.formLayoutWidget.setGeometry(QtCore.QRect(100, 110, 181, 80))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout = QtGui.QFormLayout(self.formLayoutWidget)
        self.formLayout.setFieldGrowthPolicy(QtGui.QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.usr_l = QtGui.QLineEdit(self.formLayoutWidget)
        self.usr_l.setObjectName("usr_l")
        self.formLayout.setWidget(0, QtGui.QFormLayout.FieldRole, self.usr_l)
        self.usr = QtGui.QLabel(self.formLayoutWidget)
        self.usr.setObjectName("usr")
        self.formLayout.setWidget(0, QtGui.QFormLayout.LabelRole, self.usr)
        self.pswd = QtGui.QLabel(self.formLayoutWidget)
        self.pswd.setObjectName("pswd")
        self.formLayout.setWidget(1, QtGui.QFormLayout.LabelRole, self.pswd)
        self.pswd_l = QtGui.QLineEdit(self.formLayoutWidget)
        self.pswd_l.setObjectName("pswd_l")
        self.formLayout.setWidget(1, QtGui.QFormLayout.FieldRole, self.pswd_l)
        self.label = QtGui.QLabel(login)
        self.label.setGeometry(QtCore.QRect(80, 0, 291, 101))
        self.label.setAccessibleName("")
        self.label.setObjectName("label")
        self.exit_l = QtGui.QPushButton(login)
        self.exit_l.setGeometry(QtCore.QRect(230, 240, 85, 27))
        self.exit_l.setObjectName("exit_l")
        self.acp_l = QtGui.QPushButton(login)
        self.acp_l.setGeometry(QtCore.QRect(80, 240, 85, 27))
        self.acp_l.setObjectName("acp_l")

        self.retranslateUi(login)
        QtCore.QMetaObject.connectSlotsByName(login)

    def retranslateUi(self, login):
        login.setWindowTitle(QtGui.QApplication.translate("login", "Welcome", None, QtGui.QApplication.UnicodeUTF8))
        self.usr.setText(QtGui.QApplication.translate("login", "Usuario", None, QtGui.QApplication.UnicodeUTF8))
        self.pswd.setText(QtGui.QApplication.translate("login", "Password", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("login", "Bienvenido al software de horas medicas.", None, QtGui.QApplication.UnicodeUTF8))
        self.exit_l.setText(QtGui.QApplication.translate("login", "Salir", None, QtGui.QApplication.UnicodeUTF8))
        self.acp_l.setText(QtGui.QApplication.translate("login", "Aceptar", None, QtGui.QApplication.UnicodeUTF8))

