
"""Creremos una decorador que su principal uso es saber cuanto tarda en 
    ejecutarse una función. 
"""

from datetime import  datetime

def execution_time(func):
    def wrapper(*args, **kwargs):
        initial_func = datetime.now()
        func(*args, **kwargs)
        final_func = datetime.now()
        time_elapsed = final_func -initial_func
        print('Pasaron {} segundos'.format(time_elapsed.total_seconds()))
    return wrapper

@execution_time
def random_func():
    for _ in range(1, 1000000000):
        pass

@execution_time
def suma(a: int, b: int) -> int:
    return a + b

@execution_time
def saludo(nombre='Max'):
    return print('Hola' + nombre)


random_func()
suma(4,5)
saludo()
