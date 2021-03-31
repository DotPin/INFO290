# -*- coding: utf-8 -*-

from PySide import QtGui
from ui_form2 import Ui_Form
import model


class FormCitas(QtGui.QDialog):

    def __init__(self, parent=None, rut=None): #que parametros van aqui?
        super(FormCitas, self).__init__(parent)
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        if rut is None:# Cuando no recibe rut crea, cuando recibe edita
            self.ui.save.clicked.connect(self.crear_ct)
        else:
            self.colocar_datos(paciente_rut,medico_rut,fecha,sintomas,diagnostico,recomendaciones,receta)
            self.ui.save.clicked.connect(self.editar_cita)

    def colocar_datos(self, paciente_rut,medico_rut,fecha,sintomas,diagnostico,recomendaciones,receta):
        #ingresa los datos de los medicos en las grillas
        
        self.ui.p_rut.setText(str(paciente_rut))
        self.ui.m_rut.setText(str(medico_rut))
        self.ui.fecha.setText(fecha)
        self.ui.sintomas.setText(sintomas)
        self.ui.diagnostico.setText(diagostico)
        self.ui.recomendaciones.setText(recomendaciones)
        self.ui.receta.setText(receta)

    def obtener_datos(self):
        #obtiene los datos del medico del formulario
        paciente_rut = self.ui.p_rut.Text()
        medico_rut = self.ui.m_rut.Text()
        fecha = self.ui.fecha.Text()
        sintomas = self.ui.sintomas.Text()
        diagostico = self.ui.diagnostico.Text()
        recomendaciones = self.ui.recomendaciones.Text()
        receta = self.ui.receta.Text()
        return (paciente_rut,medico_rut,fecha,sintomas,diagnostico,recomendaciones,receta)

    def crear_ct(self):
        paciente_rut,medico_rut,fecha,sintomas,diagnostico,recomendaciones,receta = self.obtener_datos()
        
        try:
            model.agregar_paciente(paciente_rut,medico_rut,fecha,sintomas,diagnostico,recomendaciones,receta)
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

    def editar_cita(self):
      
        rut, nombres, apellidos, ficha = self.obtener_datos()
        try:
            model.editar_cita(paciente_rut,medico_rut,fecha,sintomas,diagnostico,recomendaciones,receta)
            print "Editar"
        except (ValueError, IOError):
            errorMessageDialog = QtGui.QMessageBox(self)
            self.errorMessageDialog.setText("Debe Completar los campos correctamente")
            self.errorMessageDialog.exec_()
            pass
