# Jogo Tower Defense - README

## Descrição do Projeto
Este projeto implementa um jogo simples de **Tower Defense** utilizando a biblioteca **Tkinter** para criar uma interface gráfica em Python. O jogador pode adicionar torres defensivas em um tabuleiro e tentar encontrar o caminho com menor dano entre o ponto inicial (0,0) e o ponto final (n-1, n-1). O jogo calcula o dano das torres em torno delas e utiliza um algoritmo de Dijkstra para determinar o melhor caminho a ser seguido.

## Funcionalidades

- **Criação do Tabuleiro**: Permite ao usuário definir o tamanho do tabuleiro.
- **Adição de Torres**: As torres podem ser adicionadas manualmente clicando nas células ou aleatoriamente.
- **Cálculo do Menor Dano**: O jogo calcula o caminho com o menor dano possível entre o ponto de partida e o ponto final.
- **Exibição do Caminho Ótimo**: O caminho de menor dano é destacado visualmente no tabuleiro.

## Estrutura do Código

### 1. **Classe `Torre`**
Define uma torre com o atributo `dano`, que representa a quantidade de dano que a torre causa nas células adjacentes.

### 2. **Classe `JogoTowerDefense`**
Gerencia o tabuleiro do jogo, as torres e o cálculo de danos. Também implementa o algoritmo de Dijkstra para encontrar o caminho com menor dano.

- **Métodos principais**:
  - `criar_tabuleiro(n)`: Cria um tabuleiro vazio de tamanho `n x n`.
  - `adicionar_torre(x, y)`: Adiciona uma torre em uma posição especificada.
  - `calcular_dano_ao_adicionar_torre(x, y)`: Atualiza o valor de dano nas células ao redor de uma torre.
  - `encontrar_menor_dano()`: Usa o algoritmo de Dijkstra para encontrar o caminho de menor dano entre o ponto inicial e o final.
  - `reconstruir_caminho()`: Reconstrói o caminho encontrado pelo algoritmo de Dijkstra.

### 3. **Classe `TowerDefenseInterface`**
Implementa a interface gráfica do jogo utilizando **Tkinter**. Permite ao usuário configurar o jogo e interagir com o tabuleiro.

- **Métodos principais**:
  - `criar_configuracao_inicial()`: Define a interface para a configuração inicial do tamanho do tabuleiro e número de torres.
  - `iniciar_jogo()`: Inicia o jogo com os parâmetros configurados pelo usuário.
  - `adicionar_torre(x, y)`: Permite ao jogador adicionar ou remover torres manualmente.
  - `encontrar_menor_dano()`: Calcula e exibe o caminho com menor dano no tabuleiro.

### 4. **Interface Gráfica com Tkinter**
A interface gráfica oferece:
- Entradas de texto para o tamanho do tabuleiro e o número de torres.
- Botões para iniciar o jogo, adicionar torres, gerar torres aleatoriamente e calcular o menor dano.
- Exibição visual do tabuleiro, onde cada célula é representada por um botão.

## Como Executar

### Pré-requisitos
- **Python 3.x**
- **Tkinter** (incluso no Python padrão)

### Passos para Execução

1. Clone o repositório:
   ```bash
   git clone https://github.com/seu-usuario/seu-repositorio.git
   ```

2. Acesse o diretório do projeto:
   ```bash
   cd seu-repositorio
   ```

3. Execute o jogo:
   ```bash
   python main.py
   ```

4. A interface gráfica será aberta. Defina o tamanho do tabuleiro e o número de torres.

5. Clique em **Iniciar Jogo** para criar o tabuleiro.

6. Adicione torres clicando nas células ou deixe o jogo gerar torres aleatoriamente.

7. Clique em **Calcular Menor Dano** para encontrar o caminho ótimo e ver o dano total.

## Personalização

- **Tamanho do Tabuleiro**: O usuário pode definir o tamanho do tabuleiro (padrão 10x10).
- **Número de Torres**: O usuário pode definir a quantidade de torres (padrão 10).

## Melhorias Futuras

- Adicionar diferentes tipos de torres com diferentes alcances e níveis de dano.
- Implementar inimigos que se movem pelo tabuleiro.
- Adicionar níveis de dificuldade e temporizadores.
- Melhorar a interface gráfica com animações e temas visuais.

## Licença

Este projeto está licenciado sob a [MIT License](LICENSE).

---

> Desenvolvido por [Gabriel Neves](https://github.com/Neves0210). Contribuições são bem-vindas!

