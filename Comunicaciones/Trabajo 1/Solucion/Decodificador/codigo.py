from math import cos,sin,pi
from scipy.fftpack import dct,idct
import numpy as np
import random
from PIL import Image, ImageDraw,ImageFont
import os

#matriz quantization ##
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
#matriz quantization##


################tam de la imagen#####################
def vertam(imagen):
    stam = os.stat(imagen)
    return stam.st_size
###################tam de la imagen###################
def cargar(imagen):
    im = Image.open(imagen)
    ancho, altura = im.size
    pixels = im.load()
    return ancho,altura,pixels,im
##################cargar imagen#################   



##################crear matriz temp#####################################
def temmat(matriz):
    a = np.zeros((8,8))
    #qa = np.zeros((8,8))
    for i in range(8):
        for j in range(8):
            a[i][j] = matriz[i][j] - 128.0
            #qa[i][j] = float(Q[i][j])
    return a

#print a
#print qa
###################crear matriz tem#################################

###################dtc discrete transformer cose######################
def trans(a):
    global qa
    b = dct(a,type=2,n=None,axis=-1,norm='ortho',overwrite_x=False)
    c = idct(b, type=2, n=None, axis=-1, norm='ortho', overwrite_x=False)
    F = np.zeros((8,8))
    for i in range(8):
        for j in range(8):
            F[i][j] = b[i][j]/qa[i][j]
    return F
##################dtc discret transformer##################################################

####################proceso##############################################################
def regr(mat):
    global qa
    new = np.zeros((8,8))
    for i in range(8):
        for j in range(8):
            new[i][j] = mat[i][j]*qa[i][j]
    c = idct(new, type=2, n=None, axis=-1, norm='ortho', overwrite_x=False)

    for i in range(8):
        for j in range(8):
            c[i][j] = c[i][j] + 128
    return c
    
def proces(imagen):
    escala(imagen) ##transformamos imagen a gris
    ancho,altura,pixels,im = cargar("gris.jpg") ##cargamos imagen a gris
    i = 0
    j = 0
    print "valor de altura: ",altura
    print "valor de ancho: ",ancho
    
    

    while i < altura: ##recorre la imagen
        while j < ancho:
            if ancho - j >= 8 and altura - i >= 8:
                mat = []
                for k in range(8): ##bloques de ocho
                    mat.append([])
                    for l in range(8): 
                        #ash += 1
                        mat[k].append(pixels[l+j,k+i][0]) ##vamos guardando la matriz
                        #print "{}".format(pixels[l+j,k+i])
                        
                #print mat
                mat = temmat(mat) ##pasamos la matriz en formato de numpy
                mat = trans(mat) ##hacemos la transformada y la cuantificacion
                #sumc = mat[0][0]
                conts = 0
                array = []
                #print mat
                for k in range(8):
                    for l in range(8):
                        if mat[k][l] != 0 and abs(mat[k][l]) < 1: ##umbralisamos y modificamos
                            mat[k][l]  = 0.0                      #3la matriz cuantificada
                            #print mat[k][l]
                            array.append(pixels[j+l,i+k][0])
                            conts += 1 
                
                finaly = regr(mat) ##aplicamos inverso de dct
                
                for k in range(8): ##pintamos nuevamente
                    for l in range(8):
                        pixels[j+l,i+k] = (int(finaly[k][l]),int(finaly[k][l]),int(finaly[k][l]))
                j = j + 8
            else:
                j = j + 1
            #print j
        i = i + 8
        #print i
        j = 0
    
    im.save("finall.jpeg")
    return
            



#######################proceso#############################################################    
#######################################################################                     
def escala(imagen):
    ancho,altura,pixels,im = cargar(imagen)
    for i in range(ancho):
        for j in range(altura):
            (a,b,c) = pixels[i,j]
            suma = a+b+c
            prom = int(suma/3)
            a = prom ##igualamos                                                                                                              
            b = prom ##igualamos                                                                                                              
            c = prom ##igualamos                                                                                                              
            pixels[i,j] = (a,b,c) ##igualamos                                                                                                 
    im.save("gris.jpg") ##guardamos la imagen nueva                                                              
    return
        #return pygame.image.load(ngrises) ##enviamos la imagen cargada
########################################################################  



def main():
    imagen = raw_input("Dame la imagen: ")
    proces(imagen)
    uno = vertam("gris.jpg")
    dos = vertam("finall.jpeg")
    print "Original : ",uno," bytes vs Nueva : ",dos,"bytes"
    print "porcentaje de compresion :",100.0 - (float(dos)*100.0)/float(uno)," %"

main()