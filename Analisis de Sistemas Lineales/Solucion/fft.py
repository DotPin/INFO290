#!/usr/bin/python
# -*- coding: utf-8 -*-

#Importa  coseno, linspace y pi

from numpy import cos, linspace, pi

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

 k = arange(n)

 T = n/Fs

 frq = k/T # 2 lados del rango de frecuancia

 frq = frq[range(n/2)] # Un lado del rango de frecuencia



 Y = fft(y)/n # fft calcula la normalizacion

 Y = Y[range(n/2)]



 plot(frq,abs(Y),'r') # grafica el espectro de frecuencia

 xlabel('Frecuencia (Hz)')

 ylabel('|Y(f)|')





if __name__ == '__main__':

    #****************Trozo de muestra de: Frecuencia -> ratio tiempo ->nº de muestras
    Fs = 150.0;  # rata de muestreo(Nº de muestreos)

    Ts = 1.0/Fs; # intevalo de muestreo(guarda nº de muestras)

    t = arange(0,1,Ts) # vector tiempo(fija y genera los intervalos a tasa constante)

    ff = 100;   # frecuencia de la señal(Hz)

    y = cos(5*pi*ff*t)      #(veces*periodo*frecuencia*dominio)
    #*********************************************************************************


    #Proceso de graficar la señal

    subplot(2,1,1)

    plot(t,y)	#*************************************F(Numero de muestras [(Dominio)], recorrido[[funcion de muestra])]

    xlabel('Tiempo')

    ylabel('Amplitud')

    subplot(2,1,2)

    #Se llama a la funcion con la señal y la rata de muestreo

    plotSpectrum(y,Fs)

    show()
