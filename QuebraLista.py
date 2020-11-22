l = [1,2,3,4,5,6,7,8,9,10]

def quebrarLista(l):
    n = len(l)
    splited = [l[i::n] for i in range(n)]
    
    return splited

print(quebrarLista(l))


