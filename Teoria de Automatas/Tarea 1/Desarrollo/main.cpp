#include <cstdlib>
#include <iostream>
#include <stdio.h>
#include <string>
#include <vector>
#include <sstream>
#include "Pila.h"
#include "Lista.h"
#include "ListaDoble.h"

using namespace std;

void estadoFinal(Lista *palabra, ListaDoble *Transiciones, Pila *stack, string fin);
void estackVacio(Lista *palabra, ListaDoble *Transiciones, Pila *stack);

vector<string> split(string str, char delimiter) {
  vector<string> internal;
  stringstream ss(str); // Turn the string into a stream.
  string tok;
  while(getline(ss, tok, delimiter)) {
    internal.push_back(tok);
  } 
  return internal;
}

int main(int argc, char *argv[])
{
	string inicial, final;
	string modo;
	string trans;
	bool continua = true;
	string respuesta;
	cout << "Bienvenido\n";
	//creo los elementos
	ListaDoble *Transiciones = new ListaDoble();
	Lista *palabra = new Lista();
	Pila *stack = new Pila();
	//agrego R al stack
	stack->inserta("R");
	
	/*Transiciones->inserta("q0","a","R","q1","AR");
    Transiciones->inserta("q1","a","A","q2","AA");
    Transiciones->inserta("q2","a","A","q2","AA");
    Transiciones->inserta("q2","b","A","q3","E");
    Transiciones->inserta("q3","b","A","q3","E");
    Transiciones->inserta("q3","E","A","qF","A");*/

    /*Transiciones->inserta("q1","a","R","q1","AR");
    Transiciones->inserta("q1","a","A","q1","AA");
    Transiciones->inserta("q1","b","A","q2","E");
    Transiciones->inserta("q2","b","A","q2","E");
    Transiciones->inserta("q2","E","R","q2","E");
    cout<<"---------Transiciones-------------\n";
    Transiciones->despliega();
    Transiciones->eliminarTodo();
    cout << "------elimine---------\n";
    Transiciones->despliega();
    
   // Lista *palabra = new Lista();
    palabra->inserta("q1","a");
    palabra->inserta("q0","a");
    palabra->inserta("q1","a");
    palabra->inserta("q1","a");
    palabra->inserta("q1","b");
    palabra->inserta("q1","b");
    palabra->inserta("q1","b");
    palabra->inserta("q1","E");
    palabra->inserta("q1","E");
    palabra->despliega();
    cout <<"elimino la palabra \n";
    palabra->eliminarLista();
    cout<<"elimine ahora imprimo palabra \n";
    palabra->despliega();
    cout<<"la mostre"<<endl;
    
    //Pila *stack = new Pila();
    //stack->inserta("R");
    cout << stack->despliega_Tope()<<endl;
    cout <<"=============================== \n";*/
	
	while(continua){
		cout << "ingrese estado inicial: \n";
		cin >> inicial;
		system("CLS");
		cout << "Su APD acepta por estado final (F) o stack vacio (V) ??? \n";
		cin >> modo;
		system("CLS");
		while((modo!="F") && (modo!="V")){
			cout<<"ERROR AL INGRESAR \n";
			system("PAUSE");
			system("CLS");
			cout << "Su APD acepta por estado final (F) o stack vacio (V) ??? \n";
			cin >> modo;
		}
		
		if(modo=="F"){
			cout << "Cual es su estado Final? \n";
			cin >>final;
			system("CLS");
		}
		cout << "Ahora ingrese transiciones\n";
		cout << "estas son separadas por coma, por ejemplo, la siguiente transicion \n";
		cout << "(q0, a, R)=(q1, AR)   se ingresa: \n";
		cout << "q0,a,R,q1,AR \n";
		cout << "para dejar de ingresar escriba 'fin' \n";
		cout << "NOTA: para ingresar simbolo 'epsilon' ingrese 'E' (mayuscula) \n";
		cout << "ingrese transicion \n";
		cin >> trans;
		system("CLS");
		while (trans != "fin"){
			vector<string> transi =split(trans, ',');
			if(transi.size() == 5){
				Transiciones->inserta(transi[0], transi[1], transi[2], transi[3], transi[4]);				
			}
			else {
				cout <<"ERROR AL ESCRIBIR LA TRANSICION \n";
			}
			cout << "Ahora ingrese transiciones\n";
			cout << "estas son separadas por coma, por ejemplo, la siguiente transicion \n";
			cout << "(q0, a, R)=(q1, AR)   se ingresa: \n";
			cout << "q0,a,R,q1,AR \n";
			cout << "para dejar de ingresar escriba 'fin' \n";
			cout << "NOTA: para ingresar simbolo 'epsilon' ingrese 'E' (mayuscula) \n";
			cout << "ingrese transicion \n";
			cin >> trans;
			system("CLS");
		}
		cout << "sus transiciones son : \n";
		Transiciones->despliega();
		
		
		cout <<"sus transiciones estan correctas? ingrese 'no' para modificar, cualquier cosa para continuar \n";
		cin >> respuesta;
		 while(respuesta =="no"){
		 	system("CLS");
		 	cout << "sus transiciones son : \n";
			Transiciones->despliega();
		 	cout << "desea 'agregar' o 'eliminar' transiciones? \n";
		 	string des;
		 	cin >> des;
		 	if (des == "agregar"){
		 		system("CLS");
		 		cout << "sus transiciones son : \n";
				Transiciones->despliega();
		 		cout << "para dejar de ingresar escriba 'fin' \n";
				cout << "ingrese transicion \n";
				cin >> trans;
				system("CLS");
				while (trans != "fin"){
					vector<string> transi =split(trans, ',');
					if(transi.size() == 5){
						Transiciones->inserta(transi[0], transi[1], transi[2], transi[3], transi[4]);				
					}
					else {
						system("CLS");
						cout <<"ERROR AL ESCRIBIR LA TRANSICION \n";
						system("PAUSE");
					}
				system("CLS");
				cout << "sus transiciones son : \n";
				Transiciones->despliega();
				cout << "ingrese transicion \n";
				cin >> trans;
				system("CLS");
				}
			}
			
			
			if (des=="eliminar"){
				system("CLS");
				cout << "sus transiciones son : \n";
				Transiciones->despliega();
				cout << "ingrese transicion a eliminar \n";
				cout << "para eliminar solo ingrese los 3 primeros elementos \n";
				cout << "si desea eliminar la transicion (q0, a, R)=(q1, AR) \n";
				cout << "solo ingrese q0,a,R \n";
				cout << "para dejar de eliminar ingrese 'fin' \n";
				cin >> trans;
				system("CLS");
				while (trans != "fin"){
					vector<string> transi =split(trans, ',');
					if(transi.size() == 3 && (Transiciones->buscaEstado(transi[0], transi[1], transi[2]) !="ERROR" )){
						Transiciones->elimina(transi[0], transi[1], transi[2]);				
					}
					else {
						system("CLS");
						cout <<"ERROR AL ESCRIBIR LA TRANSICION \n";
						system("PAUSE");
					}
				system("CLS");
				cout << "sus transiciones son : \n";
				Transiciones->despliega();	
				cout << "ingrese transicion \n";
				cin >> trans;
				system("CLS");
				
				}		
			}
			cout << "sus transiciones son : \n";
			Transiciones->despliega();
			cout <<"sus transiciones estan correctas? ingrese 'no' para modificar, cualquier cosa para continuar \n";
			cin >> respuesta;	
		}
		
		system("CLS");
		cout << "Para ingresar palabra, debe hacerlo caracter a caracter \n";
		cout << "por ejemplo para ingresar la palabra 'aab', \n";
		cout << "debe ingresar 'a' y presione la tecla 'Enter', \n";
		cout << "luego 'a' y tecla 'Enter', y finalmente 'b' y tecla 'Enter' \n";
		cout << "Ingrese caracter, escriba 'fin' para finalizar \n";
		string pal="";
		cin >> pal;
		bool repetir = true;
		while(repetir){
			while (pal!="fin"){
				//cout<<"ingrese al while de la palabra\n";
				if(pal.length()==1 && pal!="fin"){
					palabra->inserta(inicial,pal);
				}
				else{
					system("CLS");
					cout << "ERROR, DEBE INGRESAR SOLO 1 CARACTER \n";
					system("PAUSE");
				}
				
				//system("CLS");
				cout << "su palabra es: \n";
				palabra->despliega();
				cout << "Ingrese caracter, escriba 'fin' para finalizar \n";
				cin >> pal;
					
			}
			
			system("CLS");
			//cout<<"sali del while de la palabra \n";
			cout << "su palabra es: \n";
			palabra->despliega();
			palabra->inserta(inicial,"E");
			palabra->inserta(inicial,"E");
			cout << "sus transiciones son: \n";
			Transiciones->despliega();
			cout << "su modo es "<<modo<<"\n";
			pal="fin";
			
			if(pal=="fin"){
					if (modo == "F"){
						estadoFinal(palabra, Transiciones, stack, final);
					}
					if (modo == "V"){
						estackVacio(palabra, Transiciones, stack);
					}
				}
			system("PAUSE");
			string otra;
			cout <<"Desea intentar con otra palabra? 'si' o 'no' \n";
			cin >> otra;
			while (otra!="si" && otra!="no"){
				system("CLS");
				cout << "Debe ingresar 'si' o 'no' \n";
				cout <<"Desea intentar con otra palabra? 'si' o 'no' \n";
				cin >> otra;
			}
			if(otra=="si"){
				cout<<"SU MODO ES "<<modo<<" \n";
				system("CLS");
				palabra->eliminarLista();
				stack->eliminarTodo();
				stack->inserta("R");
				cout << "Ingrese caracter, escriba 'fin' para finalizar \n";
				cin >> pal;
			}
			if (otra == "no"){
				system("CLS");
				string continuar;
				cout << "Desea 'reiniciar' el programa o 'finalizar' \n";
				cin >> continuar;
				if(continuar=="reiniciar"){
					palabra->eliminarLista();
					Transiciones->eliminarTodo();
					stack->eliminarTodo();
					stack->inserta("R");
					repetir = false;
					
				}
				if(continuar == "finalizar"){
					palabra->eliminarLista();
					Transiciones->eliminarTodo();
					stack->eliminarTodo();
					stack->inserta("R");
					repetir=false;
					continua=false;
				}
				
			}
			//system("PAUSE");
		}
	}

	
	//system("CLS");
	cout << "antes de terminar estoy aqui \n";
    system("PAUSE");   
    
}
void estadoFinal(Lista *palabra, ListaDoble *Transiciones, Pila *stack, string fin){
	string lectEst, lectSimb, stak, sig, escr;

   	//datos de palabra
   	lectSimb=palabra->lecturaSimb();
   	lectEst=palabra->lecturaEst();
   	cout<<"el estado es "<<lectEst<<"\n";
   	sig="q0";
   	while(sig!=fin && sig!="ERROR"){
   		//cout<<"entre al while\n";
   		lectSimb=palabra->lecturaSimb();
   		lectEst=palabra->lecturaEst();
   		stak=stack->despliega_Tope();
   		//cout<<lectEst<<","<<lectSimb<<","<<stak<<"<-----imprimo los datos a buscar\n";
   		
   		//busco esos datos en mis transiciones
   		sig = Transiciones->buscaEstado(lectEst, lectSimb, stak);
   		escr = Transiciones->buscaEscribe(lectEst, lectSimb, stak);
   		//cout<<"el resultado de la busqueda es : "<<sig<<","<<escr<<"\n";
   		//muevo trabajando
		palabra->mueveTrab(sig);
		stack->trabajaStack(escr,stack);
	   }
	if(sig==fin){
		cout<<"acepto la palabra\n";
	}
	
	if(sig=="ERROR"){
		cout<<"palabra rechazada\n";
	}
}

