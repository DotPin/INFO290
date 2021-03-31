#ifndef LISTAVUELOS_H
#define LISTAVUELOS_H
#include <iostream>
#include <cstdlib>

using namespace std;

class ListaVuelos{
      protected:
                class Nodo{
                      public:
                             string codigo;
                             string origen;
                             string destino;
                             string fecha;
                             string hora;
                             string capacidad;
                             string cadAsientos;
                             Nodo *siguiente;
                };
                
                Nodo * inicio;
      public:
	         ListaVuelos();
	         void inserta(string codigo,string origen,string destino,string fecha,string hora,string capacidad,string cadAsientos);
	         void liberaAsiento(string codigo, string asiento);
	         void despliega(void);
};

#endif
