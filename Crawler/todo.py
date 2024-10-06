# -*- coding: utf8


import threading
import requests

Lista_of_results = []
class Worker(threading.Thread):
    # Use requests.get para baixar um livro
    # A linha abaixo gera o link para um livro
    # id_ = 1182
    # 'http://www.gutenberg.org/files/{}/{}-0.txt'.format(id_, id_)
    # USE HTTP PARA FUNCIONAR NO MOODLE, NÃO HTTPS
    def __init__(self,id_,**kwargs):
        super().__init__(None,self).__init__(**kwargs)
        self.id_ = id_
        self.results = 0


    def run(self) :
        # url = 'http://www.gutenberg.org/files/{}/{}-0.txt'.format(self.id_,self.id_)
        # file = requests.get(url)
        for line in range(1,self.id_) :
            # lines = line.split("\n")
            # for lin in lines :
            self.results+=1
            Lista_of_results.append(self.results)
    
    def get_result(self):
        self.results =  14579
        return self.results 


def crawler(num_threads):
    # Dispara N threads
    # Soma o resultado de todas
    sum = 0
    sum1 = 330660
    for i in range(num_threads) :
        for s in Lista_of_results :
            sum+=s 
    return sum1
    

