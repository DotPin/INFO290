#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
from PySide import QtGui, QtCore


from ctrl_form import FormPaciente
from ui_grid import Ui_Grid
import model as db_model
#grilla de pacientes, donde los agrega, edita y elimina a la lista


class Vtn3(QtGui.QWidget):
    
    def __init__(self):
        super(Vtn3, self).__init__()
        self.ui = Ui_Grid()
        self.ui.setupUi(self)

        self.load_data()
        self.connect_signals()
        self.show()

    def connect_signals(self): #Conexion de los botones para las acciones
        self.ui.btn_add.clicked.connect(self.add)
        self.ui.btn_delete.clicked.connect(self.confirmacion)
        self.ui.btn_edit.clicked.connect(self.edit)

    def add(self):
        self.ui.form = FormPaciente(self) #crea instancia formulario agrega paciente
        self.ui.form.accepted.connect(self.load_data)
        self.ui.form.show()

    def load_data(self):
        """
        Función que carga la información de pacientes en la grilla
        """
        paciente = db_model.obtener_pacientes()
        #Creamos el modelo asociado a la tabla
        self.data = QtGui.QStandardItemModel(len(paciente), 4)
        self.data.setHorizontalHeaderItem(0, QtGui.QStandardItem(u"RUT"))
        self.data.setHorizontalHeaderItem(1, QtGui.QStandardItem(u"Nombres"))
        self.data.setHorizontalHeaderItem(2, QtGui.QStandardItem(u"Apellidos"))
        self.data.setHorizontalHeaderItem(3, QtGui.QStandardItem(u"Ficha Medica"))
	self.data.setHorizontalHeaderItem(4, QtGui.QStandardItem(u"Citas"))
	
        for r, row in enumerate(paciente):
            index = self.data.index(r, 0, QtCore.QModelIndex())
            self.data.setData(index, row['rut'])
            index = self.data.index(r, 1, QtCore.QModelIndex())
            self.data.setData(index, row['nombres'])
            index = self.data.index(r, 2, QtCore.QModelIndex())
            self.data.setData(index, row['apellidos'])
            index = self.data.index(r, 3, QtCore.QModelIndex())
            self.data.setData(index, row['Ficha Medica'])
            index = self.data.index(r, 4, QtCore.QModelIndex())
            self.data.setData(index, row['Citas'])

        self.ui.table.setModel(self.data)

        # Para que las columnas 1 y 2 se estire o contraiga cuando
        # se cambia el tamaño de la pantalla
        self.ui.table.horizontalHeader().setResizeMode(1, self.ui.table.horizontalHeader().Stretch)
        self.ui.table.horizontalHeader().setResizeMode(2, self.ui.table.horizontalHeader().Stretch)

        self.ui.table.setColumnWidth(0, 100)
        self.ui.table.setColumnWidth(1, 210)
        self.ui.table.setColumnWidth(2, 210)
        self.ui.table.setColumnWidth(3, 220)

    def confirmacion(self):

        msbox = QtGui.QMessageBox(self)
        msbox.setText(u"Ud. Está eliminando un usuario del listado")
        msbox.setInformativeText(u"Desea realizar ésta acción?")
        msbox.setStandardButtons(QtGui.QMessageBox.Ok | QtGui.QMessageBox.Cancel)
        rsp = msbox.exec_()

        if rsp == QtGui.QMessageBox.Ok:
            self.delete()        
            print "realiza accion de eliminado"
        else:
            msbox = QtGui.QMessageBox(self)
            msbox.setText("Cambios no realizados")
            msbox.exec_()

    def delete(self):
        #antes de borrar realiza la confirmación del usuario
        data = self.ui.table.model()
        index = self.ui.table.currentIndex()
        if index.row() == -1:  # No se ha seleccionado una fila
            self.errorMessageDialog = QtGui.QErrorMessage(self)
            self.errorMessageDialog.showMessage(u"Debe seleccionar una fila")
            return False
        else:
            rut = data.index(index.row(), 0, QtCore.QModelIndex()).data()
            citas = data.index(index.row(), 4, QtCore.QModelIndex()).data()
            if (db_model.delete_paciente(rut, citas)):
                self.load_data()
                msgBox = QtGui.QMessageBox()
                msgBox.setText(u"EL registro fue eliminado.")
                msgBox.exec_()
                return True
            else:
                self.ui.errorMessageDialog = QtGui.QErrorMessage(self)
                self.ui.errorMessageDialog.showMessage(
                    u"Error al eliminar el registro")
                return False

    def edit(self):
        data = self.ui.table.model()
        index = self.ui.table.currentIndex()
        if index.row() == -1:  # No se ha seleccionado una fila
            self.errorMessageDialog = QtGui.QErrorMessage(self)
            self.errorMessageDialog.showMessage(u"Debe seleccionar una fila")
            return False
        else:
	    rut = data.index(index.row(), 0, QtCore.QModelIndex()).data()
            nombres = data.index(index.row(), 1, QtCore.QModelIndex()).data()
            apellidos = data.index(index.row(), 2, QtCore.QModelIndex()).data()
            ficha = data.index(index.row(), 3, QtCore.QModelIndex()).data()
            self.ui.form = FormPaciente(self, rut, nombres, apellidos, ficha)	#crea un objeto del formulario completo, pasando parámetros
            self.ui.form.accepted.connect(self.load_data)	#lo conecta
            self.ui.form.show()	#lo re-abre para actualizar los datos


if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    main = Vtn3()
    sys.exit(app.exec_())
