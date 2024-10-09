# Game-TowerDefense

Este projeto implementa um jogo de Tower Defense em Python, onde o objetivo é encontrar o caminho de menor dano em um tabuleiro quadrado com torres. A classe principal, `JogoTowerDefense`, gerencia o tabuleiro, a adição de torres e o cálculo do menor caminho para se deslocar do ponto inicial ao ponto final, evitando ou minimizando o dano causado pelas torres.

## Funcionalidades

1. **Criação do Tabuleiro**: Um tabuleiro quadrado de tamanho `n x n` é criado, onde o jogador pode posicionar torres em diferentes posições.

2. **Adição de Torres**: Torres podem ser adicionadas ao tabuleiro com coordenadas específicas, e cada torre possui um valor de dano.

3. **Cálculo de Dano**: A função `calcular_dano` determina o dano total que uma unidade sofre ao passar por uma posição específica do tabuleiro, levando em conta a proximidade das torres.

4. **Algoritmo de Menor Caminho**: Utilizando uma variação do algoritmo A*, o método `encontrar_menor_dano` encontra o caminho com o menor dano entre o ponto inicial (0,0) e o ponto final (`n-1, n-1`).

5. **Conversão de Caminho para Direções**: O caminho gerado é convertido em direções simples (Norte, Sul, Leste, Oeste) para facilitar a visualização do trajeto.

6. **Carregamento e Salvamento de Arquivos**: O tabuleiro pode ser carregado a partir de um arquivo de texto (`.in`), e as direções do melhor caminho podem ser salvas em um arquivo de saída (`.out`).

## Como Utilizar

1. **Carregar o Tabuleiro**:
   O tabuleiro e a posição das torres são carregados a partir de um arquivo de texto de entrada. O arquivo deve seguir o formato:
   
   ```
   n
   linha1
   linha2
   ...
   ```
   Onde `n` é o tamanho do tabuleiro e cada linha subsequente indica a presença de torres (`T`) ou espaços vazios (`0`).

2. **Encontrar o Melhor Caminho**:
   Após carregar o tabuleiro, o jogo busca o caminho com o menor dano, imprimindo o dano mínimo e o caminho encontrado.

3. **Salvar Direções**:
   As direções (Norte, Sul, Leste, Oeste) do melhor caminho são salvas em um arquivo de saída.

## Exemplo de Execução

1. **Carregar o jogo**:
   ```python
   jogo = JogoTowerDefense.carregar_de_arquivo('inst2.in')
   ```

2. **Encontrar o menor dano**:
   ```python
   menor_dano, melhor_caminho = jogo.encontrar_menor_dano()
   ```

3. **Converter para direções e salvar**:
   ```python
   direcoes = jogo.converter_para_direcoes(melhor_caminho)
   jogo.salvar_direcoes('sol.out', direcoes)
   ```

4. **Imprimir resultados**:
   ```python
   print("Menor Dano:", menor_dano)
   print("Melhor Caminho:", melhor_caminho)
   ```

5. **Exibir o tabuleiro com o caminho**:
   O tabuleiro é impresso no console com o melhor caminho marcado por `-` e as torres marcadas por `T`.

## Requisitos

- Python 3.x
- Biblioteca `heapq` para a implementação do algoritmo de busca de menor caminho.
- Biblioteca `copy` para realizar cópias profundas do estado do jogo.

## Exemplo de Arquivo de Entrada (inst2.in)

```
5
T000T
00000
00000
T000T
00000
```

## Contribuição

Sinta-se à vontade para contribuir com melhorias no código, otimizações ou novas funcionalidades.

## Licença

Este projeto está sob a licença MIT.
