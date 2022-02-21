# Python profesional

## Lenguajes de programación compilados e interpretados

Compilados: son los lenguajes que se comunican directamente con la computadora a lenguaje binario. Un ejemplo de lenguaje compilado es C++.

Interpretados: A diferencia de un lenguaje compilado. Este lenguaje pasa a un paso intermedio que tiene instrucciones legibles que se denominan byte code. El byte code es un lenguaje especial de más bajo nivel de Python que puede ser leído por un intérprete.

### Garbage collector

En Python tiene una sección especial que cada vez que vamos escribiendo código y definiendo objetos o variables estos a la vez se van desechando cuando Python detecta que no se están utilizando más en el código.

### Que es la carpeta __pycache__?

Esta carpeta se crea cada que corremos nuestro código en la dirección principal del código. Ahí se guarda el byte code, es ese código intermedio que crea Python, para que pueda ser leído por la maquina virtual. ¿Cuál es la ventaja de tener esta carpeta en nuestros proyectos? Funciona como una especie de recuperación del código que ya hemos trabajado.

### Modulo

Es cualquier archivo de Python. Generalmente, contiende código que puedes reutilizar.

### Paquete

Un paquete es una carpeta que contiene módulos. Siempre posee el archivo __init__.py


## Tipados (estático, dinámico, débil y fuerte)

En los lenguajes de programación existen 4 tipos de tipados: estático, dinámico, débil y fuerte.

### Static (estático)

Los lenguajes de tipado estático son los que levantan los errores de tipo en tiempo de compilación.

### Dynamic (dinámico)

Los lenguajes de tipado dinámico son los que levantan los errores de tipo tiempo de ejecución.

### Strong and Weak

No hay un consenso en la comunidad sobre las diferencias entre un lenguaje programación fuerte o débil. Pero para conveniencia de este curso definiremos que un lenguaje de programación de tipado fuerte son los que tratan con más severidad a los diferentes tipos de datos. Y los lenguajes de tipado débil son los que tratan con menos severidad a estos tipos de datos.

## Tipado estático en Python

Python es un lenguaje de tipado dinamico fuerte. Para poder definir las variables y su tipo al momento de programar, se realiza con la sintaxis de dos puntos seguido por su tipo

Ejemplo

> numero: int = 5

> cadena: str = "Hola mundo"

Para estructuras de datos complejas como diccionarios, listas o tuplas necesitaremos importar la clase Dict, List, Tuple del modulo typing

```
from typing import Dict, List, Tuple
lista: List = []
diccionario: Dict = {}
tupla: Tuple = ()
```

Para definir el tipo de valor que retornara una función se logra con la sintaxis de ->. Veamos

> def function() -> type:

Las ventajas de convertir a Python sus variables en estáticas es mas claridad a la hora de escribir código. Saber en donde se encuentran los errores y que sea entendible para más programadores
.
Ahora para que esta definición de tipos sea tomada enserio por Python hay que agregar algo mas que solo la sintaxis. Para esto es necesaria otro modulo que no esta en el core de Python, mypy.

## Mypy

En Python existe la libreria mype que nos permite hacer una examinación del código que estamos correindo. Donde nos lanzara los errores de tipo.
En consola se colocaria la siguiente sintaxis:

> mypy [name_file_py] --check-untyped-defs

## Scope

Cuando hablamos de scope en un lenguaje de programación nos referimos al alcance que pueden tener las variables i.e. hacia donde va una variable cuando la escribimos en nuetro programa y hasta donde llega. 

> **Una variable solo esta disponible dentro de la región donde fue creada**

### Local Scope

El local scope es la región que se corresponde al ámbito de una función  en donde vive una o mas variables.

### Global Scope 

El globlal scope son las variables que van a tener un alcance en todo nuestro programa.

Podemos tener dentro de un bloque de código una variable local a una variable global con el keyword **global**


## Nested Functions

Son funciones que son creadas dentro de otra función.

## Closure

Un closure es cuando una variable de Scope superior es recordada y aunque se elimine ese scope superior aun se puede acceder a esa variable mediante un scope inferior.

Para poder identificar un closure es lo siguiente:

* Debemos tener una nested function
* La nested function debe referenciar un valor de un scope superior.
* La función que envuelve a la nested function debe retornarla también.

