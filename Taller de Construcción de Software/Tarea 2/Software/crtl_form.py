#!/usr/bin/python
# -*- coding: utf-8 -*- 

import sys
from PySide import QtCore, QtGui
import model as db_nt
from formulario import Ui_formulario

class Frm(QtGui.QMainWindow):
  def iniciar(self):
    self.cat = Ui_formulario()
    self.cat.setupUi(self)
    self.load_cbx()
    self.botones()
    self.show()

  def botones(self):
    validador = QtGui.QIntValidator()
    self.cat.add.clicked.connect(self.ingresar)
    self.cat.dia.setValidator(validador)	#Evitamos que ingresen string en los campos fecha
    self.cat.mes.setValidator(validador)
    self.cat.year.setValidator(validador)
    self.cat.volver.clicked.connect(self.volver)
    

  def volver(self):		#NO OLVIDARSE DEL SELF EN EL METODO PARA ENLAZAR VENTANAS!!!
    self.close()
    from MPortales import Vtn1
    self.b = Vtn1()
    self.b.iniciar()
  
  def load_cbx(self):
    ctg = db_nt.obt_tb_ctgrs()
    for b in ctg:
      self.cat.cmb_ctg.addItem(b["nombre"])

  def ingresar(self):#************************genera arreglo de validaciones
    a = []
    vdd =  True	#inicializa condicion de agregado
    self.errorMessageDialog = QtGui.QMessageBox(self)

    dia = int(self.cat.dia.text())	#deben ser enteros para revisarse en rango numérico
    mes = int(self.cat.mes.text())
    year = int(self.cat.year.text())
    t_noticia = self.cat.t_noticia.text()
    txt_noticia = self.cat.txt_noticia.toPlainText()
    index_c = self.cat.cmb_ctg.currentIndex() + 1
    autor = self.cat.autor.text()
    resumen = self.cat.resumen.text()
    
    a.append(self.val_empty(t_noticia))	#Valido titulo
    a.append(self.val_empty(txt_noticia))	#Valido Texto
    a.append(self.val_empty(resumen))	#valido resumen
    a.append(self.val_empty(autor))		#valido autor
          
    if self.cat.si.isChecked():	#Obtengo publicada
      pbl = 'SI'
    elif self.cat.no.isChecked():
      pbl = 'NO'
    if self.cat.si.isChecked() or self.cat.no.isChecked():
      a.append(True)
    else:
      a.append(False)
    
    if (dia<=31 and dia>=1) and (mes<=12 and mes>=1) and (year>=1000):
      a.append(True)
      fecha = (str(dia)+'-'+str(mes)+'-'+str(year))
    else:
      a.append(False)
      self.errorMessageDialog.setText("Debe Ingresar Formato valido: DD-MM-YYYY")
      self.errorMessageDialog.exec_()
    
    for z in a:		#Evalua el formulario completo
      if not z:
	vdd = False
	
    if vdd:
      db_nt.crea_ntcs(t_noticia,fecha,resumen,txt_noticia,pbl,autor,index_c)
      self.errorMessageDialog.setText("Datos Ingresados!!!")
      self.errorMessageDialog.exec_()
    else:
      self.errorMessageDialog.setText("Faltan Campos por completar")
      self.errorMessageDialog.exec_()
    
  def val_empty(self, text):
    if (text == "" or text == " "):
      return False
    else:
      return True