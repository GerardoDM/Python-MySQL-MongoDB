
import mysql.connector 

class Cliente:

    clienteList = []


    def set_nombre(self, nombre):
        self.nombre = nombre

    def set_rfc(self, rfc):
        self.rfc = rfc
    
    def set_direccion(self,direccion):
        self.direccion = direccion

    def set_company(self, company):
        self.company = company
    
    def insertCliente(self, nombre, rfc, direccion, company):

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

    def fetchClientes(self):
        
        try:

            connection = mysql.connector.connect(host='localhost',
                                                database='PruebaPython',
                                                user='root',
                                                password='root')

            sql_select_Query = "select * from cliente"
            cursor = connection.cursor()
            cursor.execute(sql_select_Query)
            records = cursor.fetchall()
    

            for row in records:

                Cliente.clienteList.append(row[0])

        except mysql.connector.Error as error:

            print("Error reading data from MySQL table", error)
        finally:

            if (connection.is_connected()):
                connection.close()
                cursor.close()
                print("MySQL connection is closed")