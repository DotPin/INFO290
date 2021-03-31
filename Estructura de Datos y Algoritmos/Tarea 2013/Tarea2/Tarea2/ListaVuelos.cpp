#include "ListaVuelos.h"
#include <fstream>
#include <QString>
#include <QFile>
#include <QTextStream>
#include <QDebug>

ListaVuelos::ListaVuelos(){ // lea la información del archivo de texto  correspondiente y crea la nueva lista de vuelos
     inicio = 0;//fija el nodo inicio igual a cero
     QString cadena2=" ";//creo un cadena QString para tratar la linea
     QString arreglo[7];//arreglo de QStrings con los datos separados de la linea
     QFile file("Vuelos.txt");
     if (!file.open(QIODevice::ReadOnly | QIODevice::Text))
          return;

     QTextStream in(&file);
     int largo=0;
     int pos=0;
     while (!in.atEnd()){
           cadena2 = in.readLine();
           largo=cadena2.length();
           qDebug()<<cadena2;
           for(int i=0; i<6;i++){//recorre el arreglo
                   pos=cadena2.indexOf("|");
                   arreglo[i]=cadena2.left(pos);//guardo en el posiscion i del arreglo el primer dato
                   qDebug()<<arreglo[i];
                   qDebug()<<pos;
                   cadena2=cadena2.mid(pos+1,largo-pos);//reescalo la linea
                   qDebug()<<cadena2;
           }
           arreglo[6]=cadena2;//guarda el ultimo dato en el arreglo
           qDebug()<<arreglo[5].toInt();
           inserta(arreglo[0],arreglo[1],arreglo[2],arreglo[3],arreglo[4],arreglo[5].toInt(),arreglo[6]);//crea un nuevo nodo en la lista con los datos de la line aleida
     }
     file.close();//cierra el archivo de entrada
}
void ListaVuelos::escribir(){//escribe los datos de la lista de vuelos en el archivo de salida
     QFile file("Vuelos.txt");//el archivo de salida
     if (!file.open(QIODevice::WriteOnly | QIODevice::Text))
              return;
     Nodo *aux = inicio;//puntero al nodo inicio
     QString linea="";
     QTextStream out(&file);
     while (aux!=0){//si la lista no esta vacia
           linea.append(aux->codigo);
           linea.append("|");
           linea.append(aux->origen);
           linea.append("|");
           linea.append(aux->destino);
           linea.append("|");
           linea.append(aux->fecha);
           linea.append("|");
           linea.append(aux->hora);
           linea.append("|");
           linea.append(QString::number(aux->capacidad));
           linea.append("|");
           linea.append(aux->cadAsientos);
           linea.append("\n");

           aux = aux->siguiente;//pasa el vuelo siguiente
     }
     out<<linea;//escribe los datos de cada nodo(vuelo) en el archivo de salida
     file.close(); //al terminar cierra el archivo de salida
}


