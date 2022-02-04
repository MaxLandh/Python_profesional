'''Se creara una clase la cual iterara sobre la serie fibonacci infinitamente  o topado con un maximo.
   Recordemos que la serie de Fibonacci es la suma de los ultimos dos numeros que nos dara como resultado el siguiente.
   Los dos primero numeros de Fibonacci son el 0 y el 1.
'''
import time

class FiboIter():

    def __init__(self, max=None):
        self.max = max

    def __iter__(self):
        self.n1 = 0
        self.n2 = 1
        self.counter = 0
        return self

    def __next__(self):
        if self.max == self.counter:
            raise StopIteration
        else:
            if self.counter == 0:
                self.counter += 1
                return self.n1
            elif self.counter == 1:
                self.counter += 1
                return self.n2
            else:
                self.aux = self.n1 + self.n2
                self.counter += 1
                self.n1, self.n2 = self.n2, self.aux
                return self.aux


if __name__ == '__main__':
    initializer = FiboIter()
    maxim = int(input('Type up to which Fibonacci number you want to get: '))
    initializer.max = maxim
    for element in initializer:
        print(element)
        time.sleep(1)   