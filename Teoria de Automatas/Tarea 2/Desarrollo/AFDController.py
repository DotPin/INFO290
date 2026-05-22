#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
from PySide import QtGui

# Clase principal que interactúa con el entorno gráfico del sistema (AFDUi),
# haciendo llamado a las funciones subordinadas que se importan en clases
# AFDFunctions y CreateAFD siendo este archivo el controlador intermedio
# entre documentos, funciones propias y despliegue gráfico

import AFDFunctions
from CreateAFD import *
from AFDUi import Ui_MainWindow


class AFDController(QtGui.QMainWindow):

    def __init__(self):  # escencial
        super(AFDController, self).__init__()  # llamado clase principal
        self.ui = Ui_MainWindow()  # creamos objeto Gui para el programa
        self.ui.setupUi(self)
        # conectamos los botones a Gui de sus respectivas funciones
        self.ui.pushButton.clicked.connect(self.ingresar)
        self.ui.pushButton_2.clicked.connect(self.verificar)
        self.ui.pushButton_4.clicked.connect(self.verEjIni)
        self.ui.pushButton_5.clicked.connect(self.verEjFin)
        self.ui.pushButton_3.clicked.connect(self.verEjTrans)
        #entrada de prueba que se ejecuta al iniciar el programa
        #estos datos han sido utilizados para probar nuestro software
        x = "q0,1,q1;q0,0,q2;q1,0,q3;q1,1,q0;q2,0,q0;q2,1,q3;q3,0,q1;q3,1,q2"
        (estados, alfabeto) = obtEstadosAlfabeto(x)
        transiciones = llenarTransiciones(estados, alfabeto, x)
        print "trans: ", transiciones
        self.afd = AFDFunctions.AFDFunctions(transiciones, estados, alfabeto)

    #Método que le da funcionalidad al botón "ingresar", el cual valida
    #el correcto ingreso de información
    def ingresar(self):
        trans = self.ui.plainTextEdit.toPlainText()
        if (trans == ""):  # si la transición es vacía, entrega aviso
            msgBox = QtGui.QMessageBox()
            msgBox.setText("No ha ingresado las Transiciones del AFD")
            msgBox.exec_()
        else:
            #Al tener datos, verificamos que sean del formato correcto
            acepta = self.afd.validaTrans(trans)
            msgBox = QtGui.QMessageBox()
            msgBox.setText(acepta)  # acuso en pantalla
            msgBox.exec_()
            #una vez validada la entrada de transiciones se procede a obtener,
            # identificar y almacenar los datos necesarios
            if(acepta == "Transiciones Ingresadas"):
                (estados, alfabeto) = obtEstadosAlfabeto(trans)
                transiciones = llenarTransiciones(estados, alfabeto, trans)
                #Inicializamos el AFD llamando al constructor de AFDFunctions
                self.afd = AFDFunctions.AFDFunctions(transiciones, estados, alfabeto)
                #Capturamos de la interfaz el estado inicial y final para
                #agregarlos a variables que podamos manipular
                inicial = self.ui.lineEdit.text()
                final = self.ui.lineEdit_2.text()
                ingresa = self.afd.agregaEstIni(inicial)
                msgBox = QtGui.QMessageBox()
                msgBox.setText(ingresa)  # acuso el éxito
                msgBox.exec_()
                ingresa = self.afd.agregaEstFin(final)
                msgBox.setText(ingresa)
                msgBox.exec_()

    #Método que le da funcionalidad al botón "verificar"
    def verificar(self):
        #Comprobamos que estén ingresados los datos requeridos previamente
        if (self.afd.inicial != "" and self.afd.final != ""):
            #Capturamos la palabra de entrada y la asignamos a una variable
            palabra = self.ui.lineEdit_3.text()
            acepta = self.afd.aceptaPalabra(palabra)
            msgBox = QtGui.QMessageBox()
            msgBox.setText(acepta)
            msgBox.exec_()
        else:
            msgBox = QtGui.QMessageBox()
            msgBox.setText("El AFD no esta completo")  # mensaje de error
            msgBox.exec_()

    def verEjIni(self):  # muestra el ejemplo de estado inicial
        msgBox = QtGui.QMessageBox()
        msgBox.setText("Debe ser un estado ingresado en las transiciones \n Ej: q0")
        msgBox.exec_()

    def verEjFin(self):  # muestra el ejemplo de estado final
        msgBox = QtGui.QMessageBox()
        msgBox.setText("Debe ser un estado ingresado en las transiciones \n Ej: q4 o qf")
        msgBox.exec_()

    def verEjTrans(self):  # muestra el ejemplo de Transiciones
        msgBox = QtGui.QMessageBox()
        msgBox.setText("Se debe ingresar las transiciones compuestas por 3-tuplas con el  formato: \n\n       estado_actual,elemento_del_alfabeto,estado_siguiente        \n\nEj:  una 3 tupla    ->   q0,a,q1\n       dos 3 tuplas  ->   q0,a,q1;q1,b,q2\n\nToda tupla se debe separar con ';'\n\nNOTA: si finaliza el ingreso con ';' el sistema esperara una siguiente tupla. por lo que le indicara que esta incompleta\n\nNOTA2: se sugiere ingresar los estados con notacion qn, siendo n el numero del estado. (en cualquier caso el software esta creado para identificar el estado sea cual sea su notacion, ya que el nombre del estado son simples etiquetas para identificarlos)")
        msgBox.exec_()

#Ejemplo de transiciones a evaluar como sujeto de prueba
# x = "q0,1,q1;q0,0,q2;q1,0,q3;q1,1,q0;q2,0,q0;q2,1,q3;q3,0,q1;q3,1,q2";

def run():  # corre la aplicación con gui
    app = QtGui.QApplication(sys.argv)  # escencial
    form = AFDController()
    form.show()  # para mostrar gui
    app.exec_()  # para ejecutar


if __name__ == '__main__':  # método main
    run()
