#/usr/bin/python
# -*- coding: utf-8 -*-
from PIL import Image, ImageDraw,ImageFont
from scipy.fftpack import dct,idct
import numpy as np
import dct2 as dc
import idct2 as idc
import calculo as err
import os
import time
import sys


def ycc(r, g, b): 
    y = int(.299*r + .587*g + .114*b)
    cb = int(128 -.168736*r -.331364*g + .5*b)
    cr = int(128 +.5*r - .418688*g - .081312*b)
    return y, cb, cr

def rgb(y, cb, cr):
    r = int(y + 1.403 * (cr-128))
    g = int(y - .34414 * (cb-128) -  .71414 * (cr-128))
    b = int(y + 1.773 * (cb-128))
    return r, g, b

def cargar(imagen):
     im = Image.open(imagen)
     ancho, altura = im.size
     pixels = im.load()
     return ancho,altura,pixels,im
 
def tam(imagen):
    stam = os.stat(imagen)
    return stam.st_size

def tablaY(imagen):
    ancho,altura,pixels,im = cargar(imagen)
    pxls = pixels
    for i in range(ancho):
         for j in range(altura):
            pixels[i,j] =  ycc(pxls[i,j][0],pxls[i,j][1],pxls[i,j][2])
    im.save("ycbcr.jpg")

 
def retorno(imagen):
    ancho,altura,pixels,im = cargar(imagen)
    pxls = pixels
    for i in range(ancho):
         for j in range(altura):
            pixels[i,j] =  rgb(pxls[i,j][0],pxls[i,j][1],pxls[i,j][2])
    im.save("rgb.jpg") 

Q= [(16,11,10,16,24,40,51,61),
   (12,12,14,19,26,58,60,55),
   (14,13,16,24,40,57,69,56),
   (14,17,22,29,51,87,80,62),
   (18,22,37,56,68,109,103,77),
   (24,35,55,64,81,104,113,92),
   (49,64,78,87,103,121,120,101),
   (72,92,95,98,112,100,103,99)
]
qa = np.zeros((8,8))
for i in range(8):
    for j in range(8):
        qa[i][j] = Q[i][j]



################## transformada ##################################################
def trans(a):
    global qa
    #Librería en mantención
    #t = dc.dctTransform(a)
    t = dct(a,type=2,n=None,axis=-1,norm='ortho',overwrite_x=False)
    F = np.zeros((8,8))
    for i in range(8):
        for j in range(8):
            F[i][j] = t[i][j]/qa[i][j]
    return F

##################matriz temporal#####################################
def tmp(matriz):
    a = np.zeros((8,8))
    for i in range(8):
        for j in range(8):
            a[i][j] = matriz[i][j] - 128.0
    
    return a

################## transformada inversa##################################################
def inv(mt):
    global qa
    new = np.zeros((8,8))
    for i in range(8):
        for j in range(8):
            new[i][j] = mt[i][j]*qa[i][j]

    #Librería en mantención
    #t = idc.dctTransform(new)
    t = idct(new, type=2, n=None, axis=-1, norm='ortho', overwrite_x=False)

    for i in range(8):
        for j in range(8):
            t[i][j] = t[i][j] + 128
    return t


################## proceso completo de transformacion###########################
def proces(imagen):
    ancho,altura,pixels,im = cargar(imagen) 
    i = 0
    j = 0
 
    while i < altura: 
        while j < ancho:
            if ancho - j >= 8 and altura - i >= 8:
                ############calculo para regiòn roja
                mt = []
                for k in range(8): 
                    mt.append([])
                    for l in range(8): 
                        mt[k].append(pixels[l+j,k+i][0]) 
                        
                
                mt = tmp(mt) 
                mt = trans(mt) 
                Y = inv(mt)
                
                             
                ######################calculo para regiòn verde
                mt1 = []
                for k in range(8):
                    mt1.append([])
                    for l in range(8): 
                        mt1[k].append(pixels[l+j,k+i][1]) 
                        
                        
                mt1 = tmp(mt1) 
                mt1 = trans(mt1) 
                Cb = inv(mt1)
                
                ################calculo para region azul
                mt2 = []
                for k in range(8): 
                    mt2.append([])
                    for l in range(8): 
                        mt2[k].append(pixels[l+j,k+i][2]) 
                        
                        
                mt2 = tmp(mt2) 
                mt2 = trans(mt2) 
                Cr = inv(mt2) 
                
                ################ensamble
                for k in range(8): 
                    for l in range(8):
                        pixels[j+l,i+k] = (int(Y[k][l]),int(Cb[k][l]),int(Cr[k][l]))
                j = j + 8
            else:
                j = j + 1
            
        i = i + 8
        j = 0
    
    im.save("trans.jpg")
   

 


def main():
    
    #imagen = input("Ingrese imagen: ")
    imagen = sys.argv[1]
    print(time.strftime("%H:%M:%S"))
    tiempoI = time.strftime("%H:%M:%S")
    tablaY(imagen)
    print("ycbcr")
    proces("ycbcr.jpg")
    print("transforma")
    retorno("trans.jpg")
    print("dimensiona")
    uno = tam(imagen)
    print("dimensiona 2")
    dos = tam("rgb.jpg")
    print ("Original : ",uno," bytes vs Nueva : ",dos,"bytes")
    print ("porcentaje de compresion :",100.0 - (float(dos)*100.0)/float(uno),") %")
    rar = 100.0 - (float(dos)*100.0)/float(uno)
    tiempoF, rojo, verde, azul = err.calc(imagen)
    imagen = imagen.split(".")
    archivo = imagen[0]+".txt"
    with (open(archivo,'w')) as a:
        a.write(str(imagen[0])+"\n")
        a.write(tiempoI+"\n")
        a.write(tiempoF+"\n")
        a.write(str(uno)+"\n")
        a.write(str(dos)+"\n")
        a.write(str(rar)+"\n")
        a.write(str(rojo)+"\n")
        a.write(str(verde)+"\n")
        a.write(str(azul)+"\n")
        
 
main()
 

 
 
        
 
 
 
