#include "ListaVuelos.h"
#include <fstream>
#include <string>

ListaVuelos::ListaVuelos(){ // lea la información del archivo de texto  correspondiente.
     inicio = 0;
     char cadena[128];
     string cadena2=" ";
     string arreglo[7];
     string aux="";
     ifstream fe("Vuelos.txt");
     while (cadena2!=""){
           fe.getline(cadena,128);
           cadena2=cadena;
           if(cadena2!=""){
               for(int i=0; i<6;i++){
                       arreglo[i]=cadena2.substr(0, cadena2.find("|"));
                       cadena2=cadena2.substr(cadena2.find("|")+1,500);
               }
               arreglo[6]=cadena2;
               inserta(arreglo[0],arreglo[1],arreglo[2],arreglo[3],arreglo[4],arreglo[5],arreglo[6]);
           }
     }
}


void ListaVuelos::inserta(string codigo,string origen,string destino,string fecha,string hora,string capacidad,string cadAsientos){
     Nodo *nuevo = new Nodo();
     nuevo->codigo = codigo;
     nuevo->origen = origen;
     nuevo->destino = destino;
     nuevo->fecha = fecha;
     nuevo->hora = hora;
     nuevo->cadAsientos = cadAsientos;
     nuevo->siguiente =0;
     Nodo *aux = inicio;
     if (inicio ==0)
        inicio = nuevo;
     else{
         while(aux->siguiente!=0){
               aux=aux->siguiente;                   
         }
         aux->siguiente=nuevo;     
     }
}
             
void ListaVuelos::liberaAsiento(string codigo,string asiento){
     int pos;
     pos=atoi(asiento.substr(1,500).c_str());
     cout<<"pos:"<<pos<<endl;     
     pos=(pos*4)-1;
     if(asiento[0]=='A'){
        pos=pos-3;
     }
     if(asiento[0]=='B'){
        pos=pos-2;
     }
     if(asiento[0]=='C'){
        pos=pos-1;
     }
     //si es D el asiento es pos, el ultimo asiento de la fila
     if (inicio !=0){
        Nodo *aux = inicio;
        cout<<"asientos: "<<aux->cadAsientos<<endl;
        if (inicio->codigo == codigo){
           inicio->cadAsientos[pos]='O';
        }
        else{
             aux = aux->siguiente;
             while (aux && (aux->codigo!=codigo)){
                   aux = aux->siguiente;
             }
             if (aux !=0){
                cout<<"asientos: "<<aux->cadAsientos<<endl;
                aux->cadAsientos[pos]='O';
                cout<<"asientos: "<<aux->cadAsientos<<endl;
             }
        }
     }
} 

void ListaVuelos::despliega(){
     Nodo *aux = inicio;
     cout <<"inicio de la lista \n";
     cout<<"Vuelo-Origen-Destino-Fecha-Hora-Capacidad-Asiento\n";
     cout<<"-------------------------------------------------\n";
     if (aux){
        cout << aux->codigo << " " << aux->origen << " "<< aux->destino << " "<< aux->fecha << " "<< aux->hora << " "<< aux->capacidad<< " "<< aux->cadAsientos<<"\n";
        while (aux->siguiente!=0){
              aux = aux->siguiente;
              cout << aux->codigo << " " << aux->origen << " "<< aux->destino << " "<< aux->fecha << " "<< aux->hora << " "<< aux->capacidad<< " "<< aux->cadAsientos<<"\n";
        }
     }
     cout <<"fin de la lista \n";
}                           