void estackVacio(Lista *palabra, ListaDoble *Transiciones, Pila *stack){
	string lectEst, lectSimb, stak, sig, escr;

   	//datos de palabra
   	lectSimb=palabra->lecturaSimb();
   	lectEst=palabra->lecturaEst();
   	//cout<<"el estado es "<<lectEst<<"\n";
   	sig="asd";
   	while(sig!="ERROR" && (stack->despliega_Tope()!="E")){
   		cout<<"entre al while\n";
   		lectSimb=palabra->lecturaSimb();
   		lectEst=palabra->lecturaEst();
   		stak=stack->despliega_Tope();
   		cout<<lectEst<<","<<lectSimb<<","<<stak<<"<-----imprimo los datos a buscar\n";
   		
   		//busco esos datos en mis transiciones
   		sig = Transiciones->buscaEstado(lectEst, lectSimb, stak);
   		escr = Transiciones->buscaEscribe(lectEst, lectSimb, stak);
   		cout<<"el resultado de la busqueda es : "<<sig<<","<<escr<<"\n";
   		//muevo trabajando
		palabra->mueveTrab(sig);
		stack->trabajaStack(escr,stack);
	   }
	//cout<<palabra->compruebaFinal()<<"<---- veo si estoy en el final \n";  
	if((stack->despliega_Tope()=="E")&& (palabra->compruebaFinal() == "final")){
		cout<<"acepto la palabra\n";
	}
	
	if(sig=="ERROR" || (stack->despliega_Tope()!="E")){
		cout<<"palabra rechazada\n";
	}
}
