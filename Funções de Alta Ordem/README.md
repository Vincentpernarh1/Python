Importante: este VPL será testado por um interpretador de Python 3.X, mas o código disponível também é compatível com Python 2.X.

Neste exercício, você deverá completar algumas funções vistas em aula. O esqueleto dessas funções está disponível em um arquivo já pré-feito. Esse arquivo chama-se todo.py. O arquivo possui 10 funções que precisam ser completadas. Essas funções possuem somente um comentário "TODO" em seu corpo e retornam None. Seu código será testado por um arquivo chamado Driver.py. Você não precisa se preocupar com esse arquivo; ele já está feito para você. Contudo, note que ele importa todo, então o nome do arquivo enviado deve ser este (com a extensão .py). Para realizar este exercício, baixe os dois arquivos, e edite o arquivo todo.py. Em seguida, envie os dois arquivos para serem corrigidos. O arquivo Driver.py pode ser enviado sem modificações. Se quiser testar seu programa localmente, pode usar os comandos abaixo:

$ echo "9 10 11 12 13 14 17 18 19" > test.txt
$ python Driver.py < test.txt
[11, 13, 17, 19]

As funções que precisam ser implementadas são as seguintes:

factAll(L): retorna uma nova lista com o fatorial de cada número em L
strAll(L): retorna uma nova lista com cada elemento de L convertido para uma string
incAll(L): retorna uma nova lista com cada elemento de L incrementado de 1
sqrAll(L): retorna uma nova lista com cada elemento de L elevado ao quadrado
isPrimeAll(L): retorna uma nova lista (de booleanos), em que a posição n é verdade se o elemento n de L for primo.
incAllN(L, N): retorna uma nova lista com cada elemento de L incrementado de N.
filterOdd(L): retorna uma nova lista somente com os números de L que são ímpares.
filterPositive(L): retorna uma nova lista somente com os números de L que são maiores que zero.
filterGtN(L, N): retorna uma nova lista somente com os números de L que são maiores que N.
filterPrimes(L): retorna uma nova lista somente com os números primos que estão em L.
Exemplos monstrando como cada função é usada podem ser vistos abaixo:

>>> L = py2ll(range(1, 10))
>>> factAll(L)
(1, (2, (6, (24, (120, (720, (5040, (40320, (362880, None)))))))))
>>> strAll(L)
('1', ('2', ('3', ('4', ('5', ('6', ('7', ('8', ('9', None)))))))))
