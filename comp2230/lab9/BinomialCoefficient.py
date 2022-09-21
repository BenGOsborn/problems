def encode(n, k):
    return f"{n},{k}"


def bin_co(n, k, cache):
    encoded = encode(n, k)

    if encoded in cache:
        return cache[encoded]

    if k == 0 or k == n:
        return 1

    cache[encoded] = bin_co(n - 1, k, cache) + bin_co(n - 1, k - 1, cache)

    return cache[encoded]


n = 2
k = 1
print(bin_co(n, k, {}))
