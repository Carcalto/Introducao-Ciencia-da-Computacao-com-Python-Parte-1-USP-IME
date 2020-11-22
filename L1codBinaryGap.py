def solution(N):
    if 1 <= N <= 2147483647:
        N1 = list(bin(N)[2:])
    else:
        N1 = 'Não Rola!!'

    count = 0
    lacuna = 0
    count2 = []
    for i in N1:
        if i == '0':
            lista2.append(i)
            count = count + 1
            #if count > 1:
            count2.append(count)
        
        else:
            #lista3.append(i)
            lacuna = lacuna + 1
            count = 0

    
    if lacuna >= 2 and count2[count - 1]:
        return max(count2)
    else:
        return 0
        



solution(529)

