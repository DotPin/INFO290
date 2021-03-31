# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'form.ui'
#
# Created: Thu Aug 20 10:54:44 2015
#      by: pyside-uic 0.2.14 running on PySide 1.1.2
#
# WARNING! All changes made in this file will be lost!
#formulario para agregar con datos Nombre, Apellidos, Rut, correos

from PySide import QtCore, QtGui

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(265, 169)
        self.gridLayout = QtGui.QGridLayout(Form)
        self.gridLayout.setObjectName("gridLayout")
        self.save = QtGui.QPushButton(Form)
        self.save.setObjectName("save")
        self.gridLayout.addWidget(self.save, 4, 2, 1, 1)
        self.label = QtGui.QLabel(Form)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.label_2 = QtGui.QLabel(Form)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.label_3 = QtGui.QLabel(Form)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)
        self.cancel = QtGui.QPushButton(Form)
        self.cancel.setObjectName("cancel")
        self.gridLayout.addWidget(self.cancel, 4, 1, 1, 1)
        self.label_4 = QtGui.QLabel(Form)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 3, 0, 1, 1)
        self.email = QtGui.QLineEdit(Form)
        self.email.setObjectName("email")
        self.gridLayout.addWidget(self.email, 3, 1, 1, 2)
        self.lastnames = QtGui.QLineEdit(Form)
        self.lastnames.setObjectName("lastnames")
        self.gridLayout.addWidget(self.lastnames, 2, 1, 1, 2)
        self.rut = QtGui.QLineEdit(Form)
        self.rut.setObjectName("rut")
        self.gridLayout.addWidget(self.rut, 0, 1, 1, 2)
        self.names = QtGui.QLineEdit(Form)
        self.names.setObjectName("names")
        self.gridLayout.addWidget(self.names, 1, 1, 1, 2)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(QtGui.QApplication.translate("Form", "Alumno", None, QtGui.QApplication.UnicodeUTF8))
        self.save.setText(QtGui.QApplication.translate("Form", "Aceptar", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("Form", "RUT:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("Form", "Nombres", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("Form", "Apellidos", None, QtGui.QApplication.UnicodeUTF8))
        self.cancel.setText(QtGui.QApplication.translate("Form", "Cancelar", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("Form", "Correo", None, QtGui.QApplication.UnicodeUTF8))
        self.rut.setPlaceholderText(QtGui.QApplication.translate("Form", "Ingrese rut con guión", None, QtGui.QApplication.UnicodeUTF8))