void ListaVuelos::inserta(QString codigo,QString origen,QString destino,QString fecha,QString hora,int capacidad,QString cadAsientos){//inserta un nuevo nodo en la lista de vuelos con los datos ingresados
     Nodo *nuevo = new Nodo();//crea el nuevo nodo(vuelo)
     nuevo->codigo = codigo;//asigna al dato codigo el codigo recibida
     nuevo->origen = origen;//asigna al dato origen el origen recibida
     nuevo->destino = destino;//asigna al dato destino el destino recibida
     nuevo->fecha = fecha;//asigna al dato fecha la fecha recibida
     nuevo->hora = hora;//asigna al dato hora la hora ingresada
     nuevo->capacidad=capacidad;//asigna al dato capacidad la capacidad recibida
     nuevo->cadAsientos = cadAsientos;//asigna al dato cadAsientos la cdena de asientos recibida
     nuevo->siguiente =0;//la direccion del nodo siguiente es 0 o nula
     Nodo *aux = inicio;//puntero al nodo inicio
     if (inicio ==0)//si la lista esta vacia
        inicio = nuevo;//el nodo creado es guardado en el inicio
     else{//si ya tiene elementos
         while(aux->siguiente!=0){//si no estamos en el final de la lista
               aux=aux->siguiente;//avanzamos de nodo
         }
         aux->siguiente=nuevo; //encontramos el final y guardamos el nodo al final de la lista
     }
}
bool ListaVuelos::estaDisp(QString codigo, QString asiento){//devuelve verdadero si el asiento de dicho vuelo con coincidencia de codigo esta desocupado, si no falso.
     bool disponible=false;
     int pos=asiento.right(1).toInt();
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
     if (inicio !=0){
        Nodo *aux = inicio;
        if (inicio->codigo == codigo){
           if(pos <=inicio->capacidad && inicio->cadAsientos[pos]=='O'){
              disponible=true;
           }
           else{
                cout<<"Asiento invalido"<<endl;
           }
        }
        else{
             aux = aux->siguiente;
             while (aux && (aux->codigo!=codigo)){
                   aux = aux->siguiente;
             }
             if (aux !=0 && pos<=aux->capacidad ){
                if(aux->cadAsientos[pos]=='O'){
                   disponible=true;
                }
             }
             else{
                cout<<"Asiento invalido"<<endl;
             }
        }
     }
     return disponible;

}
int ListaVuelos::asientosDisp(QString codigo){//devuelve un entero con la cantidad de asientos disponibles del vuelo con coincidencia de codigo
    Nodo *aux=inicio;
    int asDisp;
     if (inicio !=0){
        Nodo *aux = inicio;
        if (inicio->codigo == codigo){
           for(int i=0;i<aux->capacidad;i++){
                    if(aux->cadAsientos[i]=='O'){
                       asDisp+=1;
                    }
           }
        }
        else{
             aux = aux->siguiente;
             while (aux && (aux->codigo!=codigo)){
                   aux = aux->siguiente;
             }
             if (aux !=0){
                for(int i=0;i<aux->capacidad;i++){
                        if(aux->cadAsientos[i]=='0'){
                           asDisp+=1;
                        }
                }
             }
        }
     }
     return asDisp;
}

void ListaVuelos::agregaFila(QString codigo){//agrega una fila de asientos desocupados a la cadena de asientos, y aumenta la capacidad del vuelo
     if (inicio !=0){
        Nodo *aux = inicio;
        if (inicio->codigo == codigo){
           inicio->capacidad+=4;
           inicio->cadAsientos=inicio->cadAsientos+"OOOO";
        }
        else{
             aux = aux->siguiente;
             while (aux && (aux->codigo!=codigo)){
                   aux = aux->siguiente;
             }
             if (aux !=0){
                aux->capacidad+=4;
                aux->cadAsientos=aux->cadAsientos+"OOOO";
             }
        }
     }

}
void ListaVuelos::ocuparAsiento(QString codigo,QString asiento){//deja ocupado un asiento libre
     int pos=asiento.right(1).toInt();
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
     if (inicio !=0){
        Nodo *aux = inicio;
        if (inicio->codigo == codigo){
           inicio->cadAsientos[pos]='X';
        }
        else{
             aux = aux->siguiente;
             while (aux && (aux->codigo!=codigo)){
                   aux = aux->siguiente;
             }
             if (aux !=0){
                aux->cadAsientos[pos]='X';
             }
        }
     }
}

void ListaVuelos::liberaAsiento(QString codigo,QString asiento){//desocupa un asiento de la cadena de asientos del vuelo
     int pos;
     pos=asiento.right(1).toInt();
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
        if (inicio->codigo == codigo){
           inicio->cadAsientos[pos]='O';
        }
        else{
             aux = aux->siguiente;
             while (aux && (aux->codigo!=codigo)){
                   aux = aux->siguiente;
             }
             if (aux !=0){
                aux->cadAsientos[pos]='O';
             }
        }
     }
}

