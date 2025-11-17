#/usr/bin/python
# -*- coding: utf-8 -*-

from PIL import Image, ImageDraw,ImageFont
import time


def calc(image):
    im = Image.open(image)
    im1 = Image.open("rgb.jpg")

    a = im.load()
    b = im1.load()

    dm = im.size

    acm=0 
    rojo=0
    verde=0
    azul=0
    for i in range(dm[0]):
        for j in range(dm[1]):
            if a[i,j][0]!=0:
                rojo = ((a[i,j][0]-b[i,j][0])/a[i,j][0])*100 + rojo
            if a[i,j][1]!=0:
                verde = ((a[i,j][1]-b[i,j][1])/a[i,j][1])*100 + verde
            if a[i,j][2]!=0:
                azul = ((a[i,j][2]-b[i,j][2])/a[i,j][2])*100 + azul
        

    rojo = abs(rojo/(dm[0]*dm[1]))
    verde = abs(verde / (dm[0]*dm[1]))
    azul = abs(azul / (dm[0]*dm[1]))

    print("Porcentaje error por color a nivel gral")
    print("{0}%: Rojo - {1}%: Verde - {2}%: Azul".format(rojo,verde,azul))
    print(time.strftime("%H:%M:%S"))
    return time.strftime("%H:%M:%S"), rojo, verde, azul