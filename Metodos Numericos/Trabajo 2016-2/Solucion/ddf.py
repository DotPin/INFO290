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

#condiciones de borde neumann para flujo en "X"
def d_x(ix,iy):
    if(iy==0):
        rst = ((ix+iy)/sqrt(2))*(2*dx) + 4
        return rst
    elif((iy>=1 and iy<5) or ix==4 or ix==5):
        rst =  ((ix+iy)/sqrt(2))*(2*dx) + matriz[ix][iy-2]
        return rst

#diferencia finita de posicionamiento central en "x"
def d_dx(ix,iy):
    #matriz[fila=yy][columna=xx]
    if (ix==0 and iy==0):
        rst = d_x(ix+1,iy) - 2*matriz[ix][iy] + 4
        return rst
    elif(iy==0 and ix<=xx-1):
        rst = matriz[ix][iy+1] - 2*matriz[ix][iy] + 4
        return rst
    elif(ix<4 and iy<4):
        if(matriz[ix][iy+1]==0):
            rst = d_x(ix,iy+1) - 2*matriz[ix][iy] + matriz[ix][iy-1]
            return rst
        else:
            rst =  matriz[ix][iy+1] - 2*matriz[ix][iy] + matriz[ix][iy-1]
            return rst
    elif((ix == 4 and iy==8) or (ix==5 and iy==9)):
        rst = d_x(ix,iy+1) - 2*matriz[ix][iy] + matriz[ix][iy-1]
        return rst
    elif(iy==len(matriz[ix])-1):
        rst =  iy - 2*matriz[ix][iy] + matriz[ix][iy-1]
        return rst
    else:
        rst = matriz[ix][iy+1] - 2*matriz[ix][iy] + matriz[ix][iy-1]
        return rst


#Generando polinomios del mallado.
polinomios=[]
for i in range(4):
    for j in range(4):
        if(j<=i):
            #print(f'({i},{j})={matriz[i][j]}',end="\t")
            polinomios.append(d_dx(i,j))
for i in range(4,6):
    for j in range(0,10):
        if(j<=9):
            #print(f'({i},{j})={matriz[i][j]}',end="\t")
            polinomios.append(d_dx(i,j))
            if(j==8 and matriz[i][j+1]==0): break
for i in range(6,yy):
    for j in range(0,xx):
        polinomios.append(d_dx(i,j))

idx=0
print(f'\nPolinomios generados usando laplaciano (ddx + _ = 0) de diferencias finitas \n')
for a in polinomios:
    print(f'[{idx}]\t=\t{a}')
    idx+=1

print(f'\nPendiente laplaciano ddy para diferencia finita en "y"')
