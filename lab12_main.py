import lab12 as lab
import sys
import os
import pdb
sys.path.insert(0, os.getcwd())

ALTURA_TABULEIRO = 10
LARGURA_TABULEIRO = 10

matriz = []
for j in range(0, ALTURA_TABULEIRO):
    matriz.append([])
    for i in range(0, LARGURA_TABULEIRO):
        matriz[-1].append(0)

n = int(input())
pontos = 0

for i in range(0, n):
    l, a, x, desl, rot = tuple(map(int, input().split(' ')))
    l, a, x = lab.atualiza_posicao(l, a, x, desl, rot)
    y = lab.encontra_y(matriz, l, x)
    valido = lab.posicao_final_valida(a, y)

    if valido:
        lab.posiciona_bloco(matriz, l, a, x, y)
        # pdb.set_trace()
        pontos += lab.atualiza_matriz(matriz)
        print("bloco {}".format(i))
        print("{} pontos".format(pontos))
        print('{}'.format('\n'.join(
            [''.join(['{}'.format(item) for item in row])
             for row in reversed(matriz)])))
    else:
        break
