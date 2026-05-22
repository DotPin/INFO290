#include "Pila.h"
#include <sstream>
#include <string>

void Pila::inserta(string valor){
     Nodo *nuevo = new Nodo();
     nuevo->valor = valor;
     nuevo->siguiente=0;
     if (inicio)
        nuevo->siguiente = inicio;  
     inicio=nuevo;
}

void Pila::eliminarTodo(){
	while (inicio){
		Nodo * aux= inicio;
        inicio = inicio->siguiente;
        delete aux;
	}
}
             
void Pila::extrae(void){
     if (inicio){
        Nodo * aux= inicio;
        inicio = inicio->siguiente;
        delete aux;
     }
     else{
         cout << "pila vacia \n";
     }       
} 

string Pila::despliega_Tope(){
     string tope;
	 if (inicio){
            tope = inicio->valor;
     }
     else{
     	tope="E";
	 }
	 return tope; 
}               

void Pila::trabajaStack(string valor, Pila *stack){
	int largo = valor.length();
	stringstream ss;
	string s;
	if(largo>1){
		string res = "";
		for(int i = 0; i < (largo -1);i++){
			res +=valor[i];
		valor=res;
		}
		largo=valor.length();
		for(int i=largo-1 ; i>=0 ; i--){
			ss<<valor[i];
			ss>>s;
			stack->inserta(s);
		}
	}
	else{
		if(valor == "E"){
			stack->extrae();
		}
	}
}
