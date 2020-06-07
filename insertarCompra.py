

from datetime import date

import mysql.connector 
from pruebaClassConexion import Conexion


def insertCompra(cantidad, fecha, precio, cliente, producto):
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


try:

    clienteList = []

    connection = mysql.connector.connect(host='localhost',
                                         database='PruebaPython',
                                         user='root',
                                         password='root')

    sql_select_Query = "select * from cliente"
    cursor = connection.cursor()
    cursor.execute(sql_select_Query)
    records = cursor.fetchall()
    

    for row in records:

        clienteList.append(row[0])

except mysql.connector.Error as error:

    print("Error reading data from MySQL table", error)
finally:

    if (connection.is_connected()):
        connection.close()
        cursor.close()
        print("MySQL connection is closed")



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


print(clienteList)


while True:
    
    clienteCompra = int(input("Ingrese ID de cliente disponible: "))

    while clienteCompra not in clienteList:
        print("No coincide con ningún ID, vuelve a intentar")
        print(clienteList)
        clienteCompra = int(input("Ingrese ID de cliente disponible: "))


    if clienteCompra in clienteList:
        print("Excelente")
        break

print(productosList)

while True:
    
    productoCompra = int(input("Ingrese ID de producto disponible: "))

    while productoCompra not in productosList:
        print("No coincide con ningún ID, vuelve a intentar")
        print(productosList)
        productoCompra = int(input("Ingrese ID de producto disponible: "))


    if productoCompra in productosList:
        print("Excelente")
        break
    
cantidadCompra = int(input('Ingrese cantidad de la compra: '))
precioCompra = int(input("Ingrese el precio total de la compra: "))
fechaCompra = date.today()
insertCompra(cantidadCompra, fechaCompra, precioCompra, clienteCompra, productoCompra)