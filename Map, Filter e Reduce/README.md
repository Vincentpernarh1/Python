Neste exercício, você deverá completar algumas funções disponíveis em um arquivo todo.py. O arquivo possui 7 funções que precisam ser completadas. Essas funções possuem somente um comentário "TODO" em seu corpo e retornam None, ou algum valor default. Seu código será testado por um arquivo chamado Driver.py. Você não precisa se preocupar com esse arquivo; ele já está feito para você. Contudo, note que ele importa todo, então o nome do arquivo enviado deve ser este (com a extensão .py). Para realizar este exercício, baixe os dois arquivos, e edite o arquivo todo.py. Em seguida, envie os dois arquivos para serem corrigidos. O arquivo Driver.py pode ser enviado sem modificações. Se quiser testar seu programa localmente, pode usar os comandos abaixo:

$ echo "1 10 11 12 13 14 17 18 19" > test.txt
$ python Driver.py < test.txt
114

As funções que precisam ser implementadas possuem comentários no arquivo todo.py, que explicam o que cada uma delas deve fazer. Exemplos monstrando como cada função é usada podem ser vistos abaixo:

>>> L0 = ['amar', 'o', 'estranho', 'deixa', 'confuso', 'este', 'coracao']
>>> L1 = [1, 2, 3]
>>> firstChars(L0)
['a', 'o', 'e', 'd', 'c', 'e', 'c']
>>> sum(L1)
6
>>> avg(L1)
2
>>> maxString(L0)
'estranho'
>>> buildLenFreq(L0)
{8: ['estranho'], 1: ['o'], 4: ['amar', 'este'], 5: ['deixa'], 7: ['confuso', 'coracao']}
>>> countFirsts(L0)
{'a': 1, 'c': 2, 'e': 2, 'd': 1, 'o': 1}
>>> mostCommonFirstChar(L0)
'c'
