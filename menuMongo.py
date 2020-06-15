import os
from datetime import date
from Producto import Producto
from Cliente import Cliente
from Compra import Compra

from pymongo import MongoClient
from CompañiaMongo import CompañiaMongo

mongoClient = MongoClient('localhost', 27017)

db = mongoClient.PruebaPython
collectionCompany = db['company']

def menu():

    os.system('cls')
    print("Selecciona una opción")
    print("\t1 - Crear Compañia")
    print("\t2 - Crear Cliente")
    print("\t3 - Crear Producto")
    print("\t4 - Realizar Compra")
    print("\t9 - salir")


while True:

    menu()

    opcionMenu = input("Elije una opcion : ")

    if opcionMenu == "1":

        nombreCompany = input('Ingrese nombre de la compañia ').upper()
        rfcCompany = input('Ingrese rfc de la compañia ')
        direccionCompany = input('Ingrese dirección de la compañia ')

        company = CompañiaMongo
        documentCompany = {'Nombre_Company': nombreCompany,
                           'RFC_Company': rfcCompany, 'Direccion_Company': direccionCompany}
        _id = collectionCompany.insert(documentCompany)

    elif opcionMenu == "2":

        nombreCliente = input('Ingrese nombre de cliente ')
        rfcCliente = input('Ingrese rfc de cliente ')
        direccionCliente = input('Ingrese dirección de cliente ')

        documentCliente = {'Nombre_Cliente': nombreCliente,
                           'RFC_Cliente': rfcCliente, 'Direccion_Cliente': direccionCliente}

        _id = db['cliente'].insert(documentCliente)

        results = collectionCompany.find()
        for r in results:
            print(r['Nombre_Company'])
        
        while True:

            company = input("Ingrese nombre de la compañia disponible ").upper()

            es = collectionCompany.find({'Nombre_Company': company})
            for e in es:
                print(e)
                
            if company in es:
                print("Excelente")
            else:
                print("No coincide con ninguna empresa, vuelve a intentar")
                company = input(
                    "Ingrese nombre de la compañia disponible ").upper()

            

    elif opcionMenu == "2":

        product = Producto()

        nombreProducto = input("Ingrese nombre de producto: ")
        precioProducto = input("Ingrese precio de producto: ")

        documentProducto = {'Nombre_producto': nombreProducto,
                            'Precio_producto': precioProducto}
        _id = db['producto'].insert(documentProducto)

    elif opcionMenu == "4":

        # compra = Compra()
        # cliente = Cliente()
        # cliente.fetchClientes()
        # producto = Producto()
        # producto.fetchProduct()

        # print(cliente.clienteList)

        # while True:

        #     clienteCompra = int(input("Ingrese ID de cliente disponible: "))

        #     while clienteCompra not in cliente.clienteList:
        #         print("No coincide con ningún ID, vuelve a intentar")
        #         print(cliente.clienteList)
        #         clienteCompra = int(
        #             input("Ingrese ID de cliente disponible: "))

        #     if clienteCompra in cliente.clienteList:
        #         print("Excelente")
        #         break

        # print(producto.productosList)

        # while True:

        #     productoCompra = int(input("Ingrese ID de producto disponible: "))

        #     while productoCompra not in producto.productosList:
        #         print("No coincide con ningún ID, vuelve a intentar")
        #         print(producto.productosList)
        #         productoCompra = int(
        #             input("Ingrese ID de producto disponible: "))

        #     if productoCompra in producto.productosList:
        #         print("Excelente")
        #         break

        cantidadCompra = int(input('Ingrese cantidad de la compra: '))
        precioCompra = int(input("Ingrese el precio total de la compra: "))
        fechaCompra = date.today()

        documentCompra = {'Cantidad_compra': cantidadCompra,
                          'Precio_compra': precioCompra, 'Fecha': fechaCompra}
        _id = db['compra'].insert(documentCompra)

    elif opcionMenu == "9":
        break
    else:
        print("")
        input("No has pulsado ninguna opción correcta...\npulsa una tecla para continuar")
