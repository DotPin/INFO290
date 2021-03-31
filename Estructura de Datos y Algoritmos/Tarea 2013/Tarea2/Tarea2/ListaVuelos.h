#ifndef LISTAVUELOS_H
#define LISTAVUELOS_H
#include <iostream>
#include <cstdlib>
#include <QString>

using namespace std;

class ListaVuelos{
      protected:
                class Nodo{
                      public://datos publicos de un nodo (un vuelo)
                             QString codigo;//codigo del vuelo
                             QString origen;//origen del vuelo
                             QString destino;//destino del vuelo
                             QString fecha;//fecha del vuelo en formato ddmmaaaa
                             QString hora;//hora de salida del vuelo
                             int capacidad;//capacidad de pasajeros del vuelo
                             QString cadAsientos;//la cadena de asientos ocupados y desocupados del vuelo
                             Nodo *siguiente;//un puntero al siguiente (nodo)vuelo de la lista
                };

                Nodo * inicio;
      public:
             ListaVuelos();//construye una lista de vuelos de un archivo con los datos para ello
             void inserta(QString codigo,QString origen,QString destino,QString fecha,QString hora,int capacidad,QString cadAsientos);//agrega un nuevo vuelo a la lista(es llamado por el constructor)
             void liberaAsiento(QString codigo, QString asiento);//desocupa un asiento de la cadena de asientos del vuelo
             void ocuparAsiento(QString codigo,QString asiento);//deja ocupado un asiento libre
             void despliegaVuelos();//muestra los vuelos disponibles con todos sus datos
             QString despliegaVuelos(QString codigo);//despliega los vuelos con conicidencia de codigo ingresado
             QString despliegaVuelos(QString origen, QString destino);//despliega vuelos con coincidencia de Origen-Destino
             void agregaFila(QString codigo);//agrega una fila de asientos desocupados a la cadena de asientos, y aumenta la capacidad del vuelo
             int asientosDisp(QString codigo);//devuelve un entero con la cantidad de asientos disponibles del vuelo con coincidencia de codigo
             bool estaDisp(QString codigo, QString asiento);//devuelve verdadero si el asiento de dicho vuelo con coincidencia de codigo esta desocupado, si no falso.
             QString despliegaAsientos(QString codigo);//despliega en salida estandar la disponibilidad de asientos como  una matriz indicando filas(numeros) y columnas(letras)
             void escribir();//escribe en el archivo de salida(mismo que el de entrada) los cambios que se hayan hecho en la lista de vuelos
};

#endif
