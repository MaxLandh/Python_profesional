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



