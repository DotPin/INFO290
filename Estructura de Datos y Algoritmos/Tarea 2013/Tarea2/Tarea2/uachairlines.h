#ifndef UACHAIRLINES_H
#define UACHAIRLINES_H

#include <QMainWindow>
#include "ListaVuelos.h"
#include "ListaPasajeros.h"

namespace Ui {
class UachAirlines;
}

class UachAirlines : public QMainWindow
{
    Q_OBJECT
    
public:
    explicit UachAirlines(QWidget *parent = 0);
    ~UachAirlines();
    
private slots:

    void on_pushButton_3_clicked();
    void iniciar();
    void on_radioButton_clicked();

    void on_radioButton_2_clicked();

    void on_pushButton_clicked();

    void on_pushButton_2_clicked();

    void on_pushButton_5_clicked();

    void on_pushButton_4_clicked();

    void on_pushButton_6_clicked();

    void on_pushButton_7_clicked();

    void on_pushButton_8_clicked();

    void on_pushButton_9_clicked();

    void on_pushButton_10_clicked();

    void on_pushButton_11_clicked();

private:
    Ui::UachAirlines *ui;
    ListaPasajeros *lp;//gurada la lista de pasajeros con los datos del txt
    ListaVuelos *lv;//gurada la lista de vuelos con los datos del txt
};

#endif // UACHAIRLINES_H
