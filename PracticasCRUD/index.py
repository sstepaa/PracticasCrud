import sqlite3
from facultades import Facultad 


def createTable():
    #Crea la conexion a la base de datos universidad.db
    conn = sqlite3.connect('universidad.db')
    #Crear un objeto cursor para tirar las querys
    curr = conn.cursor()    
    #Esta consulta va a crear una tabla facultad
    curr.execute(""" CREATE TABLE IF NOT EXISTS Facultad(
        nroFacultad REAL PRIMARY KEY ,
        nombre TEXT NOT NULL, 
        domicilioSede TEXT
    ) """)
    #Esta consulta va a crear una tabla facultad
    #Cerrar la conexion.
    conn.close()

def insertFaccultad(facultad):
    conn = sqlite3.connect('universidad.db')
    curr = conn.cursor()
    curr.execute("INSERT INTO Facultad VALUES (? , ? , ?)" , (facultad.nroFacultad , facultad.nombre , facultad.domicilioSede))
    conn.commit()#Guardo los cambios
    conn.close()#Cierro la conexion
    
    
fac_1 = Facultad(2,'Universidad Palermo' , 'Maria Bravo')
fac_2 = Facultad(3 , 'San Diego' , 'Elcano')
fac_3 = Facultad(4 , 'San Pedro' , 'Dorrego')
fac_4 = Facultad(5 , 'La Matanza' , 'La matanza')
many_facultades = [
    (fac_1.nroFacultad , fac_1.nombre , fac_1.domicilioSede) , 
    (fac_2.nroFacultad , fac_2.nombre , fac_2.domicilioSede) ,
    (fac_3.nroFacultad , fac_3.nombre , fac_3.domicilioSede) 
]



insertFaccultad(fac_4)#Inserto mediante la funcion la tupla de la facultad nueva.1
