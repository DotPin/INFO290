#!/usr/bin/python
# -*- coding: utf-8 -*-

from sympy import *
import numpy as np
import csv

xx = 7      #Largo de la placa
yy = 5      #Alto de la placa
idx_node = 0
dx = dy = 0.5

xx = int(round(xx/dx))-1
yy = int(round(yy/dy))-1

#matriz = np.zeros((yy,xx),dtype='f')

#matriz = [[Valor for x in range(Columnas)] for x in range(filas)]
matriz = [[0 for x in range(xx)] for x in range(yy)]

range1 = round(yy/2)+1
for i in range(range1):
    matriz[i][i]=1

range2 = int(range1)*2-1
for j in range(i,range2):
    matriz[i][j]=1

for k in range(j+1,j+3):
    i+=1
    matriz[i][k] = 1

for l in range(k+1,k+3):
    matriz[i][l] = 1

def pluss_node(i):
    nd = 'T'+str(i)
    sym = symbols(nd)
    i += 1
    return i,sym

for i in range(yy):
    for j in range(xx):
        if(i==0 and j==0):
            idx_node, matriz[i][j] = pluss_node(idx_node)
            break
        if (matriz[i][j] == 1):
            for k in range(j,xx):
                if (matriz[i][k] == 1):
                    idx_node, matriz[i][k] = pluss_node(idx_node)
                else:
                    break
            break
        else:
            idx_node, matriz[i][j] = pluss_node(idx_node)


print(f'\n\n**********(Mallado ({xx},{yy}))********************')
for a in matriz:
    print(a)

def d_x(ix,iy):     #condiciones de borde para flujo en "X"
    if(iy==0):  #condición de dirichlet
        rst = ((ix+iy)/sqrt(2))*(2*dx) + 4
    elif((iy>1 and iy<4) or iy==4 or iy==5):    #condición de neumann
        rst =  ((ix+iy)/sqrt(2))*(2*dx) + matriz[ix-2][iy]
    return rst


def d_dx(ix,iy):     #diferencia finita de posicionamiento central en "x"
    if (ix==0 and iy==0):
        rst = d_x(ix+1,iy) - 2*matriz[ix][iy] + 4
        return rst
    elif(ix==0 and iy!=yy-1):
        rst = matriz[ix+1][iy] - 2*matriz[ix][iy] + 4
        return rst
    elif(ix<3 and iy<3):
        if(matriz[ix+1][iy]==0):
            rst = d_x(ix+1,iy) - 2*matriz[ix][iy] + matriz[ix-1][iy]
            return rst
        else:
            rst =  matriz[ix+1][iy] - 2*matriz[ix][iy] + matriz[ix-1][iy]
            return rst
    elif(ix==8 or ix==9):
        rst = d_x(ix,iy) -2*matriz[ix][iy] + matriz[ix-1][iy]
        return rst
    elif(ix==xx-1):
        rst =  iy - 2*matriz[ix][iy] + matriz[ix-1][iy]
        return rst
    else:
        rst = matriz[ix+1][iy] - 2*matriz[ix][iy] + matriz[ix-1][iy]
        return rst

polinomios=[]
for i in range(4):
    for j in range(4):
        polinomios.append(d_dx(i,j))

for a in polinomios:
    print(a)