QString ListaVuelos::despliegaAsientos(QString codigo){//despliega en salida estandar la disponibilidad de asientos como  una matriz indicando filas(numeros) y columnas(letras)
    QString salida="";
    if (inicio !=0){
        Nodo *aux = inicio;
        if (inicio->codigo == codigo){
            salida.append("    A   B   C   D\n");
            for(int j=0;j<aux->capacidad/4;j++){
                salida.append("\n"+QString::number(j+1)+"  ");
                for(int i=4*j;i<(4*j)+4;i++){
                        salida.append(aux->cadAsientos[i]+"   ");
                }
            }
            salida.append("\n");
        }
        else{
             aux = aux->siguiente;
             while (aux && (aux->codigo!=codigo)){
                   aux = aux->siguiente;
             }
             if (aux !=0){
                salida.append("    A   B   C   D\n");
                for(int j=0;j<aux->capacidad/4;j++){
                    salida.append("\n"+QString::number(j+1)+"  ");
                    for(int i=4*j;i<(4*j)+4;i++){
                            salida.append(aux->cadAsientos[i]+"   ");
                    }
                }
                salida.append("\n");
             }
        }
     }
    return salida;
}

void ListaVuelos::despliegaVuelos(){//muestra los vuelos disponibles con todos sus datos
     Nodo *aux = inicio;
     //cout <<"inicio de la lista \n";
     if (aux){
        //cout << aux->codigo << " " << aux->origen << " "<< aux->destino << " "<< aux->fecha << " "<< aux->hora << " "<< aux->capacidad<< " "<< aux->cadAsientos<<"\n";
        while (aux->siguiente!=0){
              aux = aux->siguiente;
              //cout << aux->codigo << " " << aux->origen << " "<< aux->destino << " "<< aux->fecha << " "<< aux->hora << " "<< aux->capacidad<< " "<< aux->cadAsientos<<"\n";
        }
     }
     //cout <<"fin de la lista \n";
}
QString ListaVuelos::despliegaVuelos(QString codigo){//despliega los vuelos con conicidencia de codigo ingresado
     QString esta="0";
     Nodo *aux = inicio;
     if (aux){
        if(aux->codigo.compare(codigo)==0){
            qDebug()<<"capacidad:";
             qDebug()<<aux->capacidad;
             esta=aux->codigo+","+aux->origen+","+aux->destino+","+aux->fecha+","+aux->hora+","+QString::number(aux->capacidad)+","+aux->cadAsientos+"\n";
        }
        while (aux->siguiente!=0){
              aux = aux->siguiente;
              if(aux->codigo.compare(codigo)==0){
                   esta=aux->codigo+","+aux->origen+","+aux->destino+","+aux->fecha+","+aux->hora+","+QString::number(aux->capacidad)+","+aux->cadAsientos+"\n";
              }
        }
     }
     cout <<endl;
     return esta;
}
QString ListaVuelos::despliegaVuelos(QString origen, QString destino){//despliega vuelos con coincidencia de Origen-Destino
     QString esta="0";
     Nodo *aux = inicio;
     //qDebug()<<"inicio->codigo";
     //qDebug()<<inicio->codigo;
     //cout <<"Vuelos que coinciden con su busqueda:"<<endl<<endl;
     if (aux){
        if(aux->origen==origen && aux->destino==destino){
             esta=aux->codigo+","+aux->origen+","+aux->destino+","+aux->fecha+","+aux->hora+","+QString::number(aux->capacidad)+","+aux->cadAsientos+"\n";
             //cout << aux->codigo << " " << aux->origen << " "<< aux->destino << " "<< aux->fecha << " "<< aux->hora << " "<< aux->capacidad<< " "<< aux->cadAsientos<<"\n";
             //esta=aux->codigo;
        }
        while (aux->siguiente!=0){
              aux = aux->siguiente;
              if(aux->origen==origen && aux->destino==destino){
                 esta=aux->codigo+","+aux->origen+","+aux->destino+","+aux->fecha+","+aux->hora+","+QString::number(aux->capacidad)+","+aux->cadAsientos+"\n";
                 //cout << aux->codigo << " " << aux->origen << " "<< aux->destino << " "<< aux->fecha << " "<< aux->hora << " "<< aux->capacidad<< " "<< aux->cadAsientos<<"\n";
                 //esta=aux->codigo;
              }
        }
     }
     qDebug()<<esta;
     return esta;
     cout <<endl;
}

