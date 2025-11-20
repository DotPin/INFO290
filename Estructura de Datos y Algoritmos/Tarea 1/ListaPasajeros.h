#ifndef LISTAPASAJEROS_H
#define LISTAPASAJEROS_H
#include <iostream>
#include <cstdlib>

using namespace std;

class ListaPasajeros{
      protected:
                class Nodo{
                      public:
                             string codigo;
                             string rut;
                             string nombre;
                             string apellido;
                             string asiento;
                             Nodo *siguiente;
                };
                
                Nodo * inicio;
      public:
	         ListaPasajeros(); //constructor
	         void inserta(string codigo, string rut, string nombre, string apellido, string asiento);
	         string elimina(string rut);
	         void despliega(void);
	         void ActualizaPasajeros();
};

#endif
