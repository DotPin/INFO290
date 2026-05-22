#include "Lista.h"

void Lista::inserta( string estado, string simbolo){
     Nodo *nuevo = new Nodo();
     nuevo->simbolo = simbolo;
     nuevo->estado = estado;
     nuevo->siguiente =0;
     if (inicio ==0){
	 
        inicio = nuevo;
        ant = nuevo;
        trabajando = nuevo;
		}
     else{
         ant->siguiente=nuevo;
         ant = nuevo;     
     }
}
             

void Lista::despliega(){
     Nodo *aux = inicio;
     if (aux){
        cout << aux->simbolo;
        while (aux->siguiente!=0){
              aux = aux->siguiente;
              cout << aux->simbolo ;
        }
     }
     cout <<"\n";
} 

string Lista::lecturaEst(){
	string est;	
	est = trabajando->estado;	
	return (est);
} 

string Lista::lecturaSimb(){
	string simb;
	simb = trabajando->simbolo;
	return (simb);
}

void Lista::mueveTrab(string est){
	(trabajando->siguiente)->estado = est;
	trabajando = trabajando->siguiente;
}

string Lista::compruebaFinal(){
	string res;
	if(trabajando->siguiente==0){
		res="final";		
	}
	else{
		res="no final";
	}
	return res;
}

void Lista::eliminarLista(){
	while(inicio){
		Nodo *aux = inicio;
		inicio = inicio->siguiente;
		delete aux;
	}
}
