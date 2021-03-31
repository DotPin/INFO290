# -*- coding: utf-8 -*-

from PySide import QtGui
from ui_form import Ui_Form
import model


class FormMedico(QtGui.QDialog):

    def __init__(self,parent = None, rut=None, nombres = None, apellidos = None, ficha = None):
        super(FormMedico, self).__init__(parent)
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        if rut is None:# Cuando no recibe rut crea, cuando recibe edita
            self.ui.save.clicked.connect(self.crear_medico)
        else:
            self.colocar_datos(rut, nombres, apellidos, ficha)
            self.ui.save.clicked.connect(self.editar_mdco)

    def colocar_datos(self, rut, nombres, apellidos, ficha):
        #ingresa los datos de los medicos en las grillas
        
        self.ui.rut.setText(str(rut))
        self.ui.names.setText(nombres)
        self.ui.lastnames.setText(apellidos)
        self.ui.email.setText(ficha)

    def obtener_datos(self):
        #obtiene los datos del medico del formulario
        rut = self.ui.rut.text()
        nombres = self.ui.names.text()
        apellidos = self.ui.lastnames.text()
        ficha = self.ui.email.text()
        return (rut, nombres, apellidos, ficha)

    def crear_medico(self):
        rut, nombres, apellidos, ficha = self.obtener_datos()
        print ("%s, %s, %s, %s ")%(rut, nombres, apellidos, ficha)
        try:
            model.agregar_paciente(rut, nombres, apellidos, ficha)
            self.accepted.emit()
            msgBox = QtGui.QMessageBox()
            msgBox.setText(u"El paciente ha sido creado.")
            msgBox.exec_()
            self.close()
        except(ValueError, IOError):
            errorMessageDialog = QtGui.QMessageBox(self)
            self.errorMessageDialog.setText("Debe Completar los campos correctamente")
            self.errorMessageDialog.exec_()
            pass

    def editar_mdco(self):
      
        rut, nombres, apellidos, ficha = self.obtener_datos()
        try:
            model.editar_paciente(rut, nombres, apellidos, ficha)
            print "Editar"
        except (ValueError, IOError):
            errorMessageDialog = QtGui.QMessageBox(self)
            self.errorMessageDialog.setText("Debe Completar los campos correctamente")
            self.errorMessageDialog.exec_()
            pass
