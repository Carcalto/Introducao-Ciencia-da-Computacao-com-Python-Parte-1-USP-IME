l = int(input('Digite a largura: '))
a = int(input('Digite a altura: '))
linha = 1

while linha <= a:
    
    coluna = 1
    while coluna <= l:
        print('#', end='')
        coluna = coluna + 1
    print()
    linha = linha + 1