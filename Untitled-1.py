import math

a = float(input("Digite o valor de A: "))
b = float(input("Digite o valor de B: "))
c = float(input("Digite o valor de C: "))

delta = b ** 2 - 4 * a * c


if delta == 0:
    deltaRaiz = math.sqrt(delta)
    x1 = (-b + deltaRaiz) / (2 * a)
    x2 = (-b - deltaRaiz) / (2 * a)
    print("As raizes da equação são iguais", x1,"e", x2)
else:
    if delta < 0:
       print("Esta equação não possui raizes reais.")
    else:
       deltaRaiz = math.sqrt(delta)
       x1 = (-b + deltaRaiz) / (2 * a)
       x2 = (-b - deltaRaiz) / (2 * a)
       print("As raizes da equação são", x1,"e", x2)

