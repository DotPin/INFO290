import csv
import sqlite3

q = []

def conectar():
    con = sqlite3.connect('redes')
    con.row_factory = sqlite3.Row
    return con
 
def agregar_red(canal, poder, nombre, archivo):
    con = conectar()
    c = con.cursor()
    query = """INSERT INTO redes (channel, power, ESSID, file)
    VALUES (?, ?, ?, ?)"""
    c.execute(query, (canal, poder, nombre, archivo))
    con.commit()

#select * from redes;
#delete from redes;
#INSERT INTO redes (channel, power, ESSID, FILE) VALUES (1, -56, "prueba", "SOLO");
with open('redes2.csv') as File:
    reader = csv.reader(File, delimiter=',', quotechar=',',
                        quoting=csv.QUOTE_MINIMAL)
    for row in reader:
        a = row[6].split(" ")
        print row
        agregar_red(int(row[0]),int(row[5]),str(a[1]), str(row[7]))
        
        