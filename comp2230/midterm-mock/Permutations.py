# Algorithm (using backtracking)

def permute(available, current, out):
    if len(available) == 0:
        out.append(current)

    for i, elem in enumerate(available):
        available_cpy = available[:i] + available[i + 1:]
        permute(available_cpy, current + [elem], out)


n = 5

test = [x for x in range(0, n)]
out = []

permute(test, [], out)

print(out)
