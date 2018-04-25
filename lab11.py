# RA 206341

# super programao pra simular os zumbizao
# feito com muito elegância e bom gosto
# o cógido é autoexplicativo

from copy import deepcopy


def surrounding(i, j, madriz):
    return [madriz[i + ni][j + nj] for (ni, nj) in [
                [-1, -1], [-1, 0], [-1, 1],
                [0, -1],           [0, 1],
                [1, -1],  [1, 0],  [1, 1]]]


def nxtx(i, j, madriz):
    sur = surrounding(i, j, madriz)
    x = madriz[i][j]
    if x == 1 and sur.count(2) >= 1:
        return 2
    if x == 2 and sur.count(1) >= 2:
        return 0
    if x == 2 and sur.count(1) == 0:
        return 0
    if x == 0 and sur.count(1) == 2:
        return 1
    return x


(m, n) = [int(x) for x in input().split()]
it = int(input())

madriz = [[0 for _ in range(n + 2)]]

for _ in range(m):
    madriz.append([0] + [int(x) for x in input().split()] + [0])

madriz.append([0 for _ in range(n + 2)])

madriz2 = deepcopy(madriz)

print("iteracao", 0)
for i in range(m):
    for j in range(n):
        print(madriz[i + 1][j + 1], end="")
    print()

for d in range(it):
    print("iteracao", d + 1)
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            x = nxtx(i, j, madriz)
            madriz2[i][j] = x
            print(x, end="")
        print()
    madriz = deepcopy(madriz2)
