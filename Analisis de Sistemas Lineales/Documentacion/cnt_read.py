#!/usr/bin/python
# -*- coding: UTF-8 -*-

def conteo(plr):
	plr = plr.strip()	
	bl = plr.find(" ")
	cnt = 1
	while bl!=-1:
		cnt += 1
		plr = plr[bl:].strip()
		bl = plr.find(" ")
	print("Ud Ingresó {0} palabras en esta línea".format(cnt))
	return cnt

def cuenta(lst):
	lst = lst.strip()
	bl = lst.find(" ")
	cnt = 1
	while bl != 0:
		cnt += 1
		lst = lst[bl:]
		lst = lst.strip
		bl = lst.find(" ")
	return cnt



#************************************************************************
#*******************Programa principal***********************************

x = 0
#with open("C:\Documents and Settings\BlackCrystal™\Escritorio\prueba.txt",'w') as a:
with (open("/home/hackerter/Documentos/Algoritmos/Analisis/prueba.txt",'w')) as a:
	n = int(input("Ingrese el numero de lineas: "))
	while n<=0:
		print("Error")
		n = int(input("Intente otravez: "))
	for i in range (0,n):
		frase = input("Ingrese alguna frase: ")
		if len(frase)>0:
			x = conteo(frase) + x
		else:
			print("Ud no ingresó palabras \n")
		if i<= n-1 and frase!=(""):
			a.write(frase+"\n")
		else:
			a.write("\n")
print("*"*50+"\n")
linea=""

with (open("/home/hackerter/Documentos/Algoritmos/Analisis/prueba.txt",'r')) as a:
	for i in range (1,n+1):
	  print("segunda parte")
	  while linea in a:
	    if linea == "":
		print("La línea no tiene contenido")
	    else:
		print("La línea {0} tiene {1} palabras".format(i,cuenta(linea)))				
	

