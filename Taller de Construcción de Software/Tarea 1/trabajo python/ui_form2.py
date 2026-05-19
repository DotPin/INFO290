# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'form2.ui'
#
# Created: Tue Sep  1 06:47:25 2015
#      by: pyside-uic 0.2.15 running on PySide 1.2.1
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(335, 375)
        self.gridLayout = QtGui.QGridLayout(Form)
        self.gridLayout.setObjectName("gridLayout")
        self.label_7 = QtGui.QLabel(Form)
        self.label_7.setObjectName("label_7")
        self.gridLayout.addWidget(self.label_7, 6, 0, 1, 1)
        self.recomendaciones = QtGui.QLineEdit(Form)
        self.recomendaciones.setObjectName("recomendaciones")
        self.gridLayout.addWidget(self.recomendaciones, 5, 1, 1, 2)
        self.save = QtGui.QPushButton(Form)
        self.save.setObjectName("save")
        self.gridLayout.addWidget(self.save, 7, 2, 1, 1)
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
        self.gridLayout.addWidget(self.cancel, 7, 1, 1, 1)
        self.label_4 = QtGui.QLabel(Form)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 3, 0, 1, 1)
        self.fecha = QtGui.QLineEdit(Form)
        self.fecha.setObjectName("fecha")
        self.gridLayout.addWidget(self.fecha, 2, 1, 1, 2)
        self.p_rut = QtGui.QLineEdit(Form)
        self.p_rut.setObjectName("p_rut")
        self.gridLayout.addWidget(self.p_rut, 0, 1, 1, 2)
        self.m_rut = QtGui.QLineEdit(Form)
        self.m_rut.setObjectName("m_rut")
        self.gridLayout.addWidget(self.m_rut, 1, 1, 1, 2)
        self.diagnostico = QtGui.QLineEdit(Form)
        self.diagnostico.setObjectName("diagnostico")
        self.gridLayout.addWidget(self.diagnostico, 4, 1, 1, 2)
        self.label_6 = QtGui.QLabel(Form)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 5, 0, 1, 1)
        self.receta = QtGui.QLineEdit(Form)
        self.receta.setObjectName("receta")
        self.gridLayout.addWidget(self.receta, 6, 1, 1, 2)
        self.label_5 = QtGui.QLabel(Form)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 4, 0, 1, 1)
        self.sintoma = QtGui.QLineEdit(Form)
        self.sintoma.setObjectName("sintoma")
        self.gridLayout.addWidget(self.sintoma, 3, 1, 1, 2)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(QtGui.QApplication.translate("Form", "Citas", None, QtGui.QApplication.UnicodeUTF8))
        self.label_7.setText(QtGui.QApplication.translate("Form", "Receta", None, QtGui.QApplication.UnicodeUTF8))
        self.save.setText(QtGui.QApplication.translate("Form", "Aceptar", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("Form", "Paciente Rut:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("Form", "Medico Rut:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("Form", "Fecha", None, QtGui.QApplication.UnicodeUTF8))
        self.cancel.setText(QtGui.QApplication.translate("Form", "Cancelar", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("Form", "Sintoma", None, QtGui.QApplication.UnicodeUTF8))
        self.p_rut.setPlaceholderText(QtGui.QApplication.translate("Form", "Ingrese rut con guión", None, QtGui.QApplication.UnicodeUTF8))
        self.label_6.setText(QtGui.QApplication.translate("Form", "Recomendaciones", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setText(QtGui.QApplication.translate("Form", "Diagnostico", None, QtGui.QApplication.UnicodeUTF8))

