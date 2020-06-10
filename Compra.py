
import mysql.connector 

class Compra:

    def insertCompra(self, cantidad, fecha, precio, cliente, producto):

        try:

            connection = mysql.connector.connect(host="localhost",database="PruebaPython" ,user="root",password="root")
            
            cursor = connection.cursor()
            mySql_insert_query = """INSERT INTO Compra (cantidad, fecha, precio, id_cliente, id_producto) 
                                    VALUES (%s, %s, %s, %s, %s) """

            

            recordTuple = (cantidad, fecha, precio, cliente, producto)
            cursor.execute(mySql_insert_query, recordTuple)
            connection.commit()
            print("Record inserted successfully into Compras table")

        except mysql.connector.Error as error:
            print("Failed to insert into Compras table {}".format(error))

        finally:
            if (connection.is_connected()):
                cursor.close()
                connection.close()
                print("MySQL connection is closed")
