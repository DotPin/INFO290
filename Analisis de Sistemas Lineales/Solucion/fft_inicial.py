#!/usr/bin/python
# -*- coding: utf-8 -*-



#Importa  coseno, linspace y pi

from numpy import cos, linspace, pi

#importe adicional para convertir arreglo de datos del archivo en arreglo numpy

import numpy as np	

#Importa plot, show, title, xlabel, ylabel y subplot para graficar

from pylab import plot, show, title, xlabel, ylabel, subplot

#Importa fft y arange

from scipy import fft, arange







#

def plotSpectrum(y,Fs):

 """

 grafica la amplitud del espectro de y(t)

 """

 n = len(y) # longitud de la señal

 k = arange(n) #establece el dominio de

 T = n/Fs

 frq = k/T # 2 lados del rango de frecuancia

 frq = frq[range(n/2)] # Un lado del rango de frecuencia



 Y = fft(y)/n # fft calcula la normalizacion

 Y = Y[range(n/2)]

 s_mstr.append(Y)

 plot(frq,abs(Y),'r') # grafica el espectro de frecuencia

 xlabel('Frecuencia (Hz)')

 ylabel('|Y(f)|')





#****************Trozo de muestra de: Frecuencia -> ratio tiempo ->nº de muestras
Fs = 60.0;  # rata de muestreo(Nº de muestreos)

Ts = 1.0/Fs; # intevalo de muestreo(guarda nº de muestras)

t = arange(0,1,Ts) # vector tiempo(fija y genera los intervalos a tasa constante)

#ff = 10;   # frecuencia de la señal(Hz) esta parte no es necesaria debido que la señal ya viene dada

#y = cos(5*pi*ff*t)      #(veces*periodo*frecuencia*dominio) funcion donde ranquea las muestras a normalizar.
#*********************************************************************************
    
s_mstr = []		#vector de guardado de muestras sin normalizar (sin fft)
s_mstr_n = []	#vector de guardado de las submuestras normalizadas (fft)
    
    
#importamos nuestra señal para muestrar
with open("mensaje2.txt","r") as sl:
  senal = sl.readline()		#lee archivo completo
  senal_f = senal.split()		#transforma en lista de strings
    
for i in range(len(senal_f)):
  senal_f[i] = float(senal_f[i])	#transforma la lista completa en datos flotantes
    
y1 = np.array(senal_f)		#transforma en lista python a "array numpy"
    
y_1 = []
y_2=[] 		#se crea arreglo python para guardar un tramo
for i in range(len(t)):
  y_2.append(y1[i])	#<---	#si se desea mostrar el segundo siguiente o desfasado, ingresar y1[i + k] con k múltipo de 1000
				#menciono que por ahora solo muestra una sola gráfica, por lo que espero poder mejorar y entregar los 23seg en un solo plot.
y_2 = np.array(y_2)			#primer tramo de [0,1] segundos "formato lista" en 1000 muestras formato "array numpy"
    
    #n_plot = sqrt(len(senal))+1
    
vv=False    
for i in range(len(y1)):
  y_1.append(senal_f[i])
  if(i%1000)==0 and vv:
    Y = np.array(y_1)
    s_mstr.append(Y)
    Y=[]
    y_1=[]
  elif i==(len(y1)-1):
    Y=np.array(y_1)
    s_mstr.append(Y)
    Y=[]
    y_1=[]
  else:
    vv=True
    
    
#Proceso de normalizar y graficar la señal

subplot(2,1,1)

plot(t,y_2)	#*************************************F(Numero de muestras [(Dominio)], recorrido[[funcion de muestra])]

xlabel('Tiempo')

ylabel('Amplitud')
    
subplot(2,1,2)

#Se llama a la funcion con la señal y la rata de muestreo
plotSpectrum(y_2,Fs)

show()

