Neste exercício, assim como nos anteriores, você deverá completar algumas funções disponíveis em um arquivo todo.py. O arquivo é composto de uma série de funções que realizam diferentes fases de um sistema de map reduce paralelo. Seu trabalho vai ser processar uma grande quantidade de arquivos html usando Soup. Em particular, os arquivos inicialmente estão compactados via tar.gz. O código abaixo ensina como tem um esqueleto de uma função mapreduce.

Para testar em sua máquina baixe o arquivo: dcc.ufmg.br/~flaviovdf/dados.tar.gz

![image](https://github.com/user-attachments/assets/71478e2c-7407-47b1-b587-f7ce6528bac7)


import multiprocessing as mp
import tarfile
tar = tarfile.open("filename.tar.gz", "r:gz")
# f = tar.extractfile(member) pega o arquivo. veja o getmembers abaixo
with mp.Pool(4) as pool:
    # extrai os arquivos e recebe um dicionário de {cantor: samples+remix+cover}
    resultado_intermed = pool.imap_unordered(extract_and_process,  tar.getmembers())
    final = reduce(merge_function, resultado_intermed)


Você deve implementar (em breve falo do arquivo):

extract_and_process: vai extrair um arquivo do .tar.gz e retornar um dicionário de artist: popularidade. Retorne uma classe Counter
merge_function: combina todos os sorts anteriores. Retorne uma classe Counter
map_reduce: retorna o resultado final. Retorne uma classe Counter
Lembre-se do primeiro VPL deste módulo. É a mesma ideia, porém em paralelo.

Cada arquivo HTML contém uma lista de quantas vezes uma música foi Sampleada, Remixada ou Covered. Seu trabalho usando Soup é realizar a soma destes 3 valores por ARTISTA//BANDA. Por exemplo, ao processar o arquivo abaixo cada artista tem uma contagem de 14. Na pasta exemplos existem alguns HTML para vocês entenderem o formato.
![image](https://github.com/user-attachments/assets/70fc51cd-6887-43d3-bf9c-b8c77c2e10b3)

