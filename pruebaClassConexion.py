import mysql.connector 
from mysql.connector import Error

class Conexion:

    # host = "localhost"
    # database = "PruebaPython"
    # user = "root"
    # password = "root"

    def _connect(self):
        try:
            connection = mysql.connector.connect(host="localhost",database="PruebaPython" ,user="root",password="root")

            if connection.is_connected():

                db_Info = connection.get_server_info()
                print("Connected to MySQL Server version ", db_Info)

                cursor = connection.cursor()
                cursor.execute("select database();")

                record = cursor.fetchone()
                print("You are connected to database: ", record)


  

        except Error as e:
            print("Error while connecting to MySql", e)
    
        finally:
            if (connection.is_connected()):
                 cursor.close()
                 connection.close()
                 print("MySQL connection is closed")
    