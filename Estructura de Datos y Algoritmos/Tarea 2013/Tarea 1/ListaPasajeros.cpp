#include "ListaPasajeros.h"
#include <fstream>
#include <iostream>

ListaPasajeros::ListaPasajeros(){ // lea la información del archivo de texto  correspondiente.
     inicio = 0;
     char cadena[128];
     string cadena2=" ";
     string arreglo[5];
     string aux="";
     ifstream fe("Pasajeros.txt");
     while (cadena2!=""){
           fe.getline(cadena,128);
           cadena2=cadena;
           if(cadena2!=""){
               for(int i=0; i<4;i++){
                       arreglo[i]=cadena2.substr(0, cadena2.find("|"));
                       cadena2=cadena2.substr(cadena2.find("|")+1,500);
               }
               arreglo[4]=cadena2;
               inserta(arreglo[0],arreglo[1],arreglo[2],arreglo[3],arreglo[4]);
           }
     }
}

void ListaPasajeros::ActualizaPasajeros(){}

void ListaPasajeros::inserta(string codigo, string rut, string nombre, string apellido, string asiento){
     Nodo *nuevo = new Nodo();
     nuevo->codigo = codigo;// asignamos informacion sobre el pasajero al nuevo nodo. 
     nuevo->rut = rut;
     nuevo->nombre = nombre;
     nuevo->apellido = apellido;
     nuevo->asiento = asiento;
     nuevo->siguiente =0;
     Nodo *aux=inicio;
     if (inicio ==0)
        inicio = nuevo;
     else{
         while(aux->siguiente!=0){
               aux=aux->siguiente;                   
         }
         aux->siguiente=nuevo;
         nuevo->siguiente=0;     
     }
}
             
string ListaPasajeros::elimina(string rut){
     string asiento="";
     if (inicio !=0){
        Nodo *aux = inicio;
        if (inicio->rut == rut){
           inicio = inicio->siguiente;
           asiento=aux->asiento;
           delete aux;
           return asiento;
        }
        else{
             Nodo *prev=aux;
             aux = aux->siguiente;
             while (aux && (aux->rut!=rut)){
                   prev = aux;
                   aux = aux->siguiente;
             }
             if (aux !=0){
                prev->siguiente = aux->siguiente;
                asiento=aux->asiento;
                delete aux;
                return asiento;
             }
             else{
                  cout<<"El pasajero no existe";
             }
        }
     }
     return 0;
} 

void ListaPasajeros::despliega(){
     Nodo *aux = inicio;
     cout <<"inicio de la lista \n";
     if (aux){
        cout << aux->codigo << " " << aux->rut << " "<< aux->nombre << " "<< aux->apellido << " "<< aux->asiento <<"\n";
        while (aux->siguiente!=0){
              aux = aux->siguiente;
              cout << aux->codigo << " " << aux->rut << " "<< aux->nombre << " "<< aux->apellido << " "<< aux->asiento <<"\n";
        }
     }
     cout <<"fin de la lista \n";
}               

