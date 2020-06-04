

import mysql.connector 
from pruebaClassConexion import Conexion

def insertVariblesIntoTable(nombre, rfc, direccion, company):
    try:
        
        connection = mysql.connector.connect(host="localhost",database="PruebaPython" ,user="root",password="root")
          
        cursor = connection.cursor()
        mySql_insert_query = """INSERT INTO Cliente (nombre_cliente, rfc_cliente, direccion_cliente, nombre_company) 
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



nombreCliente = input('Ingrese nombre de cliente ')
rfcCliente = input('Ingrese rfc de cliente ')
direccionCliente = input('Ingrese dirección de cliente ')


companyList = ["UNO", "dos", "TRES"]

while True:
    
    company = input("Ingrese nombre de la compañia disponible ").upper()

    while company not in companyList:
        print("No coincide con ninguna empresa, vuelve a intentar")
        company = input("Ingrese nombre de la compañia disponible ").upper()


    if company in companyList:
        print("Excelente")
        break
    


insertVariblesIntoTable(nombreCliente, rfcCliente , direccionCliente ,company )

