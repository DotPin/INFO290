#include <QFile>
#include <QTextStream>
#include "ListaPasajeros.h"
#include <fstream>
#include <iostream>
#include <QString>
#include <QDebug>

ListaPasajeros::ListaPasajeros(){ // lea la información del archivo de texto  correspondiente.
     inicio = 0;//fija el inicio de la lista en cero
     QString cadena2=" ";//creo un cadena QString para tratar la linea
     QString arreglo[5];//arreglo de QStrings con los datos separados de la linea
     QFile file("Pasajeros.txt");
     int largo=0;
     int pos=0;
     if (!file.open(QIODevice::ReadOnly | QIODevice::Text))
          return;

     QTextStream in(&file);
     while (!in.atEnd()){
           cadena2=in.readLine();//transforma la cadena en QString para su correcto procesamiento
           largo=cadena2.length();
           for(int i=0; i<4;i++){//recorre el arreglo
               pos=cadena2.indexOf("|");
               arreglo[i]=cadena2.left(pos);//guardo en el posiscion i del arreglo el primer dato
               //qDebug()<<arreglo[i];
               //qDebug()<<pos;
               cadena2=cadena2.mid(pos+1,largo-pos);//reescalo la linea
               //qDebug()<<cadena2;
           }
           arreglo[4]=cadena2;//guarda el ultimo dato en el arreglo
           inserta(arreglo[0],arreglo[1],arreglo[2],arreglo[3],arreglo[4]);//crea un nuevo nodo en la lista con los datos de la line aleida
     }
     file.close();//cierra el archivo de entrada
}

void ListaPasajeros::escribir(){//escribe los datos de la lista de pasajeros en el archivo de salida
    QFile file("Pasajeros.txt");//el archivo de salida
    if (!file.open(QIODevice::WriteOnly | QIODevice::Text))
             return;
    QTextStream out(&file);
    QString linea="";
     Nodo *aux = inicio;//puntero al nodo inicio
     while (aux!=0){//si la lista no esta vacia
           linea.append(aux->codigo);
           linea.append("|");
           linea.append(aux->rut);
           linea.append("|");
           linea.append(aux->nombre);
           linea.append("|");
           linea.append(aux->apellido);
           linea.append("|");
           linea.append(aux->asiento);
           linea.append("\n");

           aux = aux->siguiente;//pasa al pasajero siguiente
     }
     out<<linea;//escribe los datos de cada nodo(pasajero) en el archivo de salida
     file.close(); //al finalizar cierro el archivo de salida
}

void ListaPasajeros::inserta(QString codigo, QString rut, QString nombre, QString apellido, QString asiento){
     Nodo *nuevo = new Nodo();
     // asignamos informacion sobre el pasajero al nuevo nodo:
     nuevo->codigo = codigo;
     nuevo->rut = rut;
     nuevo->nombre = nombre;
     nuevo->apellido = apellido;
     nuevo->asiento = asiento;
     nuevo->siguiente =0;
     Nodo *aux=inicio;
     if (inicio ==0)//si la lista esta vacia
        inicio = nuevo;//guardo e nuevo nodo en el inicio
     else{//si hay nodos
         while(aux->siguiente!=0){//mientras no estemos en el final de la lista
               aux=aux->siguiente;  //avanza de nodo
         }
         aux->siguiente=nuevo;//agrego el nuevo nodo al final de la lista
     }
}
void ListaPasajeros::cambiaAsiento(QString codigo, QString rut,QString nuevoAsiento){//cambia el asiento de un pasajero en el vuelo reservado
     Nodo *aux = inicio;
     if (aux){
        if(aux->codigo==codigo && rut==aux->rut){
             qDebug()<<"asiento antiguo:";
             qDebug()<<aux->asiento;
             aux->asiento=nuevoAsiento;
             qDebug()<<"asiento nuevo:";
             qDebug()<<aux->asiento;

        }
        else{
            while (aux->siguiente!=0){
                  aux = aux->siguiente;
                  if(aux->codigo==codigo &&rut==aux->rut){
                      qDebug()<<"asiento antiguo:";
                      qDebug()<<aux->asiento;
                      aux->asiento=nuevoAsiento;
                      qDebug()<<"asiento nuevo:";
                      qDebug()<<aux->asiento;
                  }
            }
        }
     }

}
QString ListaPasajeros::elimina(QString codigo,QString rut){//elimina un pasajero de la lista con coincidencia de codigo de vuelo y su rut
     QString asiento="0";
     if (inicio !=0){
        Nodo *aux = inicio;
        if (inicio->rut == rut && inicio->codigo==codigo){
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
             if (aux !=0 && aux->codigo==codigo){
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
     return asiento;
}

QString ListaPasajeros::despliegaPasajero(QString codigo, QString rut){//despliega en salida estandar los datos del pasaje reservado de un pasajero con coincidencia de codigo y rut
     Nodo *aux = inicio;
     QString datos="0";
     if (aux){
        if(aux->codigo==codigo && rut==aux->rut){
             //asiento=aux->asiento;
             datos="";
             datos.append("Datos del pasajero: ");
             datos.append("Nombre: ");
             datos.append(aux->nombre);
             datos.append(" ");
             datos.append("Rut: ");
             datos.append(aux->rut);
             datos.append(" ");
             datos.append("Asiento: ");
             datos.append(aux->asiento);
             datos.append("\n");
        }
        else{
            while (aux->siguiente!=0){
                  aux = aux->siguiente;
                  if(aux->codigo==codigo &&rut==aux->rut){
                     //asiento=aux->asiento;
                      datos="";
                      datos.append("Datos del pasajero: ");
                      datos.append("Nombre: ");
                      datos.append(aux->nombre);
                      datos.append(" ");
                      datos.append("Rut: ");
                      datos.append(aux->rut);
                      datos.append(" ");
                      datos.append("Asiento: ");
                      datos.append(aux->asiento);
                      datos.append("\n");
                  }
            }
        }
     }
     return datos;
}

QString ListaPasajeros::despliegaPasaVuelo(QString codigo){//despliega en salida estandar un alista de los pasajeros del vuelo con coincidencia de codigo
     Nodo *aux = inicio;
     QString salida="0";
     if (aux){
        if(aux->codigo==codigo){
            salida="";
             salida.append(aux->codigo);
             salida.append(" ");
             salida.append(aux->rut);
             salida.append(" ");
             salida.append(aux->nombre);
             for(int i=0;i<11-(aux->nombre.length());i++){
                     salida.append(" ");
             }
             salida.append(aux->apellido);
             for(int i=0;i<11-(aux->apellido.length());i++){
                     salida.append(" ");
             }
             salida.append(aux->asiento);
             salida.append("\n");
             qDebug()<<"salida;";
            qDebug()<<salida;
        }
        while (aux->siguiente!=0){
              aux = aux->siguiente;
              if(aux->codigo==codigo){
                  salida.append(aux->codigo);
                  salida.append(" ");
                  salida.append(aux->rut);
                  salida.append(" ");
                  salida.append(aux->nombre);
                 for(int i=0;i<11-aux->nombre.length();i++){
                         salida.append(" ");
                 }
                 salida.append(aux->apellido);
                 for(int i=0;i<11-aux->apellido.length();i++){
                         salida.append(" ");
                 }
                 salida.append(aux->asiento);
                 salida.append("\n");
                 qDebug()<<"salida;";
                qDebug()<<salida;
              }
        }
     }
     return salida;
}
