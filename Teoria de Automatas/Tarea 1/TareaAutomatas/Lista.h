#ifndef LISTA_H
#define LISTA_H
#include <iostream>
#include <cstdlib>
#include <string>

using namespace std;

class Lista{
      protected:
                class Nodo{
                      public:
                             string simbolo;
                             string estado;
                             Nodo *siguiente;
                            
                };
                
                Nodo * inicio;
                Nodo * ant;
                Nodo * trabajando;
      public:
	         Lista(){inicio=0;}
	         void inserta(string estado, string simbolo);
	         void despliega(void);
	         string lecturaEst(void);
	         string lecturaSimb(void);
	         void mueveTrab(string est);
	         string compruebaFinal(void);
	         void eliminarLista(void);
	        
};

#endif
             
