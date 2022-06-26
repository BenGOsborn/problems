tests = [([[1, 2], [3, 4]], 1, 4)]


def reshape(matrix, rows, cols):
    if len(matrix) * len(matrix[0]) != rows * cols:
        return matrix

    out = []

    for i in range(rows):
        temp = []

        for j in range(cols):
            temp.append(0)

        out.append(temp)

    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            position = i * len(matrix[0]) + j

            row_index = position // rows
            col_index = position % cols

            print(position, row_index, col_index)

            # out[][] = matrix[i][j]

    return out


test = tests[0]
print(reshape(test[0], test[1], test[2]))
