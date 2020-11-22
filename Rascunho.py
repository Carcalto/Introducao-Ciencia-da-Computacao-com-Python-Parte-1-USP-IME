def solution(N):
    if 1 <= N <= 2147483647:
        N1 = list(bin(N)[2:])
        
    
    else:
        N1 = 'Não Rola!!'

    return N1

lista = solution(20)
lista2 = []
lista3 = []
count = 0
count2 = []

for i in lista:
    if i == '0':
        lista2.append(i)
        count = count + 1
        #if count > 1:
        count2.append(count)
        
    else:
        #lista3.append(i)
        count = 0




print(lista)
#print(lista3)
print(count2)
print(max(count2))




