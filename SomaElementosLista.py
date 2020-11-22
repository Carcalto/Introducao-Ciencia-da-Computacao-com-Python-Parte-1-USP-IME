import random

lista1 = [1, 2, 3, 4, 5]
#lista1 = [random.randint(0,5) for i in range(10)]

def soma_elementos(lista):
    soma = 0
    for number in lista:
        soma = soma + number
    
    return soma

print(soma_elementos(lista1))
    
