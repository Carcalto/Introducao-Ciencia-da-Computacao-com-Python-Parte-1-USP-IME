numero = input("Digite um número onde seus algarismos serão somados: ")
numeroAlgarismos = len(numero)
numeroInteiro = int(numero)
aux = numeroInteiro
soma = 0
i = 1

while i <= numeroAlgarismos:
    soma = soma + aux % 10
    aux = aux // 10
    i = i + 1

print("A soma dos algarismos do número", numeroInteiro, "é:", soma)