# RA 206341

import itertools


def calc_profit(movements, values):
    profit = 0
    for day, vals in enumerate(movements):
        if vals[0] >= 0:
            profit -= values[vals[0]][day]
        if vals[1] >= 0:
            profit += values[vals[1]][day]
    return profit


def valid_comb(comb):
    current_company = -1
    sold_companies = []
    for day in comb:
        if day[1] != -1:
            if current_company == -1 or current_company != day[1]:
                return False
            if day[1] == current_company:
                current_company = -1
                sold_companies.append(day[1])
        if current_company == -1:
            if day[0] != -1:
                if day[0] not in sold_companies:
                    current_company = day[0]
                else:
                    return False
        elif day[0] != -1:
            return False
    return True


# valores das ações para cada dia
# são 4 empresas, dentro vão ter valores para cada dia 0 <= x <= d
values = [[], [], [], []]

d = int(input())

for j in range(4):
    for i in range(d):
        values[j].append(float(input()))

perms = list(itertools.permutations(range(-1, 4), 2))
perms.append((-1, -1))
combinations = itertools.product(perms, repeat=d)
filtered_combs = []
for comb in combinations:
    if valid_comb(comb):
        filtered_combs.append(comb)


# capitalismo HUAHUAHUAHUA
max_profit = 0
max_profit_comb = [[-1, -1]] * d
for comb in filtered_combs:
    profit = calc_profit(comb, values)
    if profit > max_profit:
        max_profit = profit
        max_profit_comb = comb

c = [-1]*4
v = c.copy()

for i, day in enumerate(max_profit_comb):
    if day[0] != -1:
        c[day[0]] = i + 1
    if day[1] != -1:
        v[day[1]] = i + 1

for i in range(4):
    if c[i] != -1 and v[i] != -1:
        print("acao %d: compra %d, venda %d, lucro %.2f" %
              (i + 1, c[i], v[i],
               (values[i][v[i] - 1] - values[i][c[i] - 1])))

print("Lucro: %.2f" % max_profit)
