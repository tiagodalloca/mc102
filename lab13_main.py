import sys
import os
import lab13 as lab
sys.path.insert(0, os.getcwd())

# Função Main

# Ler a quantidade de jogadores
n = int(input())
tabela = []
# Ler os nomes dos jogadores e inicializa a tabela
for i in range(n):
    nomeTime = input()
    # inicializa os pontos, numero de vitorias, saldo de gols, gols pros
    # com '0'
    time = [nomeTime, 0, 0, 0, 0]
    tabela.append(time)

# calculo da quantidade de jogos do campeonato
qtdJogos = (n * (n - 1)) / 2
qtdJogos = int(qtdJogos)

# Ler os jogos e atualiza a tabela
for i in range(qtdJogos):
    jogo = input()
    lab.atualizaTabela(tabela, jogo)

# Ordena a tabela
lab.ordenaTabela(tabela)

# Imprime a tabela
# import pdb
# pdb.set_trace()
lab.imprimeTabela(tabela)
