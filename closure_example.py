"""Script para describir un closure y una nested function"""

def make_multiplier(x):
    """make_Multiplier es la función de orden superior
    que retornara la función anidada. Solicita un parametro entero"""
    
    def multiplier(n):
        return x * n #Este es el valor final
    
    return multiplier #Se retorna la función anidada

#Creamos una variable que sera igual a la función de orden superior

times10 = make_multiplier(10)

print(times10(3))

