Neste exercício, assim como nos anteriores, você deverá completar algumas funções disponíveis em um arquivo todo.py. O arquivo possui uma classe que precisam ser implementada. Esta classe vai ser uma Thread. 

O propósito da sua Thred é baixar livros do https://www.gutenberg.org/browse/scores/top. Seu código será testado por um arquivo chamado Driver.py. Você não precisa se preocupar com esse arquivo; ele já está feito para você. Contudo, note que ele importa todo, então o nome do arquivo enviado deve ser este (com a extensão .py). Para realizar este exercício, baixe os dois arquivos, e edite o arquivo todo.py. Em seguida, envie os dois arquivos para serem corrigidos. O arquivo Driver.py pode ser enviado sem modificações.

Qual a ideia da sua thread? A mesma tem que baixar livros do projeto Gutenberg. Após baixar os livros, sua thread deve contar quantas LINHAS existem nos livros. A lista de livros para baixar vai ser disponilizada na pasta dados.

O Driver.py basicamente vai rodar seu código variando o número de threads que devem ser disparada.

Lembre que você vai ter que implementar um método para pegar o resultado.

class Worker(threading.Thread)
    # ....
    
    def run(self):
        # 1. Baixar um livro
        # 2. Contar o número de linhas do livro    
    def get_result(self):
            # 1. retorna o número de linhas do livro


Além da classe Worker. Você deve implementar uma função crawl. Esta função dispara os vários Workers e depois soma o número de LINHAS de TODOS os livros.

Embora não seja possível realizar testes avançados no VPL, rode o código na sua máquina e compare o tempo de execução com números diferentes de threads.
