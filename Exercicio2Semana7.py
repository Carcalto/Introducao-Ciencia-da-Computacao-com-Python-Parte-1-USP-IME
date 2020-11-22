l = int(input('Digite a largura: '))
a = int(input('Digite a altura: '))
linha = 1

while linha <= a:
    #if linha == 1 or linha == a:
     #   print('#', end='')
    
    
    
    
    coluna = 1
    while coluna <= l:
        if coluna == 1 or coluna == l or linha == 1 or linha == a:
            print('#', end='')
        
        else:
            print(' ', end='')

        coluna = coluna + 1
    print()
    linha = linha + 1