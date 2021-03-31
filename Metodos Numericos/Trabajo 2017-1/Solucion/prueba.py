#!/usr/bin/python
# -*- coding: utf-8 -*-

#Para la ejecución de éste código es necesario tener instalado python v2.7 o superior
#ademas tener instalada la paquetería python-sympy
#desde linux $sudo apt-get install python-sympy
#para windows descargar e instalar el paquete sympy desde el siguiente link:https://pypi.python.org/pypi/sympy


from sympy import *
import csv


#Declaracion de variables

h = 0.999999999999	#condicion de temperaturas
R = 12	#temperatura refrigerante
A = 0	#condicion Cara Aislante
B = 60	#condicion 4

dx = 0.5
dy = 0.5
dz = 0.5

#xx=6
#xy=4
#z=9
dx = input("INgrese valor dx entre 0<dx<1: ")
dy = input("INgrese valor dy entre 0<dy<1: ")
dz = input("INgrese valor dz entre 0<dz<1: ")


xx = input("Ingrese el lado cuadrado: ")
z = input("Ingrese profundidad de la superficie: ")

#Para el caso de evaluar con deltas descomentar las 2 lineas inferiores

xx= int(round(xx/dx))		#dx dy dz son variaciones dif_finitias del nodo para calcular dimensiones correctas de la matriz 3D
z= int(round(z/dz))

#<********************Declaracion de métodos**********************

def mostrar(texto):
  print "************************{}******************************".format(texto)

  for i in range(0,z):		#relleno con las variables "symbolic" a nodos equisdistantes
    print "cara {}".format(i)
    for j in range(0,xx):		#por dentro de la superficie
      for k in range(0,xx):
	if prl[i][j][k] != "":
	  print prl[i][j][k],
	else:
	  print "\t",
	#print "{} \t".format(prl[i][j][k])
      print "\n"

def ddty(x,y,z,j):		#Condiciones de newman
  if j==1:
    z = x-2*dy*h*(x-R)
  elif j== xx-2:
    x = z-2*dy*h*(z-R)
  yyy = (x-2*y+z)/(dy*dy)
  return yyy

def ddtx(x,y,z,i):
  if i==1:
    z = x-2*dy*h*(x-R)
  elif i==xx-2:
    x = z-2*dy*h*(z-R)
  xxx = (x-2*y+z)/(dx*dx)
  return xxx

def ddtz(x,y,z,k):
  if k==1:
    z = x-2*dy*h*(x-A)
  elif k==z-2:
    x = z-2*dy*h*(z-B)
  zzz = (x-2*y+z)/(dz*dz)
  return zzz

#<********************Fin Declaracion de métodos*************************


#Inicio del programa principal

prl = [[["" for x in xrange(xx)] for x in xrange(xx)] for x in xrange(z)]

for i in range(0,z):		#rellenado condiciones de borde
    for j in range(0,xx):
      prl[i][0][j] = R
      prl[i][xx-1][j] = R
      prl[i][j][0] = R
      prl[i][j][xx-1] = R

mostrar("Condiciones de Borde")
      
  
for i in range(1,xx-1):		#Rellenando condiciones en caras
  for j in range(1,xx-1):
    prl[0][i][j] = A
    prl[z-1][i][j] = B

mostrar("Condiciones en Caras")

in_nd = 0
for i in range(1,z-1):		#relleno con las variables "symbolic" a nodos equisdistantes
  for j in range(1,xx-1):		#por dentro de la superficie
    for k in range(1,xx-1):
      nd = "T"+str(in_nd)
      sy = symbols(nd)
      #prl[z][y][x]
      prl[i][j][k] = sy
      print "{}".format(prl[i][j][k])
      in_nd += 1		#numerará los nodos uno x uno hasta terminar cada celda de la matriz	

mostrar("LLenado")    

#x = ["" for x in range(xx*z)] generar vector para generar matriz H[x*y*z] y rellenar con ecuación elíptica de nodos
#despues generar matriz con datos de tipo A[x*y*z,x*y*z] y vector B[x*y*z] a incógnitas de tipo Ax=B



#Haciendo algoritmo para diferencias divididas, para generar los polinomios lineales por cada nodo de la ecuacion laplaceana en 3D.

w = ["" for x in range((xx-2)*(z-2)*(xx-2))]		#Vector para guardar las ecuaciones lineales


in_nd = 0
for i in range(1,z-1):		
  for j in range(1,xx-1):		
    for k in range(1,xx-1):
      w[in_nd] = ddtx(prl[i][j][k+1],prl[i][j][k],prl[i][j][k-1],k) + ddty(prl[i][j+1][k],prl[i][j][k],prl[i][j-1][k-1],j) + ddtx(prl[i+1][j][k],prl[i][j][k],prl[i-1][j][k],i)
      in_nd += 1		

for i in range(len(w)):			#Corroboramos que las ecuaciones estén bien ejecutadas
  print w[i]
  
print "\n\n"
#Realizando descomposición de ecuaciones lineales a matriz

def mM1(aa,txt):
  tt = txt[1].split("T")
  l = int(tt[1])		#sin problemas aki
  if txt[0].find("-")>-1:
    pl = txt[0].split("-")
    ppl = float(pl[1])
    txt[0] = float(ppl*-1)
  M[aa][l] = float(txt[0])
  
  
def mM(aa,txt):
  
  pt2 = txt[len(txt)-1].split("T")
  l = int(pt2[len(txt)-1])
  
  ng2 = float(txt[0])
  M[aa][l] = ng2

def mB(aa,txt):
  B[aa] = txt

M = [[0 for x in xrange((xx-2)*(z-2)*(xx-2))] for x in xrange((xx-2)*(z-2)*(xx-2))]	#genera matriz M

B = [0 for x in xrange((xx-2)*(z-2)*(xx-2))]	#Vector B perteneciente a la matriz

for a in range(len(w)):
  sp = str(w[a]).split("+")
  for b in sp:
    if b.find("-")!= -1:		#determina si algúno posee negativo
      
      if b.find("-")<2:
	pt = b.split("-")		#separa el negativo
	pt[1] = "-"+pt[1]	
      else:
	pt = b.split("-")		#separa el negativo
	pt[1] = "-"+pt[1]	
	
      for c in pt:		#luego separa el multiplicador
	if c != "":
	  pt1 = c.split("*")	
	  mM1(a,pt1)		#funcion para meterlo a matriz
    elif b.find("*")<0:
      if b == "":
	mB(a,0)
      else:
	mB(a,float(b))
    else:  
      ptf = b.split("*")
      mM(a,ptf)

dataCSV2 = open("matriz_b", "wb")
wr = csv.writer(dataCSV2, dialect='excel')
wr.writerows([B])


dataCSV = open("matriz_a", "wb")
writer = csv.writer(dataCSV, dialect='excel')
writer.writerows(M)

    

            


