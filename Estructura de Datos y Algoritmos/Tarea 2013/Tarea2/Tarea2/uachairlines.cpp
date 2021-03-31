#include "uachairlines.h"
#include "ui_uachairlines.h"
#include "ListaVuelos.h"
#include "ListaPasajeros.h"
#include <QDebug>
#include <QMessageBox>

UachAirlines::UachAirlines(QWidget *parent) :
    QMainWindow(parent),
    ui(new Ui::UachAirlines)
{
    ui->setupUi(this);
    lp = new ListaPasajeros();
    lv=new ListaVuelos();
    iniciar();
}

UachAirlines::~UachAirlines()
{
    delete ui;
}

void UachAirlines::on_radioButton_clicked()
{
    if(ui->radioButton->isChecked()){
        ui->frame->setEnabled(true);
        ui->frame_2->setEnabled(false);
    }
    else{
        ui->frame->setEnabled(false);
    }
}
void UachAirlines::on_radioButton_2_clicked()
{
    if(ui->radioButton_2->isChecked()){
        ui->frame_2->setEnabled(true);
        ui->frame->setEnabled(false);
        ui->label_2->setVisible(false);
        ui->label_2->setText("");
    }
    else{
        ui->frame_2->setEnabled(false);
    }
}
void UachAirlines::iniciar(){
    ui->frame_3->setVisible(false);
    ui->pushButton_5->setVisible(false);
    ui->pushButton_6->setVisible(false);
    ui->frame_4->setVisible(false);
    ui->pushButton_3->setVisible(false);
    ui->label_15->setVisible(false);
    ui->label_16->setVisible(false);
    ui->label_13->setVisible(false);
    ui->label_14->setVisible(false);
    ui->lineEdit_12->setVisible(false);
    ui->label_19->setVisible(false);
    ui->label_20->setVisible(false);
    ui->pushButton_8->setVisible(false);
    ui->pushButton_10->setVisible(false);
}




void UachAirlines::on_pushButton_clicked()//al presionar buscar por codigo
{
    QString linecodigo=ui->lineEdit->text();
    qDebug()<<linecodigo;
    if(linecodigo!=""){//si el lineedit no esta vacio
        QString vuelo=lv->despliegaVuelos(linecodigo);
        qDebug()<<vuelo;
        if(vuelo!="0"){//si el vuelo esta en la lista de vuelos
            QStringList info=vuelo.split(",");
            vuelo="";
            qDebug()<<vuelo[5];
            vuelo.append("Codigo:"+info[0]+"\n");
            vuelo.append("Origen:"+info[1]+"\n");
            vuelo.append("Destino:"+info[2]+"\n");
            vuelo.append("Fecha:"+info[3]+"\n");
            vuelo.append("Hora:"+info[4]+"\n");
            vuelo.append("Capacidad:"+info[5]+"\n");
            vuelo.append("Asientos:"+info[6]+"\n");
            ui->label_2->setVisible(true);

            ui->label_2->setText(vuelo);
        }
        else{
            ui->label_2->setText("Vuelo no encontrado");
        }
    }
}

void UachAirlines::on_pushButton_2_clicked()//al presionar buscar por origen destino
{
    QString origen=ui->lineEdit_2->text();
    QString destino=ui->lineEdit_3->text();
    //qDebug()<<linecodigo;
    if(origen!="" && destino!=""){//si el lineedit no esta vacio
        QString vuelo=lv->despliegaVuelos(origen,destino);
        //qDebug()<<vuelo;
        if(vuelo!="0"){//si el vuelo esta en la lista de vuelos
            QStringList info=vuelo.split(",");
            vuelo="";
            qDebug()<<vuelo[5];
            vuelo.append("Codigo:"+info[0]+"\n");
            vuelo.append("Origen:"+info[1]+"\n");
            vuelo.append("Destino:"+info[2]+"\n");
            vuelo.append("Fecha:"+info[3]+"\n");
            vuelo.append("Hora:"+info[4]+"\n");
            vuelo.append("Capacidad:"+info[5]+"\n");
            vuelo.append("Asientos:"+info[6]+"\n");

            ui->label_5->setText(vuelo);
            ui->pushButton_5->setVisible(true);
        }
        else{
            ui->label_5->setText("Vuelo no encontrado");
        }
    }
}

