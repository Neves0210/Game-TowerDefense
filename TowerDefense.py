import heapq
import copy

class Torre:
    def __init__(self, dano=10):
        self.dano = dano

class JogoTowerDefense:
    def __init__(self, n):
        self.n = n
        self.tabuleiro = self.criar_tabuleiro(n)
        self.torres = []

    def criar_tabuleiro(self, n):
        return [[0 for _ in range(n)] for _ in range(n)]

    def adicionar_torre(self, x, y):
        if 0 <= x < self.n and 0 <= y < self.n:
            self.tabuleiro[x][y] = 1
            self.torres.append((x, y, Torre()))

    def copiar_estado_jogo(self):
        return copy.deepcopy(self)

    @staticmethod
    def carregar_de_arquivo(nome_arquivo):
        with open(nome_arquivo, 'r') as arquivo:
            linhas = arquivo.readlines()
        
        n = int(linhas[0].strip())
        jogo = JogoTowerDefense(n)

        for i, linha in enumerate(linhas[1:]):
            for j, caractere in enumerate(linha.strip()):
                if caractere == 'T':
                    jogo.adicionar_torre(i, j)

        return jogo

    def calcular_dano(self, x, y):
        dano = 0
        for i in range(self.n):
            for j in range(self.n):
                if self.tabuleiro[i][j] == 1:
                    if abs(i - x) <= 1 and abs(j - y) <= 1:
                        dano += 10
        return dano

    def encontrar_menor_dano(self):
        n = self.n
        inicio = (0, 0)
        fim = (n-1, n-1)
        movimentos = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        
        heap = [(0, inicio)]
        distancias = {inicio: 0}
        caminho = {inicio: None}
        
        while heap:
            custo_atual, (x, y) = heapq.heappop(heap)
            
            if (x, y) == fim:
                break
            
            for dx, dy in movimentos:
                nx, ny = x + dx, y + dy
                if 0 <= nx < n and 0 <= ny < n:
                    if self.tabuleiro[nx][ny] == 1:
                        continue
                    dano = self.calcular_dano(nx, ny)
                    novo_custo = custo_atual + dano
                    if (nx, ny) not in distancias or novo_custo < distancias[(nx, ny)]:
                        distancias[(nx, ny)] = novo_custo
                        heapq.heappush(heap, (novo_custo, (nx, ny)))
                        caminho[(nx, ny)] = (x, y)
        
        return distancias[fim], self.reconstruir_caminho(caminho, fim)
    
    def reconstruir_caminho(self, caminho, fim):
        caminho_reverso = []
        atual = fim
        while atual is not None:
            caminho_reverso.append(atual)
            atual = caminho[atual]
        return list(reversed(caminho_reverso))
    
    def converter_para_direcoes(self, caminho):
        direcoes = []
        for i in range(1, len(caminho)):
            x_atual, y_atual = caminho[i-1]
            x_prox, y_prox = caminho[i]
            if x_prox > x_atual:
                direcoes.append("Sul")
            elif x_prox < x_atual:
                direcoes.append("Norte")
            elif y_prox > y_atual:
                direcoes.append("Leste")
            elif y_prox < y_atual:
                direcoes.append("Oeste")
        return direcoes

    def salvar_direcoes(self, nome_arquivo, direcoes):
        with open(nome_arquivo, 'w') as arquivo:
            for direcao in direcoes:
                arquivo.writelines(direcao + "\n")

jogo = JogoTowerDefense.carregar_de_arquivo('inst2.in')

menor_dano, melhor_caminho = jogo.encontrar_menor_dano()

direcoes = jogo.converter_para_direcoes(melhor_caminho)

jogo.salvar_direcoes('sol.out', direcoes)

print("Menor Dano:", menor_dano)
print("Melhor Caminho:", melhor_caminho)

print("Tabuleiro com Caminho:")
for i in range(jogo.n):
    linha = ""
    for j in range(jogo.n):
        if (i, j) in melhor_caminho:
            linha += "- "
        elif jogo.tabuleiro[i][j] == 1:
            linha += "T "
        else:
            linha += "0 "
    print(linha.strip())