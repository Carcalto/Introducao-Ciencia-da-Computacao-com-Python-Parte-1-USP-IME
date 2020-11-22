import math


def soma_hipotenusas(n1):
    i = 1
    lista = []

    while i <= n1:
        j = 1
    
        while j <= n1:

            n = (i**2 + j**2)**0.5
        
        
            if n % math.floor(n) == 0 and n <= n1:
                lista.append(n)
                

            j = j + 1
        
        i = i + 1
    
    return soma_elementos(remove_repetidos(lista))



def remove_repetidos(lista):
    lista3 = []
    
    for elemento in lista:
        if elemento not in lista3:
            lista3.append(elemento)
    
    lista3.sort()
    return lista3


def soma_elementos(lista):
    soma = 0
    for number in lista:
        soma = soma + number
    
    return soma


soma_hipotenusas(25)


