'''Reto de la clase de sets. Se definieran las cuatro operaciones con sets:
   Union, inteseccion, diferenciación y diferenciación simetrica.
'''


# set_1 = {1,5,6,9,7,"Hola", "País", "Platzi", True, False}
# set_2 = {1,6,4,9,7,2,3, "Mundo", "Platzi", "Ciudad", False}

# #Unión

# set_union = set_1 | set_2
# print('El conjunto de union es {}'.format(set_union))

# #Intersección

# set_intersection = set_1 & set_2
# print('El conjunto de intersección es {} '.format(set_intersection))

# #Diferenciación

# set_diff = set_1 - set_2
# print('El conjunto de diferenciación es {}'.format(set_diff))

# #Diferenciación simetrica

# set_diff_sim = set_1 ^ set_2
# print('El conjunto de diferenciación simetrica es {}'.format(set_diff_sim))


"""Eliminar elementos repeditos en una lista usando sets"""
import random
from typing import List

def remove_duplicates(some_list: List) -> List:
    set_list = set(some_list)
    list_to_list = list(set_list)
    return list_to_list


if __name__ == "__main__":
    my_list = [random.randint(0,10) for _ in range(0,10)] #Una lista de número aleatorios
    print('My list generated is: {}'.format(my_list))
    my_list_unique = remove_duplicates(my_list)
    print('My list unique is: {}'.format(my_list_unique))