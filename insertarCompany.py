

import mysql.connector 
from pruebaClassConexion import Conexion

# objeto = Conexion()

# objeto._connect()

companyList = []

def insertVariblesIntoTable(nombre, rfc, direccion):
    try:
        
        connection = mysql.connector.connect(host="localhost",database="PruebaPython" ,user="root",password="root")
          
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

nombreCompany = input('Ingrese nombre de la compañia ').upper()
precioCompany = input('Ingrese rfc de la compañia ')
direccionCompany = input('Ingrese dirección de la compañia ')
insertVariblesIntoTable(nombreCompany, precioCompany, direccionCompany)



################################################
###############################################





try:

    connection = mysql.connector.connect(host='localhost',
                                         database='PruebaPython',
                                         user='root',
                                         password='root')

    sql_select_Query = "select * from Company"
    cursor = connection.cursor()
    cursor.execute(sql_select_Query)
    records = cursor.fetchall()
    print("Total number of rows in Laptop is: ", cursor.rowcount)

    for row in records:

        companyList.append(row[0])

        # print("Id = ", row[0], )
        # print("Name = ", row[1])
        # print("Purchase date  = ", row[2], "\n")

except mysql.connector.Error as error:

    print("Error reading data from MySQL table", error)
finally:

    if (connection.is_connected()):
        connection.close()
        cursor.close()
        print("MySQL connection is closed")





####################################################################################
####################################################################################


def insertVariablesIntoTable(nombre, rfc, direccion, company):
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

print(companyList)

while True:
    
    company = input("Ingrese nombre de la compañia disponible ").upper()

    while company not in companyList:
        print("No coincide con ninguna empresa, vuelve a intentar")
        print(companyList)
        company = input("Ingrese nombre de la compañia disponible ").upper()


    if company in companyList:
        print("Excelente")
        break
    


insertVariablesIntoTable(nombreCliente, rfcCliente , direccionCliente ,company )

