import random

lista1 = [random.randint(0,5) for i in range(10)]


def remove_repetidos(lista):
    lista3 = []
    
    for elemento in lista:
        if elemento not in lista3:
            lista3.append(elemento)
    
    lista3.sort()
    return lista3

print(lista1)
print(remove_repetidos(lista1))

