Neste exercício, assim como nos anteriores, você deverá completar algumas funções disponíveis em um arquivo todo.py. O arquivo possui 4 funções que precisam ser completadas. Essas funções possuem somente um comentário "TODO" em seu corpo e retornam a lista vazia, ou False. Seu código será testado por um arquivo chamado Driver.py. Você não precisa se preocupar com esse arquivo; ele já está feito para você. Contudo, note que ele importa todo, então o nome do arquivo enviado deve ser este (com a extensão .py). Para realizar este exercício, baixe os dois arquivos, e edite o arquivo todo.py. Em seguida, envie os dois arquivos para serem corrigidos. O arquivo Driver.py pode ser enviado sem modificações.

As funções que devem ser implementadas possuem comentários no arquivo todo.py, que indicam o que elas fazem. Abaixo seguem exemplos das funções sendo usadas:

$ python -i todo.py

>>> delInitials(['Fer', 'mag', 'Q', 'pereira'])
'Fer, Mag, Pereira'
>>> delInitials(['Fer', 'm', 'Q', 'pereira'])
'Fer, Pereira'
>>> delInitials(['Fer', 'mag', 'Q', 'pereira', 'S', 'Sa'])
'Fer, Mag, Pereira, Sa'
>>> delInitials(['a', 'aa', 'b', 'bb'])
'Aa, Bb'
>>> everyOccurrence('Fernando', 'aeiou')
[1, 4, 7]
>>> everyOccurrence('xaxbxaxyza', 'aeiou')
[1, 5, 9]
>>> everyOccurrence('0a1e2i3o4u', 'aeiou')
[1, 3, 5, 7, 9]
>>> factors(6)
[2, 3]
>>> factors(10)
[2, 5]
>>> factors(12)
[2, 3, 4, 6]
>>> factors(28)
[2, 4, 7, 14]
>>> isPerfect(6)
True
>>> isPerfect(10)
False
>>> isPerfect(12)
False
>>> isPerfect(28)
True
