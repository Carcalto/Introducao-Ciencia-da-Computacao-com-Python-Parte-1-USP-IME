n = int(input("Digite o valor de n: "))
fatorial = 1

if n ==0 or n == 1:
   print(fatorial)
else:
   while n > 1:
        fatorial = fatorial * n
        n = n - 1
   
   print(fatorial)