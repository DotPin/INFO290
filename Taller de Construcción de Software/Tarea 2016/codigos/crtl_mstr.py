#!/usr/bin/python
# -*- coding: utf-8 -*- 

import sys
from PySide import QtCore, QtGui
from MPortales import *
from ui_portal_usr import Ui_mostrador
import model as db_model

#Inicia Ventana de Mostrado de detalles de noticias

class Vtn2 (QtGui.QMainWindow):
  def iniciar(self):
    self.msrt = Ui_mostrador()
    self.msrt.setupUi(self)
    self.load_data()
    self.botones()
    self.show()
      
  def botones(self):
    self.msrt.volver.clicked.connect(self.atras)
    self.msrt.filtro.textChanged.connect(self.cambio_tbl)
    self.msrt.si.stateChanged.connect(self.publicacion_s)
    self.msrt.no.stateChanged.connect(self.publicacion_n)

  def atras(self):
    self.close()
    from MPortales import Vtn1
    self.init = Vtn1()
    self.init.iniciar()
  
  def publicacion_s(self):	#filtro por checkbox publicada
    self.msrt.label.setText(unicode("Otròñe"))
    if self.msrt.si.checkState():
      text = 'SI'
      dts = db_model.filtro(text)
      self.imprimir_en_tabla(dts)
    elif self.msrt.si.checkState() and self.msrt.no.checkState():
      self.load_data()

  def publicacion_n(self):	#filtro por checkbox no publicada
    if self.msrt.no.checkState():
      text = 'NO'
      dts = db_model.filtro(text)
      self.imprimir_en_tabla(dts)
    elif self.msrt.si.checkState() and self.msrt.no.checkState():
      self.load_data()
  
  def load_data(self):
    datos = db_model.mostrar_ntcs()
    self.imprimir_en_tabla(datos)

  def cambio_tbl(self, text):	#filtro por bandeja de texto
    if not(self.msrt.si.checkState() or self.msrt.si.checkState()):	#condicion nor para quitar los check
      self.msrt.si.setChecked(False)
      self.msrt.si.setChecked(False)
    fltr = db_model.refresco(text)		#Guardo datos filtrados
    self.imprimir_en_tabla(fltr)	#llamo a la funcion de grabado a tabla con parámetro de refresco

  def imprimir_en_tabla(self, datos):	#metodo gènerico para impresion de las tablas generadas por querys distintas
    self.model = QtGui.QStandardItemModel(self.msrt.tabla)
    for e in datos:		#llenado de datos en tabla
      a = (e["fecha"]) + "\n"
      a = a + (e["titulo"]) + "\n"
      a = a + (e["resumen"]) + "\n"
      a = a + (e["texto"]) + "\n"
      a = a + (e["publicada"]) + "\n"
      a = a + (e["autor"]) + "\n"
      a = a + (e["Categoria"])
      self.item = QtGui.QStandardItem(a)
      self.model.appendRow(self.item)
      a = ""
    self.msrt.tabla.setModel(self.model)
      
    
    