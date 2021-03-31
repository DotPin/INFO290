#!/usr/bin/python
# -*- coding: UTF-8 -*-

#este programa hace conteo de las palabras ingresadas por el usuario 

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

#**********************************************************************
#*********************Programa Principal*******************************

x = 0
#with open("C:\Documents and Settings\BlackCrystal™\Escritorio\prueba.txt",'w') as a:
with (open("/home/diego/Escritorio/prueba.txt",'w')) as a:
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
print("Ud ingresó en total {0} lineas".format(x))

