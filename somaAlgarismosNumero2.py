numero = input("Digite um número inteiro: ")
numeroAlgarismos = len(numero)
numeroInteiro = int(numero)
aux = numeroInteiro
soma = 0
i = 1

while i <= numeroAlgarismos:
    soma = soma + aux % 10
    aux = aux // 10
    i = i + 1

print(soma)