```
def main():
    a = 1
    def nested():
        print(a)
    
    return nested

my_func = main()
my_func()
```


## ¿Donde aparecen los closures?

Aparecen cuando se tenga una clase que solo tenga un método y este se vuelva mas elegante.

Tambiém aparecen en los decoradores.

## Decoradores

Un decorador es una función que recibe como parámetro otra función, le añade cosas, la ejecuta y retorna una función diferente. Es una función que le da super poderes a otra función.

```
def decorador(func):
    def wrapper():
        print("Esto se añade a mi función original")
        func()
    return wrapper

@decorador
def saludo():
    print("Hola")

saludo()
```


## Estructura de datos avanzada

### Iteradores

Los iteradores son una estructura avanzada de datos, para entender de que se tratan los iteradores hay que entender que son los iterables. Los iterables son básicamente todos los objetos que nosotros podemos recorrer con un ciclo.

Un iterable común es una lista, una cadena de texto y hasta un diccionario.

Los iterables son aquellas estructuras de datos divisibles en elementos únicos que podemos recorrer en un ciclo.

Pero lo que sucede cuando, por ejemplo, pasamos por un ciclo una lista de objetos para que pueda ser iterado primero Python debe convertir a la lista en un **iterador**. Es el iterador el que si puede recorrerse dentro del lenguaje.

```
# Creando un iterador

my_list =[1,2,3,4,5]
my_iter = iter(my_list)

# Iterando un iterador

print(next(my_iter))

# Cuando no quedan datos, la excepción StopIteration es elevada

```
Lo que vemos en el ejemplo es que el objeto lista se convierte en un iterable con la función built-in ***iter*** y puede ser iterable con la función interna de Python de next.

Ahora, si queremos crear un iterador desde cero necesitamos crear una clase y dentro de la clase tener dos metodos principales. El método  ```__iter__``` y el método  ```__next__```.


```
class Evennumbers():

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


```

## Generadores 

Hemos visto que crear un iterador desde cero es complicado. Tenemos que usar programación orientada a objetos, usar los doonder de iter y next. Utilizar métodos y atributos. Esto lo sabe Python. Entonces nos da una herramienta útil para estos casos, los **generadores**

Los **generadores** son funciones que guardan un estado. Pero antes de que entremos a su definición más clara, hay que verla como la sintax sugar de los iteradores.

Veamos un ejemplo:

```
def my_gen():

    print("Hello world")
    n = 0 
    yield n

    print("Hello heaven")
    n = 1 
    yield n

    print("Hello hell")
    n = 2
    yield n

a = my_gen()

print(next(a)) #Hello world

print(next(a)) #Hello heaven

print(next(a)) #Hello hell

print(next(a)) #StopIteration

```

Se define una función la cual tendrá su bloque de código y su scope.

En el ejemplo vemos que imprime un "Hola mundo", luego define una varaible n igual a cero y usa el keyword **yield**

**Yield** es el homólogo de **return**. Recordemos que return es el keyword que finaliza, queramos o no, a la función que estamos definiendo. Pero yield finaliza y pausa la función en ese preciso momenot. Y cuando se vuelva a llamar a dicha función, no iniciara desde el inicio, iniciara donde se pauso con yield. Eso es un generador. Tiene una sintaxis mas clara con respecto a las clases y más entendible.


Asi como hay lists comprehensions y dict comprehensions, existen también los generator comprehensions. Igual que como los iteradores, nos ahorran memoria la definir un iterador.
Un generator comprehension nos ayuda a recorrer una lista sin que se guarde solo cuando nosotros lo llamemos. 

```
my_list = [1,4,7,9,10]

my_second_list = [x*2 for x in my_list]

my_second_gen = (x*2 for x in my_list) #Generator comprehension


```

## Sets

Un set es una colección desordenada de elementos únicos e inmutables

```
my_set = {3, 4, 5}

my_set2 = {"hola", 23.3, False, True}

my_set3 = {3, 3, 2}

my_set4 = {[1,2,3], 4}  #Alzara un error ya que una lista es un objeto mutable

```


