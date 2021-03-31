#!/usr/bin/python
# -*- coding: utf-8 -*-

#Esta librería posee los métodos necesarios para obtener el alfabeto y los
#estados correspondiente al Autómata ingresado por el usuario. así como las
#instrucciones requeridas para determinar y llenar la matriz de transiciones

import pprint


# Llenamos la matriz de transiciones luego de validarla
def llenarTransiciones(estados, alfabeto, ent):
    n = len(estados)
    m = len(alfabeto)
    print n,m
    #Matriz de transiciones inicializada vacía
    transVacia = [["**************" for x in xrange(m)]for x in xrange(n)]
    transiciones = transVacia
    pprint.pprint(transiciones)
    posFil = 0
    posCol = 0
    #Identificamos las tuplas separadas por ";" en el ingreso
    tuplas = ent.split(';')
    for i in tuplas:
        #Individualizamos el contenido de la tupla mediante el separador ","
        elems = i.split(",")
        cont1 = 0
        cont2 = 0
        #Obtenemos los movimientos de cada estado para ubicar sus posiciones
        #en la matriz de transición
        for a in estados:
            if elems[0] == a:
                posFil = cont1
            cont1 = cont1 + 1
        for b in alfabeto:
            if elems[1] == b:
                posCol = cont2
            cont2 = cont2 + 1
        #Agregamos valores a la matriz de transiciones
        transiciones[posFil][posCol] = elems[0], elems[2]

    #Imprimimos por consola la matriz como técnica de debug. y así comprobar
    #que la programación sea correcta al tener una tabla de transiciones válida.
    print "\nMatriz de Transiciones:\n"
    print "  Est\Alf ",
    for k in range(m):
        print "      [", alfabeto[k],
        print "]   ",
    print "\n"

    for w in range(n):
        print "|  ", estados[w], "  | ",
        for z in range(m):
            print transiciones[w][z],
        print "\n"
    #Retorna la matriz de transiciones
    return transiciones


#Filtramos los estados y el elfabeto de la entrada
def obtEstadosAlfabeto(entrada0):
    #Se crea un arreglo de tuplas al separar la entrada por ";"
    tuplas = entrada0.split(";")
    stringEstados = ""
    stringAlfabeto = ""
    #Se recorre cada elemento de "tuplas" para procesar los datos
    for i in tuplas:
        #Individualizamos elementos de cada tupla separados por ","
        tupla = i.split(",")
        #Guardamos el primera elemento de la tupla (estado)
        estadoActual = tupla[0]
        #Consultamos si el estado ha sido almacenado anteriormente para no
        #almacenar estados repetidos
        if (stringEstados.find(estadoActual) == -1):
            stringEstados += estadoActual
            #Mientras queden tuplas por analizar concatenaremos una ","
            if (i != tuplas[len(tuplas) - 1]):
                stringEstados += ','
        #Guardamos el tercer elemento que corresponde al estado de destino
        estadoSiguiente = tupla[2]
        #Realizamos la misma operación anterior para el estado de destino
        #(sí ha sido agregado lo ignoramos, caso contrario lo agregamos)
        if (stringEstados.find(estadoSiguiente) == -1):
            stringEstados += estadoSiguiente
            if (i != tuplas[len(tuplas) - 1]):
                stringEstados += ','
        #Asignamos el segundo elemento de la tupla (elemento del alfabeto)
        #a una variable auxiliar para ser objeto de comparación
        alfabetoActual = tupla[1]
        #Identificamos el elemento del alfabeto y realizamos el proceso de
        #captura sin repetirlos
        if (stringAlfabeto.find(alfabetoActual) == -1):
            stringAlfabeto += alfabetoActual
            if (i != tuplas[len(tuplas) - 1]):
                stringAlfabeto += ','
    #Terminada la etapa de recorrido y recolección de datos se validan las
    #variables finales y se les da el formato necesario para su posterior uso
    estados = stringEstados.split(',')
    alfabeto = stringAlfabeto.split(',')

    #Imprimimos por consola los estados y el alfabeto para corroborar el
    #correcto funcionamiento del software
    print "Vector Estados:"
    print estados
    print "Vector Alfabeto:"
    print alfabeto
    print "\n"
    return (estados, alfabeto)


