#!/usr/bin/python
# -*- coding: utf-8 -*-

from math import cos
#from scipy.fftpack import dct,idct
import numpy as np
from math import *

def dctTransform(matrix):

    
    dct1 = np.zeros((8,8))
    
    m = len(matrix)
    n = len(matrix)
    for u in range(m):
        for v in range(n):
 
            if (u == 0):
                cu = 1 / sqrt(m)
            else:
                cu = sqrt(2) / sqrt(m)
            
            
            if (v == 0):
                cv = 1 / sqrt(n)
            else:
                cv = sqrt(2) / sqrt(n)
 
 
            sm = 0
            for x in range(m):
                for y in range(n):
                    dct2 = matrix[x][y] * cos(((2 * x + 1) * u * pi) / (2 * m)) * cos(((2 * y + 1) * v * pi) / (2 * n))
                    sm = sm + dct2
                
            
            dct1[u][v] = cu * cv * sm
    return dct1


def main():

    Q= [(16,11,10,16,24,40,51,61),
   (12,12,14,19,26,58,60,55),
   (14,13,16,24,40,57,69,56),
   (14,17,22,29,51,87,80,62),
   (18,22,37,56,68,109,103,77),
   (24,35,55,64,81,104,113,92),
   (49,64,78,87,103,121,120,101),
   (72,92,95,98,112,100,103,99)
   ]
    dctTransform(Q)
    b = dct(Q,type=2,n=None,axis=-1,norm='ortho',overwrite_x=False)
    
    print("DCT SCIPY***********************")
    for i in range(len(Q)):
        for j in range(len(Q)):
            print (b[i][j]+str(","))
        print("\n")
                  


    
