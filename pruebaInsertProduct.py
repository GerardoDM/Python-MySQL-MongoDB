

import mysql.connector 

from Producto import Producto

product = Producto()

nombreProducto = input("Ingrese nombre de producto: ")
precioProducto = input("Ingrese precio de producto: ")
product.insertarProducto(nombreProducto, precioProducto)