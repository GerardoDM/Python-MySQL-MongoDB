
import os
import mysql.connector 
from Company import Company
from Producto import Producto
from Cliente import Cliente
 
def menu():

	
	os.system('cls') 
	print ("Selecciona una opción")
	print ("\t1 - Crear Compañia")
	print ("\t2 - Crear Cliente")
	print ("\t3 - Crear Producto")
	print ("\t3 - Realizar Compra")
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

	elif opcionMenu=="9":
		break
	else:
		print ("")
		input("No has pulsado ninguna opción correcta...\npulsa una tecla para continuar")




