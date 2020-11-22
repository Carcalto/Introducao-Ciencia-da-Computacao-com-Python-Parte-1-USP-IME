n = int(input("Digite o valor de n: "))
impar = 1

while n > 0:
    if (impar % 2) == 1:
        
        n = n - 1
        print(impar)
        impar = impar + 1
        
    else:
        impar = impar + 1
    