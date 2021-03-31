#!/usr/bin/python
# -*- coding: utf-8 -*- 


import sys
from PySide import QtCore, QtGui
#importar ventana portal para cargarla despues del login
from MPortales import *
from ui_login import Ui_Noticias


class Main(QtGui.QMainWindow):
  def __init__(self):
    super(Main, self).__init__()
    self.ui1 = Ui_Noticias()
    self.ui1.setupUi(self)
    self.botones() #es necesario colocar este metodo, carga la actividad de los objetos
    self.show()

  def botones(self):
    self.ui1.pushButton.clicked.connect(self.validar)
    self.ui1.pushButton_2.clicked.connect(exit)


  def validar(self):
    print "pasa"
    self.errorMessageDialog = QtGui.QMessageBox(self)
    from MPortales import Vtn1
    usr = self.ui1.lineEdit.text()
    pss = self.ui1.lineEdit_2.text()
    usr = "Admin"
    pss = "admin"
    print usr
    print pss
    if (usr == "Admin" and pss == "admin"):
      self.close()
      self.prt = Vtn1()
      self.prt.iniciar().show()
    else:
      self.errorMessageDialog.setText("Datos no válidos: %s , %s"%(usr,pss))
      self.errorMessageDialog.exec_()

def run():
    app = QtGui.QApplication(sys.argv)
    main = Main()
    sys.exit(app.exec_())

if __name__ == '__main__':
    run()