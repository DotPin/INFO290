# -*- coding: utf-8 -*-

import sys
from PySide import QtCore, QtGui
from Mportal2 import *
from w3 import Ui_login


class Main(QtGui.QMainWindow):
    def __init__(self):
        super(Main, self).__init__()
        self.ui1 = Ui_login()
        self.ui1.setupUi(self)
        self.botones()
        self.show()

    def botones(self):
        self.ui1.acp_l.clicked.connect(self.validar)
        self.ui1.exit_l.clicked.connect(exit)


    def validar(self):
        from Mportal2 import * # Se carga nuevamente para evitar conflicto
        self.errorMessageDialog = QtGui.QMessageBox(self)
        #usr = self.ui1.usr_l.text()
        #psswd = self.ui1.pswd_l.text()
        usr = "admin"
        psswd = "admin"
        if (usr == "admin" and psswd == "admin"):
            self.close()
            self.v2 = Vtn2()
            self.v2.iniciar().show()
        else:
            self.errorMessageDialog.setText("Usuario que pasa %s , %s"%(usr,psswd))
            #self.errorMessageDialog.setText("Usuario no registrado")
            self.errorMessageDialog.exec_()




def run():
    app = QtGui.QApplication(sys.argv)
    main = Main()
    sys.exit(app.exec_())

if __name__ == '__main__':
    run()