void UachAirlines::on_pushButton_5_clicked()//al presionar hacer reserva
{
    ui->pushButton_5->setVisible(false);
    ui->label_5->setText("");
    ui->label_5->setVisible(false);
    ui->frame_3->setVisible(true);
    ui->frame_3->setEnabled(true);
    ui->pushButton_3->setText("Guardar");
    ui->pushButton_3->setVisible(true);
    ui->frame_2->setEnabled(false);
}
void UachAirlines::on_pushButton_3_clicked()//al presionar reservar pasaje
{
    if(ui->pushButton_3->text().compare("Guardar")==0){
        QString origen=(ui->lineEdit_2->text());
        QString destino=(ui->lineEdit_3->text());
        QString codigo=lv->despliegaVuelos(origen,destino);
        codigo=codigo.left(codigo.indexOf(","));
        if(codigo.compare("0")!=0){
            ui->frame_3->setVisible(false);
            ui->pushButton_3->setText("Reservar");
            ui->label_5->setText(lv->despliegaAsientos(codigo));
            ui->label_5->setVisible(true);
            ui->frame_4->setVisible(true);

        }
        else{
            QMessageBox msgBox;
            msgBox.setText("El vuelo ingresado no existe");
            msgBox.exec();
        }
    }
    else{
        QString nombre=ui->lineEdit_4->text();
        QString apellido=ui->lineEdit_5->text();
        QString rut=ui->lineEdit_6->text();
        QString telefono=ui->lineEdit_7->text();
        QString asiento=ui->lineEdit_8->text();

        QString origen=(ui->lineEdit_2->text());
        QString destino=(ui->lineEdit_3->text());
        QString codigo=lv->despliegaVuelos(origen,destino);
        codigo=codigo.left(codigo.indexOf(","));
        if(lv->estaDisp(codigo,asiento)){
            qDebug()<<"asiento disponible";
            lv->ocuparAsiento(codigo,asiento);
            lp->inserta(codigo,rut,nombre,apellido,asiento);
            qDebug()<<"reservado";
            QMessageBox msgBox;
            msgBox.setText("Su pasaje ha sido reservado");
            msgBox.exec();
            ui->frame_3->setVisible(false);
            ui->frame_4->setVisible(false);
            ui->pushButton_3->setText("Guardar");
            ui->pushButton_3->setVisible(false);
            ui->pushButton_5->setVisible(false);
            ui->lineEdit_2->setText("");
            ui->lineEdit_3->setText("");
            ui->lineEdit_4->setText("");
            ui->lineEdit_5->setText("");
            ui->lineEdit_6->setText("");
            ui->lineEdit_7->setText("");
            ui->lineEdit_8->setText("");
            ui->label_5->setText("");

        }
        else{
            QMessageBox msgBox;
            msgBox.setText("El asiento ingresado no se encuentra disponible");
            msgBox.exec();
        }

    }
}

void UachAirlines::on_pushButton_4_clicked()
{
    QString codigo=ui->lineEdit_9->text();
    QString rut=ui->lineEdit_10->text();
    QString asientos=lv->despliegaAsientos(codigo);
    QString datospasajero=lp->despliegaPasajero(codigo,rut);
    if(asientos.compare("0")!=0 && datospasajero.compare("0")!=0){
        ui->label_15->setVisible(true);
        ui->label_16->setVisible(true);
        ui->label_14->setVisible(true);
        ui->label_13->setVisible(true);
        ui->lineEdit_12->setVisible(true);
        ui->label_15->setText(asientos);
        ui->label_16->setText(datospasajero);
        ui->pushButton_6->setVisible(true);
    }
    else{
        QMessageBox msgBox;
        msgBox.setText("Combinacion Vuelo-Pasajero invalida");
        msgBox.exec();
    }
}

