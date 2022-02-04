''' Craremos una serie fibonacci pero con generadores.
'''

import time

def fibo_gen(max = 0):
    n1 = 0
    n2 = 1
    counter = 0
    if max == 0:
        while True:    
            if counter == 0:
                counter += 1
                yield n1
            elif counter == 1:
                counter += 1
                yield n2
            else:
                aux = n1 + n2
                n1, n2 = n2, aux
                counter += 1
                yield aux     

    else: 
        while max >counter:    
            if counter == 0:
                counter += 1
                yield n1
            elif counter == 1:
                counter += 1
                yield n2
            else:
                aux = n1 + n2
                n1, n2 = n2, aux
                counter += 1
                yield aux


if __name__ == '__main__':
    fibonacci = fibo_gen() #Se inicializa el generador, igual que como con clases.
    try:
        maxim = int(input('Type up to which Fibonacci number you want to get: '))
    except  ValueError:
        print('Please, type a number integer positive')
          
    for element in fibonacci:
        print(element)
        time.sleep(0.5)