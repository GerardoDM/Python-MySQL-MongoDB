

import mysql.connector 
from pruebaClassConexion import Conexion
from consolemenu import *
from consolemenu.items import *

# objeto = Conexion()

# objeto._connect()

def insertVariblesIntoTable(nombre, rfc, direccion, company):
    try:
        
        connection = mysql.connector.connect(host="localhost",database="PruebaPythonMySQL" ,user="root",password="root")
          
        cursor = connection.cursor()
        mySql_insert_query = """INSERT INTO Cliente (nombre_cliente, rfc_cliente, direccion_cliente, id_company) 
                                VALUES (%s, %s, %s, %s) """

        

        recordTuple = (nombre, rfc, direccion, company)
        cursor.execute(mySql_insert_query, recordTuple)
        connection.commit()
        print("Record inserted successfully into Cliente table")

    except mysql.connector.Error as error:
        print("Failed to insert into MySQL table {}".format(error))

    finally:
        if (connection.is_connected()):
            cursor.close()
            connection.close()
            print("MySQL connection is closed")

array = ['uno', 'dos', 'tres']

nombreCompany = input('Ingrese nombre de cliente ')
precioCompany = input('Ingrese rfc de cliente ')
direccionCompany = input('Ingrese dirección de cliente ')

array = ['UNO', 'DOS', 'TRES']
print(array)

company = input("Ingrese nombre de la compañia disponible ").upper()
print(company)

if company in array:
    print("Excelente")


insertVariblesIntoTable(nombreCompany, precioCompany, direccionCompany,company )

