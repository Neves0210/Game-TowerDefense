import tkinter as tk
from tkinter import messagebox
import heapq
import random
import os
import time

# Definição da classe Torre
class Torre:
    def __init__(self, dano=10):
        self.dano = dano

# Definição da classe JogoTowerDefense
class JogoTowerDefense:
    def __init__(self, n):
        self.n = n
        self.tabuleiro = self.criar_tabuleiro(n)
        self.torres = []
        self.matriz_dano = [[0 for _ in range(n)] for _ in range(n)]

    def criar_tabuleiro(self, n):
        return [[0 for _ in range(n)] for _ in range(n)]

    def adicionar_torre(self, x, y):
        if 0 <= x < self.n and 0 <= y < self.n:
            self.tabuleiro[x][y] = 1
            self.torres.append((x, y, Torre()))
            self.calcular_dano_ao_adicionar_torre(x, y)

    def calcular_dano_ao_adicionar_torre(self, x, y):
        for i in range(max(0, x-1), min(self.n, x+2)):
            for j in range(max(0, y-1), min(self.n, y+2)):
                self.matriz_dano[i][j] += 10

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
                if 0 <= nx < n and 0 <= ny < n and self.tabuleiro[nx][ny] != 1:
                    novo_custo = custo_atual + self.matriz_dano[nx][ny]
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

# Interface com Tkinter
class TowerDefenseInterface:
    def __init__(self, root):
        self.root = root
        self.n = 10
        self.torres_aleatorias = 10
        self.jogo = None
        self.botao_matriz = None
        self.frame_tabuleiro = None  
        self.criar_configuracao_inicial()

    def criar_configuracao_inicial(self):
        frame_config = tk.Frame(self.root)
        frame_config.grid(row=0, column=0)

        # Entrada para o tamanho do tabuleiro
        tk.Label(frame_config, text="Tamanho do Tabuleiro:").grid(row=0, column=0)
        self.tamanho_input = tk.Entry(frame_config)
        self.tamanho_input.grid(row=0, column=1)
        self.tamanho_input.insert(0, "10")

        # Entrada para o número de torres
        tk.Label(frame_config, text="Número de Torres:").grid(row=1, column=0)
        self.torres_input = tk.Entry(frame_config)
        self.torres_input.grid(row=1, column=1)
        self.torres_input.insert(0, "10")

        # Botão para iniciar o jogo
        botao_iniciar = tk.Button(frame_config, text="Iniciar Jogo", command=self.iniciar_jogo)
        botao_iniciar.grid(row=2, column=0, columnspan=2)

    def iniciar_jogo(self):
        try:
            self.n = int(self.tamanho_input.get())
            self.torres_aleatorias = int(self.torres_input.get())
            self.jogo = JogoTowerDefense(self.n)
            
            self.limpar_tabuleiro()
            self.criar_tabuleiro()
            self.gerar_tabuleiro_aleatorio()
        except ValueError:
            messagebox.showerror("Erro", "Por favor, insira valores válidos para o tamanho do tabuleiro e o número de torres.")

    def limpar_tabuleiro(self):
        if self.frame_tabuleiro is not None:
            self.frame_tabuleiro.destroy()

    def criar_tabuleiro(self):
        self.frame_tabuleiro = tk.Frame(self.root)
        self.frame_tabuleiro.grid(row=1, column=0)

        self.botao_matriz = [[None for _ in range(self.n)] for _ in range(self.n)]
        for i in range(self.n):
            for j in range(self.n):
                if (i, j) == (self.n - 1, self.n - 1):  
                    botao = tk.Button(self.frame_tabuleiro, text="Fim", width=3, height=2)
                else:
                    botao = tk.Button(self.frame_tabuleiro, text="0", width=3, height=2, 
                                      command=lambda x=i, y=j: self.adicionar_torre(x, y))
                botao.grid(row=i, column=j)
                self.botao_matriz[i][j] = botao

        botao_calcular = tk.Button(self.root, text="Calcular Menor Dano", command=self.encontrar_menor_dano)
        botao_calcular.grid(row=2, column=0)

    def adicionar_torre(self, x, y):
        if self.jogo.tabuleiro[x][y] == 0:
            self.jogo.adicionar_torre(x, y)
            self.botao_matriz[x][y].config(text="T", bg="red")
        else:
            self.jogo.tabuleiro[x][y] = 0
            self.botao_matriz[x][y].config(text="0", bg="SystemButtonFace")

    def gerar_tabuleiro_aleatorio(self):
        for i in range(self.n):
            for j in range(self.n):
                self.jogo.tabuleiro[i][j] = 0
                self.botao_matriz[i][j].config(text="0", bg="SystemButtonFace")

        torres_adicionadas = 0
        while torres_adicionadas < self.torres_aleatorias:
            x = random.randint(0, self.n - 1)
            y = random.randint(0, self.n - 1)

            if (x == self.n - 1 and y == self.n - 1) or (x == self.n - 2 and y == self.n - 2):
                continue

            if self.jogo.tabuleiro[x][y] == 0:
                self.jogo.adicionar_torre(x, y)
                self.botao_matriz[x][y].config(text="T", bg="red")
                torres_adicionadas += 1

    def encontrar_menor_dano(self):
        start_time = time.time()
        try:
            menor_dano, melhor_caminho = self.jogo.encontrar_menor_dano()
            for x, y in melhor_caminho:
                if x == 0 and y == 0:
                    self.botao_matriz[x][y].config(bg="green", text="Início")
                else:
                    self.botao_matriz[x][y].config(bg="green", text=f"D: {self.jogo.matriz_dano[x][y]}")
            elapsed_time = time.time() - start_time
            cpu_usage = os.getloadavg()[0] if os.name != 'nt' else "Monitoramento indisponível no Windows"
            # messagebox.showinfo("Resultado", f"Menor Dano: {menor_dano}\nTempo: {elapsed_time:.2f}s\nCPU: {cpu_usage}")
            messagebox.showinfo("Resultado", f"Menor Dano: {menor_dano}\nTempo: {elapsed_time:.2f}")
        except KeyError:
            messagebox.showerror("Erro", "Caminho não encontrado")

# Inicializando a interface
root = tk.Tk()
root.title("Jogo Tower Defense")
app = TowerDefenseInterface(root)
root.mainloop()
