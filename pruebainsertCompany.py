
import mysql.connector 

from Company import Company

company = Company()

nombreCompany = input('Ingrese nombre de la compañia ').upper()
precioCompany = input('Ingrese rfc de la compañia ')
direccionCompany = input('Ingrese dirección de la compañia ')
company.insertarCompany(nombreCompany, precioCompany, direccionCompany)