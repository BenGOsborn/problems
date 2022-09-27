class Solution:
    def spiralOrder(self, matrix):
        min_i = 0
        max_i = len(matrix)
        min_j = 0
        max_j = len(matrix[0])

        out = []

        while min_i < max_i and min_j < max_j:
            for j in range(min_j, max_j):
                out.append(matrix[min_i][j])

            min_i += 1

            for i in range(min_i, max_i - 1):
                out.append(matrix[i][max_j - 1])

            max_j -= 1

            if (min_i < max_i):
                for j in range(max_j, min_j - 1, -1):
                    out.append(matrix[max_i - 1][j])

                max_i -= 1

            if (min_j < max_j):
                for i in range(max_i - 1, min_i - 1, -1):
                    out.append(matrix[i][min_j])

                min_j += 1

        return out


tests = [
    ([[1, 2, 3], [4, 5, 6], [7, 8, 9]], [1, 2, 3, 6, 9, 8, 7, 4, 5]),
    ([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]],
     [1, 2, 3, 4, 8, 12, 11, 10, 9, 5, 6, 7]),
    ([[2, 3]], [2, 3])
]

for test in tests:
    print(Solution().spiralOrder(test[0]))
    print(test[1])
    print()
