/****************************************************************************
** Meta object code from reading C++ file 'uachairlines.h'
**
** Created: Mon 9. Dec 13:11:04 2013
**      by: The Qt Meta Object Compiler version 63 (Qt 4.8.1)
**
** WARNING! All changes made in this file will be lost!
*****************************************************************************/

#include "../../Tarea2/uachairlines.h"
#if !defined(Q_MOC_OUTPUT_REVISION)
#error "The header file 'uachairlines.h' doesn't include <QObject>."
#elif Q_MOC_OUTPUT_REVISION != 63
#error "This file was generated using the moc from 4.8.1. It"
#error "cannot be used with the include files from this version of Qt."
#error "(The moc has changed too much.)"
#endif

QT_BEGIN_MOC_NAMESPACE
static const uint qt_meta_data_UachAirlines[] = {

 // content:
       6,       // revision
       0,       // classname
       0,    0, // classinfo
      14,   14, // methods
       0,    0, // properties
       0,    0, // enums/sets
       0,    0, // constructors
       0,       // flags
       0,       // signalCount

 // slots: signature, parameters, type, tag, flags
      14,   13,   13,   13, 0x08,
      40,   13,   13,   13, 0x08,
      50,   13,   13,   13, 0x08,
      75,   13,   13,   13, 0x08,
     102,   13,   13,   13, 0x08,
     126,   13,   13,   13, 0x08,
     152,   13,   13,   13, 0x08,
     178,   13,   13,   13, 0x08,
     204,   13,   13,   13, 0x08,
     230,   13,   13,   13, 0x08,
     256,   13,   13,   13, 0x08,
     282,   13,   13,   13, 0x08,
     308,   13,   13,   13, 0x08,
     335,   13,   13,   13, 0x08,

       0        // eod
};

static const char qt_meta_stringdata_UachAirlines[] = {
    "UachAirlines\0\0on_pushButton_3_clicked()\0"
    "iniciar()\0on_radioButton_clicked()\0"
    "on_radioButton_2_clicked()\0"
    "on_pushButton_clicked()\0"
    "on_pushButton_2_clicked()\0"
    "on_pushButton_5_clicked()\0"
    "on_pushButton_4_clicked()\0"
    "on_pushButton_6_clicked()\0"
    "on_pushButton_7_clicked()\0"
    "on_pushButton_8_clicked()\0"
    "on_pushButton_9_clicked()\0"
    "on_pushButton_10_clicked()\0"
    "on_pushButton_11_clicked()\0"
};

void UachAirlines::qt_static_metacall(QObject *_o, QMetaObject::Call _c, int _id, void **_a)
{
    if (_c == QMetaObject::InvokeMetaMethod) {
        Q_ASSERT(staticMetaObject.cast(_o));
        UachAirlines *_t = static_cast<UachAirlines *>(_o);
        switch (_id) {
        case 0: _t->on_pushButton_3_clicked(); break;
        case 1: _t->iniciar(); break;
        case 2: _t->on_radioButton_clicked(); break;
        case 3: _t->on_radioButton_2_clicked(); break;
        case 4: _t->on_pushButton_clicked(); break;
        case 5: _t->on_pushButton_2_clicked(); break;
        case 6: _t->on_pushButton_5_clicked(); break;
        case 7: _t->on_pushButton_4_clicked(); break;
        case 8: _t->on_pushButton_6_clicked(); break;
        case 9: _t->on_pushButton_7_clicked(); break;
        case 10: _t->on_pushButton_8_clicked(); break;
        case 11: _t->on_pushButton_9_clicked(); break;
        case 12: _t->on_pushButton_10_clicked(); break;
        case 13: _t->on_pushButton_11_clicked(); break;
        default: ;
        }
    }
    Q_UNUSED(_a);
}

const QMetaObjectExtraData UachAirlines::staticMetaObjectExtraData = {
    0,  qt_static_metacall 
};

const QMetaObject UachAirlines::staticMetaObject = {
    { &QMainWindow::staticMetaObject, qt_meta_stringdata_UachAirlines,
      qt_meta_data_UachAirlines, &staticMetaObjectExtraData }
};

#ifdef Q_NO_DATA_RELOCATION
const QMetaObject &UachAirlines::getStaticMetaObject() { return staticMetaObject; }
#endif //Q_NO_DATA_RELOCATION

const QMetaObject *UachAirlines::metaObject() const
{
    return QObject::d_ptr->metaObject ? QObject::d_ptr->metaObject : &staticMetaObject;
}

void *UachAirlines::qt_metacast(const char *_clname)
{
    if (!_clname) return 0;
    if (!strcmp(_clname, qt_meta_stringdata_UachAirlines))
        return static_cast<void*>(const_cast< UachAirlines*>(this));
    return QMainWindow::qt_metacast(_clname);
}

int UachAirlines::qt_metacall(QMetaObject::Call _c, int _id, void **_a)
{
    _id = QMainWindow::qt_metacall(_c, _id, _a);
    if (_id < 0)
        return _id;
    if (_c == QMetaObject::InvokeMetaMethod) {
        if (_id < 14)
            qt_static_metacall(this, _c, _id, _a);
        _id -= 14;
    }
    return _id;
}
QT_END_MOC_NAMESPACE
