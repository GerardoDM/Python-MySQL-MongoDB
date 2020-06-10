

from pruebaClassConexion import Conexion
import mysql.connector 


class Producto:

    def set_precio(self,precio):
        self.precio = precio

    def set_nombre(self,nombre):
        self.nombre = nombre

    def fetchProduct(self):
        try:
            productosList = []

            connection = mysql.connector.connect(host='localhost',
                                                database='PruebaPython',
                                                user='root',
                                                password='root')

            sql_select_Query = "select * from producto"
            cursor = connection.cursor()
            cursor.execute(sql_select_Query)
            records = cursor.fetchall()
            

            for row in records:

                productosList.append(row[0])

        except mysql.connector.Error as error:

            print("Error reading data from MySQL table", error)
        finally:

            if (connection.is_connected()):
                connection.close()
                cursor.close()
                print("MySQL connection is closed")

    def insertarProducto(self,nombre_producto, precio):
        try:

        
            connection = mysql.connector.connect(host="localhost",database="PruebaPython" ,user="root",password="root")
                
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
