def subsets(n, base, current):
    print(current)

    if len(current) == n:
        return

    for i in range(base, n + 1):
        current.append(i)

        subsets(n, i + 1, current)

        current.pop(-1)


def subsets2(n, base, current):
    print(current)

    if len(current) == n:
        return

    for i in range(base, n + 1):
        subsets2(n, i + 1, current + str(i))


# subsets(3, 1, [])
subsets2(3, 1, "")