void UachAirlines::on_pushButton_6_clicked()
{
    if(ui->pushButton_6->text().compare("Cambiar")==0){
        if(lv->estaDisp(ui->lineEdit_9->text(),ui->lineEdit_12->text())){
            lv->liberaAsiento(ui->lineEdit_9->text(),ui->lineEdit_12->text());
            lv->ocuparAsiento(ui->lineEdit_9->text(),ui->lineEdit_12->text());
            lp->cambiaAsiento(ui->lineEdit_9->text(),ui->lineEdit_10->text(),ui->lineEdit_12->text());
            ui->label_15->setText(lv->despliegaAsientos(ui->lineEdit_9->text()));
            QMessageBox msgBox;
            msgBox.setText("Asiento Cambiado");
            msgBox.exec();
            ui->pushButton_6->setText("Terminar");
        }
        else{
            QMessageBox msgBox;
            msgBox.setText("Asiento No disponible");
            msgBox.exec();
        }
    }
    else{
        ui->lineEdit_9->setText("");
        ui->lineEdit_10->setText("");
        ui->lineEdit_12->setVisible(false);
        ui->label_13->setVisible(false);
        ui->label_14->setVisible(false);
        ui->label_15->setVisible(false);
        ui->label_16->setVisible(false);
        ui->pushButton_6->setText("Cambiar");
        ui->pushButton_6->setVisible(false);
    }


}

void UachAirlines::on_pushButton_7_clicked()
{
    QString codigo=ui->lineEdit_11->text();
    QString rut=ui->lineEdit_13->text();
    QString asientos=lv->despliegaAsientos(codigo);
    QString datospasajero=lp->despliegaPasajero(codigo,rut);
    if(asientos.compare("0")!=0 && datospasajero.compare("0")!=0){
        ui->label_19->setText(datospasajero);
        ui->label_19->setVisible(true);
        ui->label_20->setVisible(true);
        ui->pushButton_8->setVisible(true);
    }
    else{
        QMessageBox msgBox;
        msgBox.setText("Conbinacion Vuelo-Pasajero invalida");
        msgBox.exec();
    }
}

void UachAirlines::on_pushButton_8_clicked()
{
    QString codigo=ui->lineEdit_11->text();
    QString rut=ui->lineEdit_13->text();
    QString asiento=lp->elimina(codigo,rut);
    lv->liberaAsiento(codigo,asiento);
    QMessageBox msgBox;
    msgBox.setText("Pasaje eliminado");
    msgBox.exec();
    ui->lineEdit_11->setText("");
    ui->lineEdit_13->setText("");
    ui->label_19->setText("");
    ui->label_19->setVisible(false);
    ui->label_20->setVisible(false);
    ui->pushButton_8->setVisible(false);
}

void UachAirlines::on_pushButton_9_clicked()
{
    QString codigo=ui->lineEdit_14->text();
    qDebug()<<"codigo ingresado";
    QString pasajeros=lp->despliegaPasaVuelo(codigo);
    if(pasajeros.compare("0")!=0){
        ui->label_22->setText("Codigo    Rut      Nombre   Apellido  Asiento\n"+pasajeros);
        ui->pushButton_10->setVisible(true);
    }
    else{
        QMessageBox msgBox;
        msgBox.setText("El vuelo ingresado no existe");
        msgBox.exec();
    }
}

void UachAirlines::on_pushButton_10_clicked()
{
       ui->pushButton_10->setVisible(false);
       ui->label_22->setText("");
       ui->label_22->setVisible("");
}

void UachAirlines::on_pushButton_11_clicked()
{
    lv->escribir();
    lp->escribir();
}
