Crie uma classe Ponto2D com um inicializador que recebe dois parâmetros (x, y) do tipo float, com valor padrão 0.0.

Em seguida, crie uma classe Retangulo, que recebe em seu inicializador dois parâmetros (esq_sup, dir_inf) do tipo Ponto2D. Esses parâmetros definem um identificador, o ponto superior esquerdo e o ponto inferior direito do polígono. Esses parâmetros devem ser privados dentro da classe, e acessíveis através de properties* com o mesmo nome.

Nessa mesma classe, declare as seguintes funções públicas:

1) 'calcularArea()': Não recebe parâmetros e retorna a área do retângulo.

2) 'calcularIntersecao(ret)': Recebe um objeto do tipo Retangulo como parâmetro. O retorno segue as seguintes regras:

2.a) Caso não possua interseção com o retângulo informado retorna None;

2.b) Caso contrário: retorna o tamanho da área de interseção.

A classe também deve possuir duas properties chamadas width e height, que retornam os comprimentos nos eixos X e Y, respectivamente, calculados a partir de esq_sup e dir_inf.
