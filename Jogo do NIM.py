def partida():
    n = int(input("Quantas peças? "))
    m = int(input("Limite de peças por jogadas? "))
    while m < 1 or m > n:
        print("\nO limite de peças por jogadas tem que ser o mínimo 1 e no máximo", n,"!!\n")
        m = int(input("\nLimite de peças por jogadas? "))

    jogada = 0
    aux = 0
    if (n % (m+1) == 0):
        print("\nVocê começa!\n")
        jogada = 1
        while n > 0:
            if jogada == 1:
                aux = usuario_escolhe_jogada(n, m)
                print("\nVocê tirou", aux, "peças.")
                n = n - aux
                print("Agora restam", n,"peças no tabuleiro.")
                jogada = 2
            else:
                aux = computador_escolhe_jogada(n, m)
                print("\nO computador tirou", aux, "peças.")
                n = n - aux
                print("Agora restam", n, "peças no tabuleiro.")
                jogada = 1

        if jogada == 1:
            print("\nFim do jogo! O computador ganhou!\n")
            return 2 
        else:
            print("\nFim do jogo! Você ganhou!\n")
            return 1 

    else:
        print('\nComputador começa!')
        jogada = 2
        while n > 0:
            if jogada == 2:
                aux = computador_escolhe_jogada(n, m)
                print("\nO computador tirou", aux, "peças.")
                n = n - aux
                print("Agora restam", n,"peças no tabuleiro.\n")
                jogada = 1
            else:
                aux = usuario_escolhe_jogada(n, m)
                print("\nVocê tirou", aux, "peças.")
                n = n - aux
                print("Agora restam", n, "peças no tabuleiro.\n")
                jogada = 2

        if jogada == 1:
            print("Fim do jogo! O computador ganhou!\n")
            return 2 
        else:
            print("Fim do jogo! Você ganhou!\n")
            return 1
    
    

def start():
    print("Bem-vindo ao jogo do NIM!\nEscolha: \n")
    print("1 - para jogar partida isolada")
    print("2 - para jogar campeonato\n")
    opcao = int(input("Opção: "))
    
    while opcao != 1 and opcao != 2:
        print("\nEscolha uma opção válida!\n")
        print("Digite novamente!\n")
        opcao = int(input("Opção: "))

    if opcao == 1:
        print("\nVocê escolheu partida isolada!\n")
        partida()
    
    if opcao == 2:
        print("\nVocê escolheu um campeonato!\n")
        campeonato()
       

def campeonato():
    QTDpartida = 1
    placarUsuario = 0
    placarComputador = 0
    while QTDpartida < 4:
        print("**** Rodada", QTDpartida ,"****\n")
        if partida() == 1:
            placarUsuario = placarUsuario + 1
        else:
            placarComputador = placarComputador + 1
        QTDpartida = QTDpartida + 1
        
    print("**** Final do campeonato! ****\n")
    print("Placar: Você", placarUsuario, "X", placarComputador, "Computador\n")


def usuario_escolhe_jogada(n,m):
    pUsuario = int(input("Quantas peças você vai tirar? "))
    while pUsuario > m or pUsuario <=0 or pUsuario > n:
        print("Oops! Jogada inválida! Tente de novo.\n")
        pUsuario = int(input("Quantas peças você vai tirar? "))
    
    return pUsuario


def computador_escolhe_jogada(n,m):    
    if n == m:
        return n
    
    if n % (m+1) != 0:
        return n % (m+1)
        

    
start()