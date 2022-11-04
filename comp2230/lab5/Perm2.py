def permutations(n, seen, prev):
    if len(prev) == n:
        print(prev)
        return

    for i in range(1, n + 1):
        if not seen[i - 1]:
            seen[i - 1] = True
            permutations(n, seen, prev + str(i))
            seen[i - 1] = False


n = 10
seen = [False] * n

permutations(n, seen, "")
