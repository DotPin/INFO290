# -*- coding: utf-8 -*-

import sys
from PySide import QtCore, QtGui
from sportal import Ui_inicio
from crtl_main import *
from ctrl_grid import *
from ctrl_grid2 import *
from ctrl_grid3 import *
from ui_grid import *


class Vtn2(QtGui.QMainWindow):

    def iniciar(self):
        self.ui2 = Ui_inicio()
        self.ui2.setupUi(self)
        self.botones()
        self.show()

    def botones(self):
        self.ui2.exit_i.clicked.connect(self.volver)
        self.ui2.pp_i.clicked.connect(self.pPaciente)
        self.ui2.pm_i.clicked.connect(self.pMedicos)
        self.ui2.pc_i.clicked.connect(self.pCitas)

    def volver(self):
        self.close()
        inicio = Main()
        inicio.__init__().iniciar()

    def pPaciente(self):
        print "entro a pacientes"
        self.v3 = Vtn3()
        self.v3.iniciarP()

    def pMedicos(self):
      print "entro a medico"
      self.v4 =  Vtn4()
      self.v4.iniciarP()

    def pCitas(self):
      print "entro a citas"
      self.v5 =  Vtn5()
      self.v5.iniciarP()



