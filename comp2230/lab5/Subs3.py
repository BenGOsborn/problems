def subsets3(base, n, current):
    print(current)

    for i in range(base, n + 1):
        subsets3(i + 1, n, current + str(i))


subsets3(1, 3, "")
