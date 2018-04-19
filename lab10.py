# RA 206341

text = input().split()

cases = {
    "d": lambda _, arg: filter((lambda word: word.lower() != arg), text),
    "i": lambda _, arg: map((lambda word: word[::-1] if word.lower() == arg else word), text),
    "r": lambda _, arg1, arg2: map((lambda word: arg2 if word.lower() == arg1 else word), text)
}


def inputs():
    x = input().lower()
    while x != "q":
        if x == "d":
            yield (x, input().lower())
        if x == "i":
            yield (x, input().lower())
        if x == "r":
            yield (x, input().lower(), input())
        x = input().lower()


for e in inputs():
    text = list(cases[e[0]](*e))
    print(" ".join(text))
