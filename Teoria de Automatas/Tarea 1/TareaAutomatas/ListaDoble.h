#ifndef LISTADOBLE_H
#define LISTADOBLE_H
#include <iostream>
#include <cstdlib>
#include <string>

using namespace std;


class ListaDoble{
      protected:
                class Nodo{
                      public:
                             string estado;
                             string simbolo;
                             string stack;
                             string estadoSiguiente;
                             string escribe;
                             Nodo *siguiente;
                             Nodo *anterior;
                };
                
                Nodo *inicio;
                Nodo *ant;
      public:
	         ListaDoble(){inicio=0;}
	         void inserta(string estado, string simbolo, string stack, string estadoSiguiente, string escribe);
	         void elimina(string estado, string simbolo, string stack); 
	         void despliega(void);
	         string buscaEstado(string esta, string simb, string stk);
	         string buscaEscribe(string esta, string simb, string stk);
	         void eliminarTodo(void);
};
#endif
