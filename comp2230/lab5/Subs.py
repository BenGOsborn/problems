def subsets(n, base, current):
    print(current)

    if len(current) == n:
        return

    for i in range(base, n + 1):
        current.append(i)

        subsets(n, i + 1, current)

        current.pop(-1)


subsets(3, 1, [])
