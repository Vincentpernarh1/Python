# -*- coding: utf8

from typing import Counter
from bs4 import BeautifulSoup
from functools import reduce
from collections import Counter

import multiprocessing as mp
import tarfile


def extract_and_process(member):
    # observe como cada processo abre o tar novamente
    # a extração é feita por processo
    # veja exemplos do HTML na pasta exemplo
    # Para pegar o nome de um artist use texto.strip().split('-')[-1].
    # O formato do texto no html é Música - Artista
    
    # TODO: implemente o resto
    
    tar = tarfile.open("dados.tar.gz", "r:gz")
    f = tar.extractfile(member)
    soup = BeautifulSoup(f, 'html.parser')
    Artist = {}
   
    for name in soup.select('.trackInfo') :
        artist = name.get_text().strip().split('-')[-1]
        newArtist = artist.split("\n")
        if newArtist[0][1:] not in Artist:
            Artist[newArtist[0][1:]] = int(newArtist[1].split(" ")[1])
        else:
            Artist[newArtist[0][1:]] += int(newArtist[1].split(" ")[1])
    return Counter(Artist)

    pass

def merge_function(dict_1, dict_2):
    # TODO: implemente
    # {**dict_1,**dict_2}
    d2 = dict_1 + dict_2
    return d2
    pass


def mapreduce(num_cpus=2):
    tar = tarfile.open('dados.tar.gz', 'r:gz')
    if num_cpus > 1:
        with mp.Pool(num_cpus) as pool:
            intermed = pool.imap_unordered(extract_and_process,
                                           tar.getmembers())
    else:
        intermed = map(extract_and_process, tar.getmembers())
    final = reduce(merge_function, intermed)
    return final