
import os
 
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
		print ("")
		input("Has pulsado la opción 1...\npulsa una tecla para continuar")
	elif opcionMenu=="2":
		print ("")
		input("Has pulsado la opción 2...\npulsa una tecla para continuar")
	elif opcionMenu=="3":
		print ("")
		input("Has pulsado la opción 3...\npulsa una tecla para continuar")
	elif opcionMenu=="9":
		break
	else:
		print ("")
		input("No has pulsado ninguna opción correcta...\npulsa una tecla para continuar")




