def éprimo (x):
    primo = False
    i = 1
    count = 0
    while i <= x:
        if (x % i) == 0 and x != 1:
             count = count + 1
             i = i + 1      
        else:
             i = i + 1
   
    if count == 2:
           primo = True
    else:
        primo
     
    return primo


def maior_primo(n):
    aux = 0
    count2 = 0
    while aux <= n:
       if (éprimo(aux) == True):
           ultimo = aux
           count2 = count2 + 1
           aux = aux + 1     
       else:
          aux = aux + 1
    
    return count2

print(maior_primo(100))