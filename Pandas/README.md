Neste exercício, assim como nos anteriores, você deverá completar algumas funções disponíveis em um arquivo todo.py. O arquivo possui 10 funções que precisam ser completadas. Essas funções possuem um comentário "TODO" em seu corpo. Seu código será testado por um arquivo chamado Driver.py. Você não precisa se preocupar com esse arquivo; ele já está feito para você. Contudo, note que ele importa todo, então o nome do arquivo enviado deve ser este (com a extensão .py). Além desses dois arquivos, o VPL contém mais um arquivo requerido: games.csv. Para realizar este exercício, baixe os três arquivos, e edite o arquivo todo.py. Em seguida, envie os três arquivos para serem corrigidos. Os arquivos Driver.py e games.csv podem ser enviados sem modificações.

Neste VPL você irá processar um arquivo CSV ("games.csv") contendo os resultados de jogos olímpicos, por países. Abaixo segue uma imagem com o início da tabela. O próprio arquivo games.csv está disponível no enunciado do VPL, caso você queira testar seu programa off-line. Inclusive, você precisa enviar este arquivo junto com os arquivos Python, quando estiver resolvendo o VPL!

Cabeçalho da tabela games.csv.

![image](https://github.com/user-attachments/assets/d2e6b619-0e5f-4e43-a68d-e2f1db0813fc)


A tabela possui 17 colunas:

Country: Nome do país.
Code: Um código de três letras que unicamente identifica o país.
Summer: Número de jogos olímpicos de verão disputados.
GoldS, SilverS, BronzeS: Número de medalhas ganhas nos jogos olímpicos de verão.
TotalS: GoldS + SilverS + BronzeS.
Winger: Número de jogos olímpicos de inverno disputados.
GoldW, SilverW, BronzeW: Número de medalhas ganhas nos jogos olímpicos de inverno.
TotalW: GoldW + SilverW + BronzeW.
NumGames: Summer + Winter.
GoldT, SilverT, BronzeT: total de medalhas de cada tipo ganhas em todos os jogos.
CombinedTotal: total de medalhas ganhas em todos os jogos.
As funções que devem ser implementadas possuem comentários no arquivo todo.py, que indicam o que elas fazem. Abaixo seguem exemplos das funções sendo usadas:

$> ls
Driver.py todo.py games.csv

$> python3 -i todo.py

>>> games = pd.read_csv('games.csv')

>>> numSummerGoldCountry(games, 'Brazil')
23

>>> getNthBestSummerCountry(games, 20)
'West Germany'

>>> numCountriesWithMoreThanNWinterMedals(games, 10)
28
>>> countGoldsWithLetter(games, 'a')
190
>>> countGoldsWithLetter(games, 'd')
46
