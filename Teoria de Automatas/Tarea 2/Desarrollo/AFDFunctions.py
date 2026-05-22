#!/usr/bin/python
# -*- coding: utf-8 -*-

# Clase de funciones encargadas de validar el ingreso de información a través
# de la interfaz gráfica entregada al usuario.
# Esto es:
#     -Validar ingreso de transiciones
#     -Validar estado inicial
#     -Validar estado final
#     -Validar el ingreso de la palabra y evaluar si es aceptada o rechazada


#NOTA: se han omitido tildes en mensajes que son procesados por Gui, ya que
#Son desplegados con error. EJ "salida = "Ingrese algun estado Inicial"


class AFDFunctions:

    #Declaración estructural de la clase
    def __init__(self, transiciones, estados, alfabeto):
        self.inicial = ""  # Estado inicial
        self.final = ""  # Estado final
        self.estados = estados  # Arreglo de estados
        self.transiciones = transiciones  # Arreglo de transiciones
        self.alfabeto = alfabeto  # Alfabeto

    #Este método comprueba que se ingrese un estado inicial válido (distinto de
    #vacío y que pertenezca a los estados previamente validados. Entregando un
    #mensaje al usuario de su éxito o fracaso en dicha operación
    def agregaEstIni(self, estIni):
        if(estIni != ""):
            if (estIni in self.estados):
                self.inicial = estIni
                salida = "Estado Inicial agregado"
            else:
                salida = "Ingrese un estado Inicial Valido"
        else:
            salida = "Ingrese algun estado Inicial"
        return salida

    #Este método comprueba que se ingrese un estado final válido (distinto de
    #vacío y que pertenezca a los estados previamente validados. Entregando un
    #mensaje al usuario de su éxito o fracaso en dicha operación
    def agregaEstFin(self, estFin):
        if(estFin != ""):
            if (estFin in self.estados):
                self.final = estFin
                salida = "Estado Final agregado"
            else:
                salida = "Ingrese un estado Final Valido"
        else:
            salida = "Ingrese algun estado Final"
        return salida

    #Este método comprueba que se ingrese una serie de transiciones en el
    #formato indicado en el botón "ejemplo". Validamos formato, cantidad y que
    #existan transiciones repetidas Ej: (q0,a,q1) y (q0,a,q1)
    def validaTrans(self, trans):
        tuplas = trans.split(';')
        salida = ""
        contA = 0
        contB = 0
        contT = 0
        for i in tuplas:
            elems = i.split(",")
            for j in elems:
                if j != '':
                    contT = contT + 1
                print "j: ",j,"contT: ",contT
            print contT
            cantidad = contT
            if(cantidad > 3):
                salida = "Hay Transiciones de mas de 3 elementos"
            if(cantidad < 3):
                salida = "Hay Transiciones de menos de 3 elementos"
            contT = 0
        tupla = [3]
        tupla2 = [3]
        if(salida == ""):
            for i in tuplas:
                tupla = i.split(',')
                for j in tuplas:
                    tupla2 = j.split(',')
                    #Verificamos si hay transiciones repetidas y alertamos
                    #al usuario en dicho caso
                    if ((contA != contB) and (tupla == tupla2)):
                        salida = "Hay Transiciones repetidas en el ingreso, favor verificar"
                    contB = contB + 1
                contA = contA + 1
                contB = 0
        #Verificamos e informamos al usuario del ingreso exitoso
        if(salida == ""):
            salida = "Transiciones Ingresadas"
        return salida

    #Método encargado de verificar el ingreso de una palabra a evaluar.
    #(Distinto de vacío y con los caracteres pertenecientes al alfabeto
    #previamente verificado) ademas de aceptar o rechazar la palabra según
    #corresponda
    def aceptaPalabra(self, pala):
        palabra = list(pala)
        correcto = True
        for i in palabra:
            #comprobamos que el alfabeto de palabra de entrada coincida con
            #el alfabeto determinado en el ingreso de transiciones
            if (i not in self.alfabeto):
                correcto = False
        #En base a lo anterior ejecutamos lo siguiente siempre y cuando
        #la palabra ingresada sea válida
        if (correcto):
            i = 0
            alfabetoActual = palabra[i]
            estadoActual = self.inicial
            posAlfabeto = self.alfabeto.index(alfabetoActual)
            posEstadoActual = self.estados.index(estadoActual)
            #Con los datos anteriores buscamos la transición en la matriz
            #correspondientes al estado actual y el alfabeto que estamos leyendo
            transicion = self.transiciones[posEstadoActual][posAlfabeto]
            #Comprobaremos mientras no tengamos transición vacía, lleguemos al
            #estado final o lleguemos al final de la palabra
            while (alfabetoActual != "*" and transicion != "**************"):
                estadoSiguiente = transicion[1]
                estadoActual = estadoSiguiente  # paso al siguiente estado
                i = i + 1
                #Comprobamos que queden elementos en la palabra por verificar
                #Caso contrario hacemos "alfabetoActual = *" para saltarnos
                #el avance de transición y asegurar la salida del while
                if (i < len(palabra)):
                    alfabetoActual = palabra[i]
                else:
                    alfabetoActual = "*"
                #Comprobamos que no hemos forzado salida y avanzamos transición
                if (alfabetoActual != "*"):
                    posAlfabeto = self.alfabeto.index(alfabetoActual)
                    posEstadoActual = self.estados.index(estadoActual)
                    transicion = self.transiciones[posEstadoActual][posAlfabeto]
            #Terminado el recorrido de la palabra comprobamos si la última
            #transición nos deja en el estado definido como final
            if(estadoActual == self.final):
                salida = "Palabra Aceptada"
            else:
                salida = "Palabra Rechazada"
        else:
            salida = "La Palabra contiene un símbolo No reconocido por el AFD"
        return salida
