#!/usr/bin/python
# -*- coding: utf-8 -*-

#importe adicional para convertir arreglo de datos del archivo en arreglo numpy y coseno, linspace y pi
import numpy as np	

#Importa librerías gráficas
import matplotlib.pyplot as plt

# creacion de diccionario de frecuencia valor

freq_val = {
    10: "A",
    20: "B",
    30: "C",
    40: "D",
    50: "E",
    60: "F",
    70: "G",
    80: "H",
    90: "I",
    100: "J",
    110: "K",
    120: "L",
    130: "M",
    140: "N",
    150: "Ñ",
    160: "O",
    170: "P",
    180: "Q",
    190: "R",
    200: "S",
    210: "T",
    220: "U",
    230: "V",
    240: "W",
    250: "X",
    260: "Y",
    270: "Z",
    280: "0",
    290: "1",
    300: "2",
    310: "3",
    320: "4",
    330: "5",
    340: "6",
    350: "7",
    360: "8",
    370: "9"
    }


def plotSpectrum(y, Fs):

# rafica la amplitud del espectro de y(t)

    n = len(y)  # longitud de la señal

    k = np.arange(n)  # establece el dominio de

    T = n / Fs  # lint:ok  # lint:ok

    frq = k / T  # 2 lados del rango de frecuancia

    frq = frq[range(int(n / 2))]  # Un lado del rango de frecuencia

    Y = np.fft.fft(y) / n  # fft calcula la normalizacion

    Y = Y[range(int(n / 2))]

    s_mstr.append(Y)
    # para detectar el valor pick e identificar la letra asociada a la freq
    comparador = max(abs(Y))
    freq_max = 0
    for i in range(len(frq - 1)):
        if (abs(Y)[i]) >= comparador:
            comparador == abs(Y)[i]
            freq_max = i
    # print freq_max

    rsp = { 
        'x':frq,
        'y':abs(Y),
        'title':str(f"{freq_max} [Hz] = {freq_val.get(freq_max)}"),
        'label':['Frecuencia (Hz)','|Y(f)|']
    }

    #ax.plot(frq,abs(Y))
    #ax.set_title(f"{freq_max} [Hz] = {freq_val.get(freq_max)}")
    #ax.set(xlabel='Frecuencia (Hz)',ylabel='|Y(f)|')
    #plt.show()

    return rsp



#****************Trozo de muestra de: Frecuencia -> ratio tiempo ->nº de muestras
Fs = 1000.0;  # rata de muestreo(Nº de muestreos)

Ts = 1.0/Fs; # intevalo de muestreo(guarda nº de muestras)

t = np.arange(0,1,Ts) # vector tiempo(fija y genera los intervalos a tasa constante)

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
    senal_f[i] = float(senal_f[i])  # transforma lista completa en datos float

y1 = np.array(senal_f)  # transforma en lista python a "array numpy"

y_1 = []
desface = 0

# sector inrerfaz usuario
print("Bienvenido al software DecoSignal")
print("Creado por:")
print("\tCaloguerea, Leandro")
print("\tRojas, Diego\n\n")

continua = True

print("Seleccione que señal desea decodificar entre 1 a 23 o un intervalo")
print("de maximo 8 entre 1 a 23 (Por tamaño de la salida\n\n")


