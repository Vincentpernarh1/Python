Neste exercício, assim como nos anteriores, você deverá completar algumas funções disponíveis em um arquivo todo.py. O arquivo possui 3 funções que precisam ser completadas. Essas funções possuem somente um comentário "TODO" em seu corpo e retornam None. Seu código será testado por um arquivo chamado Driver.py. Você não precisa se preocupar com esse arquivo; ele já está feito para você. Contudo, note que ele importa todo, então o nome do arquivo enviado deve ser este (com a extensão .py). Para realizar este exercício, baixe os dois arquivos, e edite o arquivo todo.py. Em seguida, envie os dois arquivos para serem corrigidos. O arquivo Driver.py pode ser enviado sem modificações.

As funções que devem ser implementadas possuem comentários no arquivo todo.py, que indicam o que elas fazem. Note que todas elas recebem listas de listas, e retornam listas de strings. Se quiser testar seu programa localmente, pode usar uma das três entradas abaixo. A única diferença entre esses arquivos é a primeira linha. Essa linha determina qual teste será realizado por Driver.py:

Entrada 1 (test_0.txt, que testa a função lastNames):

0
Artur, Alberto, Vaz
Micaelis, Aubertendraub, Witzengarten
Caius, Julius, Cesar

Entrada 2 (test_1.txt, que testa a função citations):

1
Artur, Alberto, Vaz
Micaelis, Aubertendraub, Witzengarten
Caius, Julius, Cesar

Entrada 3 (test_2.txt, que testa a função fullCitations):

2
Artur, Alberto, Vaz
Micaelis, Aubertendraub, Witzengarten
Caius, Julius, Cesar

Abaixo seguem comandos mostrando o programa de teste sendo usado com essas entradas:

Primeiro teste:

L$ python Driver.py < test_0.txt
Vaz
Witzengarten
Cesar

Segundo teste:

$ python Driver.py < test_1.txt
A. Vaz
M. Witzengarten
C. Cesar

Terceiro teste:

$ python Driver.py < test_2.txt
A. A. Vaz
M. A. Witzengarten
C. J. Cesar

Você também pode testar as funções que precisam ser feitas diretamente no interpretador em linha de comando:

$ python -i todo.py

>>> L = [['ana', 'Teresa', 'Silva'], ['Lydiani', 'Gomidi', 'Dantas']]
>>> lastNames(L)
['Silva', 'Dantas']
>>> citations(L)
['A. Silva', 'L. Dantas']
>>> fullCitations(L)
['A. T. Silva', 'L. G. Dantas']
