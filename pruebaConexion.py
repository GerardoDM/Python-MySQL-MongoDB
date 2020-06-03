
import mysql.connector 
from pruebaClassConexion import Conexion

# objeto = Conexion()

# objeto._connect()

def insertVariblesIntoTable(nombre_producto, precio):
    try:
        
        connection = mysql.connector.connect(host="localhost",database="PruebaPythonMySQL" ,user="root",password="root")
          
        cursor = connection.cursor()
        mySql_insert_query = """INSERT INTO Producto (nombre_producto, precio) 
                                VALUES (%s, %s) """

        

        recordTuple = (nombre_producto, precio)
        cursor.execute(mySql_insert_query, recordTuple)
        connection.commit()
        print("Record inserted successfully into Producto table")

    except mysql.connector.Error as error:
        print("Failed to insert into MySQL table {}".format(error))

    finally:
        if (connection.is_connected()):
            cursor.close()
            connection.close()
            print("MySQL connection is closed")

nombreProducto = input()
precioProducto = input()
insertVariblesIntoTable(nombreProducto, precioProducto)

