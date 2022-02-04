import time

class Evennumbers():
    '''Clase que itera los numeros que son pares hasta el infinito o un maximo'''

    def __init__(self, max=None):
        self.max = max
    
    def __iter__(self):
        self.num = 0
        return self
    
    def __next__(self):
        if not self.max or self.num <= self.max:
            result = self.num
            self.num += 2
            return result
        else:
            raise StopIteration


numeros = Evennumbers()
numeros.max = 10
for element in numeros:
    print(element)
    time.sleep