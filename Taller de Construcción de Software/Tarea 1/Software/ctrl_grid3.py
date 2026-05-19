#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
from PySide import QtGui, QtCore
from ctrl_form2 import FormMedico
from ui_grid import Ui_Grid
import model as db_model
#grilla de medicos, donde los agrega, edita y elimina a la lista


class Vtn5(QtGui.QWidget):
    
    def __init__(self):
        super(Vtn5, self).__init__()
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
        self.ui.form = FormCita(self) #crea instancia formulario agrega cita
        self.ui.form.accepted.connect(self.load_data)
        self.ui.form.show()

    def load_data(self):
        """
        Función que carga la información de cita en la grilla
        """
        ct = db_model.obtener_cita()
        #Creamos el modelo asociado a la tabla
        self.data = QtGui.QStandardItemModel(len(ct), 7) #revisar q hace
        self.data.setHorizontalHeaderItem(0, QtGui.QStandardItem(u"RUT"))
        self.data.setHorizontalHeaderItem(1, QtGui.QStandardItem(u"Medico"))
        self.data.setHorizontalHeaderItem(2, QtGui.QStandardItem(u"Fecha"))
        self.data.setHorizontalHeaderItem(3, QtGui.QStandardItem(u"Síntoma"))
        self.data.setHorizontalHeaderItem(4, QtGui.QStandardItem(u"Diagnostico"))
        self.data.setHorizontalHeaderItem(5, QtGui.QStandardItem(u"Recomendaciones"))
        self.data.setHorizontalHeaderItem(6, QtGui.QStandardItem(u"Receta"))

        for r, row in enumerate(ct):
            index = self.data.index(r, 0, QtCore.QModelIndex())
            self.data.setData(index, row['paciente_rut'])
            index = self.data.index(r, 1, QtCore.QModelIndex())
            self.data.setData(index, row['medico_rut'])
            index = self.data.index(r, 2, QtCore.QModelIndex())
            self.data.setData(index, row['fecha'])
            index = self.data.index(r, 3, QtCore.QModelIndex())
            self.data.setData(index, row['sintomas'])
            index = self.data.index(r, 4, QtCore.QModelIndex())
            self.data.setData(index, row['diagnostico'])
            index = self.data.index(r, 5, QtCore.QModelIndex())
            self.data.setData(index, row['recomendaciones'])
            index = self.data.index(r, 6, QtCore.QModelIndex())
            self.data.setData(index, row['receta'])

        self.ui.table.setModel(self.data)

        # Para que las columnas 1 y 2 se estire o contraiga cuando
        # se cambia el tamaño de la pantalla
        self.ui.table.horizontalHeader().setResizeMode(1, self.ui.table.horizontalHeader().Stretch)
        self.ui.table.horizontalHeader().setResizeMode(2, self.ui.table.horizontalHeader().Stretch)

        self.ui.table.setColumnWidth(0, 100)
        self.ui.table.setColumnWidth(1, 210)
        self.ui.table.setColumnWidth(2, 210)
        self.ui.table.setColumnWidth(3, 220)
        self.ui.table.setColumnWidth(4, 210)
        self.ui.table.setColumnWidth(5, 220)
        self.ui.table.setColumnWidth(6, 220)

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
            paciente_rut = data.index(index.row(), 0, QtCore.QModelIndex()).data()
            #citas = data.index(index.row(), 4, QtCore.QModelIndex()).data() dejo esgta linea x si las moscas
            if (db_model.borrar(rut)):
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
	    paciente_rut = data.index(index.row(), 0, QtCore.QModelIndex()).data()
	    medico_rut = data.index(index.row(), 1, QtCore.QModelIndex()).data()
	    fecha = data.index(index.row(), 2, QtCore.QModelIndex()).data()
	    sintomas = data.index(index.row(), 3, QtCore.QModelIndex()).data()
	    diagostico = data.index(index.row(), 4, QtCore.QModelIndex()).data()
	    recomendaciones = data.index(index.row(), 5, QtCore.QModelIndex()).data()
	    receta = data.index(index.row(), 6, QtCore.QModelIndex()).data()
            self.ui.form = FormCita(self, rut)
            self.ui.form.accepted.connect(self.load_data)
            self.ui.form.show()


if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    main = Vtn5()
    sys.exit(app.exec_())
