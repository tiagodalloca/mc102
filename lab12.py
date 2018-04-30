#!/usr/bin/env python3

# Laboratorio 12 - Tetris
# Nome: Tiago Pereira Dall'Oca
# RA: 206341

from functools import reduce

ALTURA_TABULEIRO = 10
LARGURA_TABULEIRO = 10

# Funcao: atualiza_posicao
#
# Parametros:
#      l: largura do bloco que ira cair
#      a: altura do bloco que ira cair
#      x: posicao horizontal inicial do bloco que ira cair
#   desl: deslocamento horizontal a ser aplicado ao bloco
#       (positivo para direita, negativo para a esquerda)
#    rot: 1 se deve rotacionar o bloco, 0 caso contrario
#
# Retorno:
#   Nova largura, altura e posicao horizontal.
#


def atualiza_posicao(l, a, x, desl, rot):
    if rot:
        if x + desl + a < LARGURA_TABULEIRO:
            if x + desl > -1:
                return a, l, x + desl
            else:
                return a, l, 0
        else:
            return a, l, LARGURA_TABULEIRO - a
    elif x + desl + l < LARGURA_TABULEIRO:
        if x + desl > -1:
            return l, a, x + desl
        else:
            return l, a, 0
    else:
        return l, a, LARGURA_TABULEIRO - l

# Funcao: encontra_y
#
# Parametros:
#    mat: matriz representando o tabuleiro
#      l: largura do bloco que ira cair
#      x: posicao horizontal do bloco que ira cair
#
# Retorno:
#   altura final y do canto inferior esquerdo do bloco apos
#   este descer o maximo possivel
#


def encontra_y(mat, l, x):
    return max([i + 1 for j in range(x, x + l)
                for i in range(len(mat))
                if mat[i][j]] + [0])

# Funcoes: posicao_final_valida
#
# Parametros:
#      a: altura do bloco que caiu
#      y: altura final do bloco que caiu
#
# Retorno:
#   1 se o bloco naquela posicao estiver contido dentro do tabuleiro,
#   ou 0 caso contrario.
#


def posicao_final_valida(a, y):
    return 1 if a + y <= ALTURA_TABULEIRO else 0

# Funcoes: posiciona_bloco
#
# Parametros:
#    mat: matriz do tabuleiro
#      l: largura do novo bloco
#      a: altura do novo bloco
#      x: posicao horizontal do novo bloco
#      y: altura final do novo bloco
#
#      Deve preencher com 1s as novas posições ocupadas pelo bloco que caiu
# Retorno:
#   NULL
#


def posiciona_bloco(mat, l, a, x, y):
    for i in range(y, y + a):
        for j in range(x, x + l):
            mat[i][j] = 1

    # Funcoes: atualiza_matriz
    #
    #    mat: matriz do tabuleiro
    #
    #       Deve remover as linhas totalmente preenchidas do tabuleiro copiando
    #       linhas posicionadas acima.
    # Retorno:
    #  retorna o numero de linhas totalmente preenchidas que foram removidas
    #  apos a atualizacao do tabuleiro.
    #


def atualiza_matriz(mat):
    oslines = [i for i in range(len(mat))
               if reduce(lambda x, y: x and y, mat[i])][::-1]
    for i in oslines:
        del mat[i]
    for _ in oslines:
        mat.append([0]*len(mat[0]))
    return len(oslines)
