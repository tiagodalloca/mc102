# RA 206341


def read_int():
    return float(input())


def e_to_km(e):
    return 0.1764*e


D = read_int()
A = read_int()

E = D*(360/A)

print(E)
print(e_to_km(E))
