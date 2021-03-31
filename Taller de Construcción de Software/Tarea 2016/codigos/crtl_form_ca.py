#!/usr/bin/python
# -*- coding: utf-8 -*- 

import sys
from PySide import QtCore, QtGui
import model as db_nt
from formulario2 import Ui_formulario2

class Frm2(QtGui.QMainWindow):
  def iniciar(self):
    self.cat = Ui_formulario2()
    self.cat.setupUi(self)
    self.botones()
    self.show()
    
  def botones(self):
    self.cat.ok.clicked.connect(self.oko)
    self.cat.cancelar.clicked.connect(self.can)
    
  def oko(self):
    self.errorMessageDialog = QtGui.QMessageBox(self)
    vdd = False
    data = db_nt.obt_tb_ctgrs()
    texto = self.cat.add.text()
    print len(texto)
    for a in data:
      if texto == a["nombre"] or len(texto) == -0:
	vdd = True
    
    if vdd:
      self.errorMessageDialog.setText("Error, Categoria repetida/Campo sin Completar")
      self.errorMessageDialog.exec_()
    else:
      print "Agrega la categoria: "+texto
      #db_nt.crea_ctgr(texto)
      
  def can(self):
    self.close()
    from MPortales import Vtn1
    self.b = Vtn1()
    self.b.iniciar()