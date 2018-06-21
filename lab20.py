#!/usr/bin/env python3

import copy

# Funcao: print_sudoku
# Essa funcao ja esta implementada no arquivo lab20_main.py
# A funcao imprime o tabuleiro atual do sudoku de forma animada, isto e,
# imprime o tabuleiro e espera 0.1s antes de fazer outra modificacao.
# Voce deve chamar essa funcao a cada modificacao na matriz resposta, assim
# voce tera uma animacao similar a apresentada no enunciado.
# Essa funcao nao tem efeito na execucao no Susy, logo nao ha necessidade de
# remover as chamadas para submissao.
from lab20_main import print_sudoku


def isvalido(resposta):
    resposta = copy.deepcopy(resposta)
    for i in range(9):
        nu = list(filter((0).__ne__, resposta[i]))
        rs = set(nu)
        if len(nu) != len(rs):
            return False
    for i in range(9):
        nu = [resposta[j][i] for j in range(9) if resposta[j][i] != 0]
        rs = set(nu)
        if len(nu) != len(rs):
            return False
    return True

# Funcao: resolve
# Resolve o Sudoku da matriz resposta.
# Retorna True se encontrar uma resposta, False caso contrario


def resolve(resposta):
    if not isvalido(resposta):
        return False
    print_sudoku(resposta)
    for i in range(9):
        for j in range(9):
            if resposta[i][j] == 0:
                for k in range(1, 9):
                    resposta[i][j] = k
                    nu = copy.deepcopy(resposta)
                    if (resolve(nu)):
                        for l in range(9):
                            resposta[l] = nu[l]
                        return True
