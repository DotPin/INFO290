#!/usr/bin/python
# -*- coding: utf-8 -*- 

import sys
from PySide import QtCore, QtGui
import model as db_nt
from ed_cat import Ui_ed_cat

class Frm4(QtGui.QMainWindow):
  def iniciar(self):
    self.dog = Ui_ed_cat()
    self.dog.setupUi(self)
    self.load_grid()
    self.botones()
    self.show()
    
  def botones(self):
    self.dog.brr.clicked.connect(self.borrar)
    self.dog.canc.clicked.connect(self.volver)
  
  def volver(self):
    self.close()
    from MPortales import Vtn1
    self.b = Vtn1()
    self.b.iniciar()
  
  def borrar(self):
    self.errorMessageDialog = QtGui.QMessageBox(self)
    data = self.dog.tabla.model()
    index = self.dog.tabla.currentIndex()
    texto = data.index(index.row(), 0, QtCore.QModelIndex()).data()
    #print "Index seleccionada: "+str(index.row()+1)
    texto2 = self.dog.nuevo.text()
    if (texto != "Otro") and (texto2 != "Otro") and (texto2 != "otro"):		#revisa si está seleccionando la categoria Otro
      db_nt.edito_ctgr(texto,texto2)
      dt = db_nt.obt_id_ctgrs(texto)	#obtengo la ID categoría a actualizar
      dt2 = db_nt.obt_id_ctgrs(texto2) 	#Obtengo la id de la categoria
      for a in dt:
	id1 = a["id"]
      for b in dt2:
	id2 = b["id"]
      print id1
      print id2
      db_nt.actualizar(id1,id2)	#cambio fk_id_categoria de las noticias a Otro
    else:
      self.errorMessageDialog.setText(u"Categoría Otro no es Editable")
      self.errorMessageDialog.exec_()
      
  def load_grid(self):
    datos = db_nt.obt_tb_ctgrs()
    self.imprimir_en_tabla(datos)
    
  def imprimir_en_tabla(self, datos):	#metodo gènerico para impresion de las tablas generadas por querys distintas
    self.model = QtGui.QStandardItemModel(len(datos), 0)
    self.model.setHorizontalHeaderItem(0, QtGui.QStandardItem(u"Nombre"))
    for r, row in enumerate(datos):		#llenado de datos en tabla
      index = self.model.index(r, 0, QtCore.QModelIndex())
      self.model.setData(index, row['Nombre'])
    self.dog.tabla.setModel(self.model)