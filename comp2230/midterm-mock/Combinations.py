def row_combinations(row_size, i, n, current):
    if len(current) == row_size:
        print(current)
        return

    for i in range(i, n + 1):
        row_combinations(row_size, i + 1, n, current + [i])


def combinations(n):
    for i in range(n):
        row_combinations(i + 1, 1, n, [])


combinations(3)
