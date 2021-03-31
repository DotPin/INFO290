#!/usr/bin/python
# -*- coding: utf-8 -*-

import sqlite3


def conectar():
    con = sqlite3.connect('citasmedicas')
    con.row_factory = sqlite3.Row
    return con

#Metodos para modulo Pacientes


def obtener_pacientes():
    """Este metodo retorna 5 valores, los correspondientes a la tabla pacientes
    mas un valor extra que es la cantidad de citas que ese paciente tiene
    registrado"""

    con = conectar()
    c = con.cursor()
    query = """SELECT A.rut Rut, A.nombres Nombres, A.apellidos Apellidos,
    A.ficha_medica 'Ficha medica', count(B.paciente_rut) Citas
    FROM paciente A outer left join cita B
    on A.rut = B.paciente_rut
    group by A.rut, B.paciente_rut
    order by Nombres"""
    resultado = c.execute(query)
    pacientes = resultado.fetchall()
    con.close()
    return pacientes


def busca_paciente(rut):
    con = conectar()
    c = con.cursor()
    query = ""


def agregar_paciente(rut, nombres, apellidos, ficha_medica):
    con = conectar()
    c = con.cursor()
    query = """INSERT INTO paciente (rut, nombres, apellidos, ficha_medica)
    VALUES (?, ?, ?, ?)"""
    c.execute(query, (rut, nombres, apellidos, ficha_medica))
    con.commit()


def editar_paciente(rut, nombres, apellidos, ficha):
    con = conectar()
    c = con.cursor()
    query = """UPDATE paciente
    SET nombres = ?, apellidos = ?, ficha_medica = ?
    WHERE rut = ?"""
    c.execute(query, (nombres, apellidos, ficha, rut))
    con.commit()


def delete_paciente(rut, citas):
    """ metodo que elimina un paciente que tenga almenos 1 cita registrada"""
    exito = False
    con = conectar()
    c = con.cursor()
    query = "DELETE FROM paciente WHERE rut = ?"
    if (citas == 0):
        try:
            resultado = c.execute(query, [rut])
            con.commit()
            exito = True
        except sqlite3.Error as e:
            exito = False
            print "Error:", e.args[0]
        con.close()
    else:
        exito = False

    #print exito
    return exito


#Metodos para manejar modulo medicos

def obtener_medicos():
    """retorna los campos de la tabla medico mas la cantidad de citas
    que tiene cada medico en la tabla cita, osea, retornaria los 4 campos de
    medico mas un campo extra con la cantidad de citas que tiene
    """
    con = conectar()
    c = con.cursor()
    query = """SELECT  A.rut Rut, C.nombre Especialidad, A.nombres Nombres,
    A.apellidos Apellidos, count(B.medico_rut) citas
    FROM medico A left outer join cita B
    on A.rut = B.medico_rut  and A.especialidad_id = C.id
    inner join especialidad C
    on A.especialidad_id = C.id
    group by medico_rut, rut
    order by rut"""
    resultado = c.execute(query)
    medico = resultado.fetchall()
    con.close()
    return medico


def agregar_medico(rut, especialidad_id, nombres, apellidos):
    con = conectar()
    c = con.cursor()
    query = """INSERT INTO medico (rut, especialidad_id, nombres, apellidos)
    VALUES (?, ?, ?, ?)"""
    c.execute(query, (rut, especialidad_id, nombres, apellidos))
    con.commit()


def editar_medico(rut, especialidad_id, nombres, apellidos):
    con = conectar()
    c = con.cursor()
    query = """UPDATE medico
    SET (nombres, especialidad_id, apellidos)
    VALUES(?,?,?)
    WHERE rut = ?"""
    c.execute(query, (nombres, especialidad_id, apellidos, rut))
    con.commit()


def delete_medico(rut, citas):
    """Elimina al medico con el rut correspondiente solo si tiene
    almenos 1 cita registrada"""

    exito = False
    con = conectar()
    c = con.cursor()
    query = "DELETE FROM medico WHERE rut = ?"
    if (citas > 0):
        try:
            resultado = c.execute(query, [rut])
            con.commit()
            exito = True
        except sqlite3.Error as e:
            exito = False
            print "Error:", e.args[0]
        con.close()
    else:
        exito = False
    return exito


#Metodos para modulo Citas

def obtener_citas():
    con = conectar()
    c = con.cursor()
    query = "Select * from cita order by fecha"
    resultado = c.execute(query)
    citas = resultado.fetchall()
    con.close()
    return citas


def delete_cita(id):
    exito = False
    con = conectar()
    c = con.cursor()
    query = "DELETE FROM citas WHERE id = ?"
    try:
        resultado = c.execute(query, [id])
        con.commit()
        exito = True
    except sqlite3.Error as e:
        exito = False
        print "Error:", e.args[0]
    con.close()
    return exito

def agregar_cita(paciente_rut,medico_rut,fecha,sintomas,diagnostico,recomendaciones,receta):
    con = conectar()
    c = con.cursor()
    query = """INSERT INTO cita (paciente_rut,medico_rut,fecha,sintomas,diagnostico,recomendaciones,receta)
    VALUES  (?, ?, ?, ?)"""
    c.execute(query, (paciente_rut,medico_rut,fecha,sintomas,diagnostico,recomendaciones,receta))
    con.commit()


def editar_cita(paciente_rut,medico_rut,fecha,sintomas,diagnostico,recomendaciones,receta):
    con = conectar()
    c = con.cursor()
    query = """UPDATE cita
    SET (fecha,sintomas,diagnostico,recomendaciones,receta)
    VALUES(?,?,?)
    WHERE paciente_rut = ? AND medico_rut = ? AND fecha = ? """
    c.execute(query, (fecha,sintomas,diagnostico,recomendaciones,receta))
    con.commit()

