#ifndef PILA_H
#define PILA_H
#include <iostream>
#include <cstdlib>
#include <string.h>

using namespace std;

class Pila{
      protected:
                class Nodo{
                      public:
                             string valor;
                             Nodo *siguiente;
                };
                
                Nodo * inicio;
      public:
	         Pila(){inicio=0;}
	         void inserta(string valor);
	         void extrae(void);//retorna elemento al tope de la pila y lo elimina
	         string despliega_Tope(void);
	         void eliminarTodo(void);
	         void trabajaStack(string valor, Pila *stack);
};

#endif
