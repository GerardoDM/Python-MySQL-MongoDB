
import mysql.connector 

class Cliente:


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