Como vimos en la definición de sets, en los ejemplos vemos que el set 1 y 2 los regresa de forma desordenada. El set 3 se repite un número, pero Python interpreta que necesitamos crear un conjunto con los números que le demos entonces elimina los elementos repetidos. Al final, el conjunto 4 no se podrá definir como set debido a que hay un elemento mutable, una lista, que se encuentra adentro.

¿Qué pasa si quiero crear un set vacío? Bueno, para esto necesitamos de la función built-in llamada **set ()**. La cual creara un conjunto vació ya que Python toma las llaves como un diccionario.

```
empty_set = {}
print(type(empty_set)) >> <clas 'dict'>

empty_set = set()
print(type(empty_set)) >> <clas 'set'>

```

### Casting con los sets

Si queremos convertr una estrucutra de datos tipo lista o tupla a una estructura de datos tipo set, realizamos lo siguiente

```
my_list = [1,1,2,3,4,4,5]
my_set  = set(my_list)
print(my_set) >> {1,2,3,4,5}

my_tuple = ("Hola", "Hola", "Hola", 1)
my_set2 = set(my_tuple)
print(my_set2) >> {"Hola", 1}

```
Tenemos una lista de números repetidos, usando la función set convertimos una lista a un set y nos retornara datos únicos. De igual forma para convertir una tupla a un set.

### Añadir elementos a un set

Para poder añadir elementos a un set ya creado tenemos a nuestra disposición dos métodos del objeto set: add()  y update(). 

```
my_set = {1,2,3}


my_set.add(4)

my_set.update([1,2,5])

my_set.update((1,7,2), {6,8})


```

### Borrar elementos de un set

Para poder borrar elementos de un set utilizaremos el método **remove** o **discard**. Los dos métodos realizan la misma accion. Pero la gran diferencia es que remove al tratar de eliminar un elemento inexistente en un conjunto nos alcanzara un error del tipo **keyerror**.


```
my_set = {1,2,3,4,5,6,7}

my_set.discard(1)

my_set.remove(2)

my_set.discard(10)

my_set.remove(12) >> #Levanta un error

```

Ahora veamos otros métodos de borrado interesantes. Para poder borrar un elemento aleatorio de un conjunto de datos utilizamos el método **pop** el cual eliminara un elemento de forma aleatoria de un set. Como vemos en el ejemplo. Si queremos borrar todos los datos de un conjunto utilizamos el método **clear**


## Operador de sets

### Union

Se refiere a la unión de dos conjuntos de elementos únicos e inmutables, i.e. combinara sus elementos eliminando los repetidos. Para lograr esta unión en Python utilizaremos el operadore pipe |.
```
my_set1 = {1,2,3}
my_set2 = {4,5,6}

my_set3 = my_set1 | my_set2

print(my_set3) >> {1,2,3,4,5,6}

```

### Intersección

Se refiere a la intersección de dos conjuntos en donde el conjunto resultante será los elementos que comparten en común. Para lograr esta operación lo hacemos con el ampersand &.

```
my_set1 = {2,3,4}
my_set2 = {4,5,6}

my_set3 = my_set1 & my_set2

print(my_set3) >> {4}

```

### Diferenciación

Es la diferencia que existe entre un conjunto y otro. Se logra con el operador de resta -.

```
my_set1 = {2,3,4}
my_set2 = {4,5,6}

my_set3 = my_set1 - my_set2

print(my_set3) >> {2,3}

```

### Difrencia simétrica

Se refiere al conjunto resultante entre dos conjuntos excepto con los elementos que se comparten. Esta operación se puede lograr con el operador circunflejo ^. 

```
my_set1 = {2,3,4}
my_set2 = {4,5,6}

my_set3 = my_set1 ^ my_set2

print(my_set3) >> {2,3,5,6}

```

## Manejo de fechas

A lo largo de la carrera de programador con Python te vas a topar con que tienes que manejar fechas, tiempos etc. Para esto Python nos ofrece la librería **datetime**. Librería que se encuentra en el core de Python.

### Formtao de fechas

Para darle formato a una fecha hay que aprendernos una tabla si o si para darle formato a una fecha. Podemos encontrar los diferentes tipos de formatos en https://docs.python.org/3/library/datetime.html#strftime-and-strptime-behavior

| Formato | Significado |
|-------|-------------|
| %Y | Year |
| %m | Month |
| %d | Day |
| %H | Hour |
| %M | Minute |
| %S | Second |


