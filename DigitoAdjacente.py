numero = input("Digite um número inteiro: ")
numeroAlgarismos = len(numero)
numeroInteiro = int(numero)
aux = numeroInteiro
i = 1
saida = 0

while i < numeroAlgarismos:
    aux1 = aux % 10
    aux2 = (aux // 10) % 10
    aux = aux // 10
    i = i + 1
    if aux1 == aux2:
       saida = saida + 1
       
    
if saida == 0:
   print("não")
else:
   print("sim")

    

