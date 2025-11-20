#include <cstdlib>
#include <iostream>
#include "ListaPasajeros.h"
#include "ListaVuelos.h"

using namespace std;

int main(int argc, char *argv[])
{
    ListaPasajeros *lp = new ListaPasajeros();
    lp->despliega();//desplegamos para ver si quedo todo en orden
    string asiento=lp->elimina("18432543-2");
    cout<<"asiento:"<<asiento<<endl;//eliminamos el pasajero de rut "rut" en la lista de pasajeros
    lp->despliega();//verificamos si esta eliminado
    
    ListaVuelos *lv=new ListaVuelos();
    lv->despliega();
    lv->liberaAsiento("231435",asiento);
    lv->despliega();
    
    
    system("PAUSE");
    return EXIT_SUCCESS;
}
