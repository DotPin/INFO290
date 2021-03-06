#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
from PySide import QtGui, QtCore

# importo lo archivos y librerias a utilizar
import MTuring1Cinta
from CreaMT import *
from MainWindow import Ui_MainWindow


class MTuring(QtGui.QMainWindow):

    def __init__(self):  # escencial
        super(MTuring, self).__init__()  # escencial
        self.ui = Ui_MainWindow()  # creo que objeto de gui para el programa
        self.ui.setupUi(self)
        self.ui.btn_ingresar.clicked.connect(self.ingresar)  # conecto los botones de la gui a sus respectivas funciones
        self.ui.btn_verificar.clicked.connect(self.verificar)
        self.ui.btn_verEstIni.clicked.connect(self.verEjIni)
        self.ui.btn_verEstFin.clicked.connect(self.verEjFin)
        self.ui.btn_verTrans.clicked.connect(self.verEjTrans)
        x = "q0,0,q1,x,D;q1,0,q1,0,D;q2,0,q2,0,I;q1,1,q2,y,I;q2,x,q0,x,D;q0,y,q3,y,D;q1,y,q1,y,D;q2,y,q2,y,I;q3,y,q3,y,D;q3,b,q4,b,D"  # instancio el objeto con una mt de muestra
        (estados, alfabeto) = obtEstadosAlfabeto(x)
        transiciones = llenarTransiciones(estados, alfabeto, x)
        self.mt = MTuring1Cinta.MTuring1Cinta(transiciones, estados, alfabeto)

    def ingresar(self):  # ingresa las transiciones y valida
        trans = self.ui.text_transiciones.toPlainText()
        if (trans == ""):  # si la transicion es vacia
            msgBox = QtGui.QMessageBox()
            msgBox.setText("No ha ingresado las Transiciones de la M.Turing")
            msgBox.exec_()
        else:
            acepta = self.mt.validaTrans(trans)  # valida las transiciones por errores de tipeo intencionales o casuales
            msgBox = QtGui.QMessageBox()
            msgBox.setText(acepta)  # acuso en pantalla
            msgBox.exec_()
            if(acepta == "Transiciones Ingresadas"):
                print trans
                (estados, alfabeto) = obtEstadosAlfabeto(trans)  #guardo los estados y alfabeto filtrados de la entrada de transiciones
                transiciones = llenarTransiciones(estados, alfabeto, trans)
                self.mt = MTuring1Cinta.MTuring1Cinta(transiciones, estados, alfabeto)  #creo mi maquina
                inicial = self.ui.line_inicial.text()  # ingreso estao inicial y final
                final = self.ui.line_final.text()
                ingresa = self.mt.agregaEstIni(inicial)
                msgBox = QtGui.QMessageBox()
                msgBox.setText(ingresa)  # acuso el exito
                msgBox.exec_()
                ingresa = self.mt.agregaEstFin(final)
                msgBox.setText(ingresa)
                msgBox.exec_()


    def verificar(self):  # verifica la palabra ingresada
        if (self.mt.inicial != "" and self.mt.final != ""):  # valida estados inicial y final, luego discrimina aceptaci??n de palabra
            palabra = self.ui.line_palabra.text()
            acepta = self.mt.aceptaPalabra(palabra)
            msgBox = QtGui.QMessageBox()
            msgBox.setText(acepta)
            msgBox.exec_()
        else:
            msgBox = QtGui.QMessageBox()
            msgBox.setText("La M. de Turing no esta Completa")  # mensaje de error
            msgBox.exec_()

    def verEjIni(self):  # muestra el ejemplo de estado inicial
        msgBox = QtGui.QMessageBox()
        msgBox.setStyleSheet("QLabel{min-width:400 px; font-size: 18px;} QPushButton{ width:100px; font-size: 18px; }")
        msgBox.setWindowTitle('Ejemplo de estado inicial')
        msgBox.setText("\n\n\n\n\n         El estado inicial es el pivote de nuestra maquina de Turing (MT).\n\n         Se solicita al usuario ingresar un estado que pertenezca a la cadena ingresada en transiciones, caso contrario se le notificara de tal error indicandole que lo intente nuevamente.")
        pixmap = QtGui.QPixmap('ej2.png') 
        pixmap = pixmap.scaled(400,400)
        msgBox.setIconPixmap(QtGui.QPixmap(pixmap))
        msgBox.exec_()        


    def verEjFin(self):  # muestra el ejemplo de estado final
        msgBox = QtGui.QMessageBox()
        msgBox.setStyleSheet("QLabel{min-width:400 px; font-size: 18px;} QPushButton{ width:100px; font-size: 18px; }")
        msgBox.setWindowTitle('Ejemplo de estado final')
        msgBox.setText("\n\n         El estado final es de vital importancia para nuestra maquina, ya que sera el estado con el que se evaluara la aceptacion o rechazo de la palabra a procesar.\n\n         Se solicita al usuario ingresar un estado que pertenezca a la cadena ingresada en transiciones, caso contrario se le notificara de tal error indicandole que lo intente nuevamente.\n\n         El estado debe seguir una estructura q'caracter', donde el caracter puede ser un numero, letra o simbolo.")
        pixmap = QtGui.QPixmap('ej3.png') 
        pixmap = pixmap.scaled(400,400)
        msgBox.setIconPixmap(QtGui.QPixmap(pixmap))
        msgBox.exec_()        


    def verEjTrans(self):  # muestra el ejemplo de Transiciones
        msgBox = QtGui.QMessageBox()
        msgBox.setStyleSheet("QLabel{min-width:400 px; font-size: 18px; font: comic-sans} QPushButton{ width:100px; font-size: 18px; }")
        msgBox.setWindowTitle('Ejemplo de transiciones')
        msgBox.setText("\nUna transicion debe ser ingresada en forma de 5-tupla bajo el siguiente formato:\n\n                                 q,a,p,X,L\n\nDonde:\nq = estado actual\na = Simbolo actual del cabezal\np = Estado siguiente\nX = Simbolo a escribir\nL = Direccion de movimiento del cabezal \n('I' para Izquierda o 'D' para Derecha)\n\nNota1: se debe separar cada transicion con ';'\nNota2: El simbolo blanco debe figurar en las transiciones, se solicitara posteriormente en la palabra a validar como final de cadena y debe ser explicitamente 'B'.")
        pixmap = QtGui.QPixmap('ej1.png') 
        pixmap = pixmap.scaled(400,400)
        msgBox.setIconPixmap(QtGui.QPixmap(pixmap))
        msgBox.exec_()

#  ejemplo de ingreso MT x = "q0,0,q1,x,D;q1,0,q1,0,D;q2,0,q2,0,I;q1,1,q2,y,I;q2,x,q0,x,D;q0,y,q3,y,D;q1,y,q1,y,D;q2,y,q2,y,I;q3,y,q3,y,D;q3,b,q4,b,D"
# Mt con la que debugie errores q0,0,q1,X,D;q0,1,q5,X,D;q0,c,q7,c,D;q1,0,q1,0,D;q1,1,q1,1,D;q1,c,q2,c,D;q2,0,q3,X,I;q2,X,q2,X,D;q3,c,q4,c,I;q3,X,q3,X,I;q4,0,q4,0,I;q4,1,q4,1,I;q4,X,q0,X,D;q5,0,q5,0,D;q5,1,q5,1,D;q5,c,q6,c,D;q6,1,q3,X,I;q6,X,q6,X,D;q7,X,q7,X,D;q7,b,q7,b,D
# es un ejercicio de prueba.

def run():  # corre la aplicacion con gui
    app = QtGui.QApplication(sys.argv)  # escencial
    form = MTuring()
    form.show()  # para mostrar gui
    app.exec_()  # para ejecutar


if __name__ == '__main__':  # metodo main
    run()