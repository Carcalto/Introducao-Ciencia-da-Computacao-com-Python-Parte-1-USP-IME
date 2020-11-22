import re

def le_assinaturas():
    print("Bem-vindo ao detector automático de COH-PIAH.")
    print("Informe a assinatra típica de um aluno infectado: ")

    wal = float(input("Entre o tamanho médio da palavra:"))
    ttr = float(input("Entre a relação Type-Token:"))
    hlr = float(input("Entre a Razão Hapax Legomana:"))
    sal = float(input("Entre o tamanho médio de sentença:"))
    sac = float(input("Entre a complexiade média de sentença:"))
    pal = float(input("Entre o tamanho médio de frase:"))

    return [wal, ttr, hlr, sal, sac, pal]

def le_textos():
    i = 1
    textos = []
    texto = input("Digite o texto " + str(i) +"(aperte enter para sair):")
    while texto:
        textos.append(texto)
        i += 1
        texto = input("Digite o texto " + str(i) +"(aperte enter para sair):")

    return textos

def separa_sentencas(texto):
    sentencas = re.split(r'[.!?]+', texto)
    if sentencas[-1] == '':
        del sentencas[-1]
    
    return sentencas

def separa_frases(sentenca):
    return re.split(r'[,:;]+', sentenca)

def separa_palavras(frase):
    return frase.split()

def n_palavras_unicas(lista_palavras):
    freq = dict()
    unicas = 0
    for palavra in lista_palavras:
        p = palavra.lower()
        if p in freq:
            if freq[p] == 1:
                unicas -= 1
            freq[p] += 1
        else:
            freq[p] = 1
            unicas += 1
    
    return unicas

def n_palavras_diferentes(lista_palavras):
    freq = dict()
    for palavra in lista_palavras:
        p = palavra.lower()
        if p in freq:
            freq[p] += 1
        else:
            freq[p] = 1

    return len(freq)


def compara_assinatura(as_a, as_b):
    
    i = 0
    soma = 0
    while i < len(as_a):
        soma += (abs(as_a[i] - as_b[i] ))
        i += 1

    
    return soma / 6


def calcula_assinatura(texto):

    assinatura = []
    assinatura.append(tamanho_medio_palavra(texto))
    assinatura.append(type_Token(texto))
    assinatura.append(hapax_legomana(texto))
    assinatura.append(tamanho_medio_sentenca(texto))
    assinatura.append(complexidade_medio_sentenca(texto))
    assinatura.append(tamanho_medio_frase(texto))

    return assinatura


def avalia_textos(textos, ass_cp):

    textos_separados = quebrarLista(textos)
    
    i = 0
    listaAvaliacao = []
    while i < len(textos_separados):
        aux = calcula_assinatura(textos_separados[i])
        aux1 = compara_assinatura(aux, ass_cp)
        listaAvaliacao.append(aux1)
        i += 1


    return listaAvaliacao


def tamanho_medio_palavra(texto):
    
    sentenca = []
    for elemento in texto:
        sentenca += separa_sentencas(elemento)

    frase = []
    for elemento in sentenca:
        frase += separa_frases(elemento)
    
    palavras = []
    for elemento in frase:
        palavras += separa_palavras(elemento)

    totalDeLetras = 0
    for elemento in palavras:
        totalDeLetras += len(elemento)


    return totalDeLetras / len(palavras)


def tamanho_medio_sentenca(texto):
    
    sentenca = []
    for elemento in texto:
        sentenca += separa_sentencas(elemento)

    soma = 0
    for elemento in sentenca:
        soma += len(elemento)

    return soma / len(sentenca)


def complexidade_medio_sentenca(texto):
    
    sentenca = []
    for elemento in texto:
        sentenca += separa_sentencas(elemento)

    frase = []
    for elemento in sentenca:
        frase += separa_frases(elemento)

    return len(frase) / len(sentenca)


def tamanho_medio_frase(texto):
    
    sentenca = []
    for elemento in texto:
        sentenca += separa_sentencas(elemento)

    frase = []
    for elemento in sentenca:
        frase += separa_frases(elemento)
    
    palavras = []
    for elemento in frase:
        palavras += separa_palavras(elemento)

    soma = 0
    for elemento in frase:
        soma += len(elemento)

    return soma / len(frase)


def type_Token(texto):
    
    sentenca = []
    for elemento in texto:
        sentenca += separa_sentencas(elemento)

    frase = []
    for elemento in sentenca:
        frase += separa_frases(elemento)
    
    palavras = []
    for elemento in frase:
        palavras += separa_palavras(elemento)

    return n_palavras_diferentes(palavras) / len(palavras)


def hapax_legomana(texto):
    
    sentenca = []
    for elemento in texto:
        sentenca += separa_sentencas(elemento)

    frase = []
    for elemento in sentenca:
        frase += separa_frases(elemento)
    
    palavras = []
    for elemento in frase:
        palavras += separa_palavras(elemento)

    return n_palavras_unicas(palavras) / len(palavras)


def quebrarLista(l):
    n = len(l)
    quebrada = [l[i::n] for i in range(n)]
    
    return quebrada




def main():

    ass_cp = le_assinaturas()
    textos = le_textos()
    lista = avalia_textos(textos, ass_cp)
    menor = min(lista)
    posicao = lista.index(menor) + 1
    print(lista)
    print(min(lista))
    print('\nO autor do texto', posicao,'está infectado com COH-PIAH')


main()