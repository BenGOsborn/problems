def zero_row_col(array, row, col):
    for i in range(len(array[row])):
        array[row][i] = 0

    for i in range(len(array)):
        array[i][col] = 0


def zero_matrix(array):
    seen_rows = {}
    seen_cols = {}

    for i in range(len(array)):
        if i in seen_rows:
            continue

        for j in range(len(array[i])):
            if j in seen_cols:
                continue

            if array[i][j] == 0:
                zero_row_col(array, i, j)
                seen_rows[i] = True
                seen_cols[j] = True
                break


tests = [[[1, 2, 0, 4], [1, 0, 2, 3], [2, 5, 1, 1], [0, 2, 2, 1]],
         [[1, 2, 5, 4], [1, 0, 2, 3], [2, 5, 1, 1], [3, 2, 2, 1]]]

for test in tests:
    zero_matrix(test)
    print(test)
