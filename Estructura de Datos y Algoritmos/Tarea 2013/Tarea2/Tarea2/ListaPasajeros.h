#ifndef LISTAPASAJEROS_H
#define LISTAPASAJEROS_H
#include <iostream>
#include <cstdlib>
#include <QString>

using namespace std;

class ListaPasajeros{
      protected:
                class Nodo{
                      public://datos publicos de la clase nodo(pasajero)
                             QString codigo;//codigo del vuelo que el pasajero tiene
                             QString rut;//rut del pasajero
                             QString nombre;//nombre del pasajero
                             QString apellido;//apellido del pasajero
                             QString asiento;//asiento del pasajero
                             Nodo *siguiente;//puntero al pasajero(nodo) siguiente
                };

                Nodo * inicio;//puntero al nodo inicial de la lista de pasajeros
      public:
             ListaPasajeros(); //construye una lista de pasajeros de un archivo de entrada con los datos
             void inserta(QString codigo, QString rut, QString nombre, QString apellido, QString asiento);//inserta un nuevo nodo(pasajero) con los datos ingresados
             QString elimina(QString codigo,QString rut);//elimina un pasajero de la lista con coincidencia de codigo de vuelo y su rut
             void cambiaAsiento(QString codigo,QString rut,QString nuevoAsiento);//cambia el asiento de un pasajero en el vuelo reservado
             QString despliegaPasaVuelo(QString codigo);//despliega en salida estandar un alista de los pasajeros del vuelo con coincidencia de codigo
             QString despliegaPasajero(QString codigo, QString rut);//despliega en salida estandar los datos del pasaje reservado de un pasajero con coincidencia de codigo y rut
             void escribir();//escribe en el archivo de salida(mismo eque el de entrada) los datos que fueron cambiados en la lista
};

#endif
