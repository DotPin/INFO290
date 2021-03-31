#!/usr/bin/python
# -*- coding: utf-8 -*- 

import sys
from PySide import QtCore, QtGui
from turing import Ui_Turing

class Main(QtGui.QMainWindow):
  def __init__(self):
    super(Main, self).__init__()
    self.mt = Ui_Turing()
    self.mt.setupUi(self)
    self.inx = 1 # permite tener el valor del index de la grilla actualizado para ir ingresadolos en orden
    self.model = QtGui.QStandardItemModel(0, 0)
    #self.rsp_model = QtGui.QStandardItemModel(0, 0)
    self.botones()
    self.show()
    
  def botones(self):
    self.mt.bt1.clicked.connect(self.llenar_grilla)
    #self.mt.bt2.clicked.connect(self.editar_campo)
    self.mt.I_trs.clicked.connect(self.numero)

  def numero(self):	#remover para ingreso dinámico
    self.entradas = int(self.mt.n_trs.text())
    if self.entradas < 0:
      msgBox = QtGui.QMessageBox()
      msgBox.setText("Ingrese un numero mayor de transiciones")  # acuso el exito
      msgBox.exec_()
    else:
      self.model = QtGui.QStandardItemModel(self.entradas, 0)
      self.model.setHorizontalHeaderItem(0, QtGui.QStandardItem(u"Transiciones"))
      #self.mt.box.setEnabled(True)	#revisar su modificacion
      #self.mt.I_trs.setEnabled(False)	#revisar su modificacion

  def llenar_grilla(self):
    b = self.mt.in1.text()
    #self.model = QtGui.QStandardItemModel(self.entradas, 0)
    if (self.inx < 2):
      self.model = QtGui.QStandardItemModel(self.inx, 0)
      self.model.setHorizontalHeaderItem(0, QtGui.QStandardItem(u"Transiciones"))
      index = self.model.index(self.inx, 0, QtCore.QModelIndex())
      self.model.setData(index, b)
      self.inx += 1
      self.mt.list_0.setModel(self.model) #paso final
    else:
      
      
    
  #def editar_campo(self):

  #def re_tabla(self):
    #for i in range(0,self.inx):
      #b = self.rsp_model.index(i, 0, QtCore.QModelIndex()).data()	#extraigo desde desde respaldo
      #index = self.model.index(i, 0, QtCore.QModelIndex())	#incorporo index a model extendido creado
      #self.model.setData(index, b)	#incorporo dato de modelo respaldado a model extendido

      
def run():
  app = QtGui.QApplication(sys.argv)
  main = Main()
  sys.exit(app.exec_())

if __name__ == '__main__':
  run()