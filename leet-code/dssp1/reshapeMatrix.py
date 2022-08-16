tests = [([[1, 2], [3, 4]], 1, 4), ([[1, 2], [3, 4]], 2, 4)]


def reshape(mat, r, c):
    if len(mat) * len(mat[0]) != r * c:
        return mat

    out = []

    for i in range(r):
        temp = []

        for j in range(c):
            temp.append(0)

        out.append(temp)

    for i in range(len(mat)):
        for j in range(len(mat[0])):
            position = i * len(mat[0]) + j

            row_index = position // c
            col_index = position % c

            out[row_index][col_index] = mat[i][j]

    return out


test = tests[1]
print(reshape(test[0], test[1], test[2]))
