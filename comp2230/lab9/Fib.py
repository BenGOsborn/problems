import time


def fib(n, cache):
    if n in cache:
        return cache[n]

    if n == 0:
        return 0
    if n == 1:
        return 1

    cache[n] = fib(n-1, cache) + fib(n-2, cache)

    return cache[n]


def fib_no_cache(n):
    if n == 0:
        return 0
    if n == 1:
        return 1

    return fib_no_cache(n-1) + fib_no_cache(n-2)


val = 30

start = time.time()

print(fib(val, {}))
print((time.time() - start) * 1000, "ms")

start = time.time()

print(fib_no_cache(val))
print((time.time() - start) * 1000, "ms")
