import os
import mysql.connector 
from datetime import date
from Company import Company
from Producto import Producto
from Cliente import Cliente
from Compra import Compra
 
def menu():

	
	os.system('cls') 
	print ("Selecciona una opción")
	print ("\t1 - Crear Compañia")
	print ("\t2 - Crear Cliente")
	print ("\t3 - Crear Producto")
	print ("\t4 - Realizar Compra")
	print ("\t9 - salir")
 
 
while True:
	
	menu()
 
	
	opcionMenu = input("Elije una opcion : ")
 
	if opcionMenu=="1":

		company = Company()

		nombreCompany = input('Ingrese nombre de la compañia ').upper()
		precioCompany = input('Ingrese rfc de la compañia ')
		direccionCompany = input('Ingrese dirección de la compañia ')
		company.insertarCompany(nombreCompany, precioCompany, direccionCompany)
		
	elif opcionMenu=="2":

		cliente = Cliente()
		company2 = Company()
		company2.fetchCompany()

		if len(company2.companyList) == 0:
			print("No puedes crear cliente sin compañias existentes")
			input("Presiona enter para continuar")
			menu()
			

			
		else:	


			nombreCliente = input('Ingrese nombre de cliente ')
			rfcCliente = input('Ingrese rfc de cliente ')
			direccionCliente = input('Ingrese dirección de cliente ')

			print(company2.companyList)


			while True:
				
				company = input("Ingrese nombre de la compañia disponible ").upper()

				while company not in company2.companyList:
					print("No coincide con ninguna empresa, vuelve a intentar")
					company = input("Ingrese nombre de la compañia disponible ").upper()


				


				if company in company2.companyList:
					print("Excelente")
					break


			cliente.insertCliente( nombreCliente, rfcCliente, direccionCliente, company)

	elif opcionMenu=="3":
		
		product = Producto()

		nombreProducto = input("Ingrese nombre de producto: ")
		precioProducto = input("Ingrese precio de producto: ")
		product.insertarProducto(nombreProducto, precioProducto)

	elif opcionMenu=="4":
		
		compra = Compra()
		cliente = Cliente()
		cliente.fetchClientes()
		producto = Producto()
		producto.fetchProduct()

		if len(cliente.clienteList) == 0 or len(producto.productosList) == 0:
			print("No puedes realizar compras sin productos o clientes creados")
			input("Presiona enter para continuar")
			menu()
		
		else:


			print(cliente.clienteList)


			while True:
				
				clienteCompra = int(input("Ingrese ID de cliente disponible: "))

				while clienteCompra not in cliente.clienteList:
					print("No coincide con ningún ID, vuelve a intentar")
					print(cliente.clienteList)
					clienteCompra = int(input("Ingrese ID de cliente disponible: "))


				if clienteCompra in cliente.clienteList:
					print("Excelente")
					break

			print(producto.productosList)

			while True:
				
				productoCompra = int(input("Ingrese ID de producto disponible: "))

				while productoCompra not in producto.productosList:
					print("No coincide con ningún ID, vuelve a intentar")
					print(producto.productosList)
					productoCompra = int(input("Ingrese ID de producto disponible: "))


				if productoCompra in producto.productosList:
					print("Excelente")
					break

			cantidadCompra = int(input('Ingrese cantidad de la compra: '))
			precioCompra = int(input("Ingrese el precio total de la compra: "))
			fechaCompra = date.today()
			compra.insertCompra(cantidadCompra, fechaCompra, precioCompra, clienteCompra, productoCompra)

	elif opcionMenu=="9":
		break
	else:
		print ("")
		input("No has pulsado ninguna opción correcta...\npulsa una tecla para continuar")