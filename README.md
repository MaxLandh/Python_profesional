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

> from typing import Dict, List, Tuple
> lista: List = []
> diccionario: Dict = {}
> tupla: Tuple = ()

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

'''
def main():
    a = 1
    def nested():
        print(a)
    
    return nested

my_func = main()
my_func()
'''


## ¿Donde aparecen los closures?

Aparecen cuando se tenga una clase que solo tenga un método y este se vuelva mas elegante.

Tambiém aparecen en los decoradores.

## Decoradores

