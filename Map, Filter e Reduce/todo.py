from functools import reduce
from typing import Counter

def firstChars(L):
     # """ Maps strings in L to a list with the first character of each string.
    # For instance:
    # firstChars(['python', 'is', 'pythy']) == ['p', 'i', 'p']
    # """
    if not L :
        return None 
    else :
        return map(lambda x: str(x)[0],L)

def sum(L):
    """ Sums the elements in L """
    if not L :
        return 0
    else :
        return reduce(lambda x,b: x + b,L)

# def avg(L):
#     # """ Returns the average of the elements in L """

#     if not L:
#         return 0
#     else :
#         return (reduce(lambda x,b:(x+b)/x ,L))

def avg(L):
    # """ Returns the average of the elements in L """

    sum=count = 0.0 
    if not L:
        return 0
    else :
        for i in L :
            sum+=i
            count+=1

    return (sum/count)

def maxString(L):
    """ Retorna a maior string dentre as strings em L.
    Por exemplo: maxString(['python', 'is', 'pythy']) == 'python'
    Se houver empate, retorna a primeira string encontrada.
    """
    if not L :
        return None
    else :
        return reduce(lambda x,b : x if len(x) > len(b) else b ,L)

def add2Dict(D, N, S):
    """ Insere a string S na lista associada ao inteiro N dentro
    do dicionario D.
    Por exemplo, se D = {1: ['b'], 2: ['xd'], 3: ['abc']}, entao,
    add2Dict(D, 2, 'ww') produz o novo dicionario:
    {1: ['b'], 2: ['xd', 'ww'], 3: ['abc']}
    Voce pode usar essa funcao para completar buildLenFreq
    """
    D[N] = D[N] + [S] if N in D else [S]
    return D

def buildLenFreq(L):
    """ Esta funcao constroi um dicionario que associa inteiros a listas com
    palavras daquele tamanho. Por exemplo:
    ins(['abc', 'xd', 'b', 'xxx']) = {1: ['b'], 2: ['xd'], 3: ['abc', 'xxx']}
    """
    D ={}
    for item  in L :
       add2Dict(D,len(item),item)  
    return D

def incValue(D, N):
    """Esta funcao incrementa o valor associado a chave N dentro do dicionario
    D. Por exemplo, se D = {1: 2, 2: 4, 3: 11}, entao
    Voce pode usar essa funcao para completar countFirsts
    """
    D[N] = D[N] + 1 if N in D else 1
    return D

def countFirsts(L):
    """ Conta o numero de ocorrencias do primeiro caracter de cada string em L.
    Por exemplo, countFirsts(['python', 'is', 'pythy']) === {'i': 1, 'p': 2}
    Note que essa funcao retorna um dicionario com cada caracter associada ao
    numero de strings que comecam com aquele caracter.
    
    """
    D = {}
    D1 = {}
    count = 0
    for item in L :
       D[item[0]] = D.get(item[0],0)+1
       incValue(D1,D.values())
    return D
   



def mostCommonFirstChar(L):
    """ Retorna a letra mais comum entre as primeiras letras de strings em L.
    Por exemplo:
    mostCommonFirstChar(['python', 'is', 'pythy']) === 'p'
    """
    D = {}
    for item in L :
       D[item[0]] = D.get(item[0],0)+1
    m = max(list(D.values()))

    for item,value in D.items() :
        if value == m :
            return item