class Solution:
    def findTheCity(self, n, edges, distanceThreshold):
        matrix = []
        for _ in range(n):
            temp = []
            for _ in range(n):
                temp.append(-1)
            matrix.append(temp)

        for u, v, w in edges:
            matrix[u][v] = w
            matrix[v][u] = w

        for i in range(n):
            matrix[i][i] = 0

        for k in range(n):
            for i in range(n):
                for j in range(n):
                    if matrix[i][k] == -1 or matrix[k][j] == -1:
                        continue

                    updated = matrix[i][k] + matrix[k][j]
                    if matrix[i][j] != -1:
                        updated = min(matrix[i][j], updated)
                    matrix[i][j] = updated

        mn = -1
        city = -1

        for i, row in enumerate(matrix):
            amount = 0
            for col in row:
                if col <= distanceThreshold and col >= 0:
                    amount += 1
            if mn == -1 or amount <= mn:
                mn = amount
                city = i

        return city


tests = [
    ((4, [[0, 1, 3], [1, 2, 1], [1, 3, 4], [2, 3, 1]], 4), 3),
    ((5, [[0, 1, 2], [0, 4, 8], [1, 2, 3], [1, 4, 2], [2, 3, 1], [3, 4, 1]], 2), 0)
]

for test in tests:
    print(Solution().findTheCity(*test[0]), test[1])
