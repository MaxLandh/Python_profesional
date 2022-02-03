"""Ejemplificaremos el uso de Decordores.
   Supongamos que tenemos una función la cual se le pasara un nombre propio
   la cual retornara el mensaje: nombre_propio, recibiste un mensaje.

    Pero queremos que ese mensaje se esciba en mayusculas sin modificar la función creada.
    Para esto usaremos los decoradores. Primero ocuparemos el concepto de closure.
"""
def mayusculas(func):
    def envoltura(texto):
        return func(texto).upper()
    return envoltura

@mayusculas
def mensaje(nombre: str) -> str:
    return '{}, recibiste un mensaje'.format(nombre)

if __name__ == '__main__':
    print(mensaje('max'))
