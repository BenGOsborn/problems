def coin_change(denom, amount):
    out = [0] * len(denom)

    i = len(denom) - 1

    while amount > 0 and i >= 0:
        quantity = amount // denom[i]

        out[i] = quantity

        amount -= (quantity * denom[i])
        i -= 1

    return out


denom = [1, 2, 5, 10, 20, 50, 100, 200]

tests = [
    (denom, 105),
    (denom, 240),
    (denom, 30),
    (denom, 85)
]

for test in tests:
    print(coin_change(*test))
