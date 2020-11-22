numero = int(input("Digite um número inteiro: "))
i = 1
count = 0

while i <= numero:
    if (numero % i) == 0:
       count = count + 1
       i = i + 1      
    else:
        i = i + 1
   
if count > 2:
    print("não primo")
else:  
    print("primo")
