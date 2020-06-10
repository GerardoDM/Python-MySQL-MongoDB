from pymongo import MongoClient
from CompañiaMongo import CompañiaMongo

mongoClient = MongoClient('localhost',27017)

db = mongoClient.PruebaPython

NombreCompañia = input('Ingrese nombre de compañia ')
rfcCompañia = input('Ingrese rfc de compañia ')
direccionCompañia = input('Ingrese dirección de compañia ')

document = {'NombreCompañia':NombreCompañia,'rfc':rfcCompañia,'DireccionCompañia':direccionCompañia}

_id = db ['company'].insert(document)