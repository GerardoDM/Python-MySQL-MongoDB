class CompañiaMongo:

    def __init__(self, nombre, rfc, direccion):
        self.nombre = nombre
        self.rfc = rfc
        self.direccion = direccion


    def toDBCollection (self):
        return {
            "nombre":self.nombre,
            "rfc":self.rfc,
            "direccion": self.direccion,
        }

    def __str__(self):
        return "Nombre: %s - RFC: %i - Direccion: %s" \
               %(self.nombre, self.rfc, self.direccion)