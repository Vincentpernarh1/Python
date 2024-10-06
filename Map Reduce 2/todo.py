# -*- coding: utf8


from collections import Counter # RECOMENDADO!


def conta_um_arquivo(fpath):
    dic = {}
    with open(fpath) as input_file:
        for line in input_file:
            line = line.lower().strip()
            if line:
                palavras = line.split()
                for i in palavras:
                    if i in dic :
                        dic[i]+=1
                    else :
                        dic[i] = 1
        return dic


def reduz(contagens_1, contagens_2):
    A = Counter(contagens_1)
    B = Counter(contagens_2)
    return (A+B)