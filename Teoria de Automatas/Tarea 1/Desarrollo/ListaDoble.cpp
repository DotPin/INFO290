#include "ListaDoble.h"

void ListaDoble::inserta(string estado, string simbolo, string stack, string estadoSiguiente, string escribe){
     Nodo* nuevo= new Nodo();
     nuevo->estado= estado;
     nuevo->simbolo = simbolo;
     nuevo->stack = stack;
     nuevo->estadoSiguiente = estadoSiguiente;
     nuevo->escribe = escribe;
     nuevo->siguiente = nuevo->anterior = 0;
     if (inicio==0){
        inicio=nuevo;
        ant = nuevo;
    }
     else{
     	ant->siguiente = nuevo;
        nuevo->anterior = ant;
        ant = nuevo;
     }         
}

void ListaDoble::eliminarTodo(){
	
	while (inicio){
		Nodo * aux = inicio;
		inicio=inicio->siguiente;
		if(inicio!=0){
			inicio->anterior = 0;
		}
		delete aux;
	}
}
	         
void ListaDoble::elimina(string estado, string simbolo, string stack){
     Nodo * aux = inicio;
     if (aux){
          if ((aux->estado == estado)&&(aux->simbolo == simbolo)&&(aux->stack == stack)){
             inicio = inicio->siguiente;
             if (inicio)
                inicio->anterior=0;
             delete aux;
          }
          else{
          	string A = (aux->siguiente)->estado;
          	string B = (aux->siguiente)->simbolo;
          	string C = (aux->siguiente)->stack;

          	while((aux->siguiente)&& ((A!=estado)|| (B!=simbolo)|| (C!=stack))){
          		aux=aux->siguiente;
          		A = (aux->siguiente)->estado;
          		B = (aux->siguiente)->simbolo;
          		C = (aux->siguiente)->stack;
			  }

			if((aux->siguiente) && (A == estado)&&(B == simbolo)&&(C == stack)) {
				Nodo *aux0 =aux->siguiente;
				aux->siguiente = aux0->siguiente;
				if(aux0->siguiente){
					(aux0->siguiente)->anterior = aux;
				}
			delete aux0;
			}
		  }
     }
     
}
	         
             
void ListaDoble::despliega(void){
     Nodo * aux = inicio;
     while(aux){
          cout <<"("<< aux->estado<<","<<aux->simbolo<<","<<aux->stack<<")=("<<aux->estadoSiguiente<<","<<aux->escribe <<")"<< "\n";
          aux = aux->siguiente;
     }
}

string ListaDoble::buscaEstado(string esta, string simb, string stk){
	string est;
	Nodo * aux = inicio;
	while(aux->siguiente && ((aux->estado !=esta)|| (aux->simbolo != simb)|| (aux->stack !=stk)) ){
		aux = aux->siguiente;
	}
	
	if(aux->siguiente == 0){
		if(aux->estado == esta && aux->simbolo == simb && aux->stack ==stk){
			est=aux->estadoSiguiente;
		}
		else{
			est="ERROR";
		}
	}
	else{
		est=aux->estadoSiguiente;
	}
	
	return est;
}

string ListaDoble::buscaEscribe(string esta, string simb, string stk){
	string esc;
	Nodo * aux = inicio;
	while(aux->siguiente && ((aux->estado !=esta)|| (aux->simbolo != simb)|| (aux->stack !=stk)) ){
		aux = aux->siguiente;
	}
	
	if(aux->siguiente == 0){
		if(aux->estado == esta && aux->simbolo == simb && aux->stack ==stk){
			esc=aux->escribe;
		}
		else{
			esc="ERROR";
		}
	}
	else{
		esc=aux->escribe;
	}
	
	return esc;
}


