
import os
import mysql.connector 
from Company import Company
from Producto import Producto
 
def menu():

	
	os.system('cls') 
	print ("Selecciona una opción")
	print ("\t1 - Crear Compañia")
	print ("\t2 - Crear Cliente")
	print ("\t3 - Crear Producto")
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
		print ("")
		input("Has pulsado la opción 2...\npulsa una tecla para continuar")

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