def intervalo(v,m,desface):
    # incrementador subplot
    gx = 0 

    #fig, axs = plt.subplots()
    fig, axs = plt.subplots(nrows=8,ncols=2,figsize=(10, 6))
    for i in range(v, m):
        y_2 = []  # se crea arreglo python para guardar un tramo
        for j in range(len(t)):
            y_2.append(y1[j + desface])  # sgte muestra y1[i+k] con k*1000
        y_2 = np.array(y_2)  # primer tramo de [0,1] segs"formato lista" en 1000
                            #  muestras formato "array numpy"
        desface = desface + 1000

        #Se llama a la funcion con la señal y la rata de muestreo
        pl = plotSpectrum(y_2, Fs)

        axs[gx,0].plot(t, y_2)
        if(gx==0):
            axs[gx,0].set_title("Espectro")
        axs[gx,0].relim([i, i + 1])
        if((gx%7)==0):
            axs[gx,0].set(xlabel='Tiempo',ylabel='Amplitud')

        axs[gx,1].plot(pl['x'],pl['y'],label=pl['title'])
        axs[gx,1].legend(fontsize=6)
        if(gx==0):
            axs[gx,1].set_title('Normalizada')
        if((gx%7)==0):
            axs[gx,1].set(xlabel=pl['label'][0],ylabel=pl['label'][1])
        gx = gx +1
    plt.show()

def señal(v,m,desface):
    fig, axs = plt.subplots(nrows=1,ncols=2,figsize=(10, 6))
    for i in range(v, m):
        y_2 = []  # se crea arreglo python para guardar un tramo
        for j in range(len(t)):
            y_2.append(y1[j + desface])  # sgte muestra y1[i+k] con k*1000
        y_2 = np.array(y_2)  # primer tramo de [0,1] segs"formato lista" en 1000
                            #  muestras formato "array numpy"
        desface = desface + 1000

        #Se llama a la funcion con la señal y la rata de muestreo
        pl = plotSpectrum(y_2, Fs)

        axs[0].plot(t, y_2)
        axs[0].set_title("Espectro")
        axs[0].relim([i, i + 1])
        axs[0].set(xlabel='Tiempo',ylabel='Amplitud')

        axs[1].plot(pl['x'],pl['y'],label=pl['title'])
        axs[1].legend(fontsize=6)
        axs[1].set_title('Normalizada')
        axs[1].set(xlabel=pl['label'][0],ylabel=pl['label'][1])
    plt.show()


while continua:
    opcion = input("Ingrese I para seleccionar intervalo o ingrese S para seleccionar una sola señal: ")
    while (opcion != "i") and (opcion != "I") and (opcion != "s") and (opcion != "S"):
        opcion = input("Error, ingrese I para intervalo, S para señal unica:")
    if opcion == "s" or opcion == "S":
        try:    
            m = int(input("Ingrese el numero de la señal que desea codificar (1-23): "))
        except:
            print("Valor incorrecto")
            break
        while (m < 1 or m > 23):
            # delimita el termino de la proxima iteracion
            try:
                m = int(input("Error, fuera de rango o entrada incorrecta, porfavor ingrese un numero de 1 a 23: "))
            except:
                print("Valor incorrecto")
                break
        v = m - 1  # delimita el inicio de la prox iteracion
        d = 2
        dd = 1
        desface = v * 1000
        señal(v,m,desface)

    elif (opcion == "I" or opcion == "i"):
        try:
            v = int(input("Ingrese el inicio del intervalo entre 1 a 16: "))
            while (v < 1 or v > 16):
                v = int(input("Error, fuera de rango o entrada incorrecta, porfavor ingrese un numero de 1 a 15: "))
        except(ValueError):
            print("Valor incorrecto")
            break
        v = v - 1
        m = v + 8
        d = 4
        dd = 4
        desface = (v - 1)*1000
        intervalo(v,m,desface)

    cond = input("\n\nDesea analizar otra señal? -ingrese S para si N para no: ")
    while (cond != "s") and (cond != "S") and (cond != "n") and (cond != "N"):
        cond = input("Error, intente una de las opciones S para si, N para no: ")
    if cond == "s" or cond == "S":
        continua = True
    else:
        continua = False


vv=False
for i in range(len(y1)):
  y_1.append(senal_f[i])
  if( (i%1000)==0 and vv):
    Y = np.array(y_1)
    s_mstr.append(Y)
    Y=[]
    y_1=[]
  elif (i==(len(y1)-1)):
    Y=np.array(y_1)
    s_mstr.append(Y)
    Y=[]
    y_1=[]
  else:
    vv=True
