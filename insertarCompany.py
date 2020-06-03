

import mysql.connector 
from pruebaClassConexion import Conexion

# objeto = Conexion()

# objeto._connect()

def insertVariblesIntoTable(nombre, rfc, direccion):
    try:
        
        connection = mysql.connector.connect(host="localhost",database="PruebaPythonMySQL" ,user="root",password="root")
          
        cursor = connection.cursor()
        mySql_insert_query = """INSERT INTO Company (nombre_company, rfc_company, direccion_company) 
                                VALUES (%s, %s, %s) """

        

        recordTuple = (nombre, rfc, direccion)
        cursor.execute(mySql_insert_query, recordTuple)
        connection.commit()
        print("Record inserted successfully into Company table")

    except mysql.connector.Error as error:
        print("Failed to insert into MySQL table {}".format(error))

    finally:
        if (connection.is_connected()):
            cursor.close()
            connection.close()
            print("MySQL connection is closed")

nombreCompany = input('Ingrese nombre de la compañia ')
precioCompany = input('Ingrese rfc de la compañia ')
direccionCompany = input('Ingrese dirección de la compañia ')
insertVariblesIntoTable(nombreCompany, precioCompany, direccionCompany)


# array = array['uno', 'dos', 'tres']

# for x in array:

