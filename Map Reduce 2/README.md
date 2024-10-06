Neste exercício, assim como nos anteriores, você deverá completar algumas funções disponíveis em um arquivo todo.py. O arquivo possui 2 funções que precisam ser completadas. Seu código será testado por um arquivo chamado Driver.py. Você não precisa se preocupar com esse arquivo; ele já está feito para você. Contudo, note que ele importa todo, então o nome do arquivo enviado deve ser este (com a extensão .py). Para realizar este exercício, baixe os dois arquivos, e edite o arquivo todo.py. Em seguida, envie os dois arquivos para serem corrigidos. O arquivo Driver.py pode ser enviado sem modificações.

As funções que devem ser implementadas possuem comentários no arquivo todo.py, que indicam o que elas fazem.

Seu programa final deve gerar uma saída no estilo:

[('the', 12793), ('to', 8039), ('and', 7692), ('of', 7489), ('a', 5683)]

A função map e a reduce produzem dicionários de contagens. Cada entrada é uma palavra e a saída um valor.

>>> resultadomap = list(map(conta_um_arquivo, glob.glob(pasta)))
>>> next(iter(resultadomap[0].items()))
('\ufeffthe', 1)
