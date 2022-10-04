class Solution:
    def checkIfPrerequisite(self, numCourses, prerequisites, queries):
        matrix = []
        for _ in range(numCourses):
            temp = []
            for _ in range(numCourses):
                temp.append(0)
            matrix.append(temp)

        for u, v in prerequisites:
            matrix[u][v] = 1

        for k in range(numCourses):
            for i in range(numCourses):
                if matrix[i][k] == 1:
                    for j in range(numCourses):
                        if matrix[k][j] == 1:
                            matrix[i][j] = 1

        out = []
        for query in queries:
            out.append(matrix[query[0]][query[1]] == 1)

        return out


tests = [
    ((2, [[1, 0]], [[0, 1], [1, 0]]), [False, True]),
    ((2, [], [[1, 0], [0, 1]]), [False, False]),
    ((3, [[1, 2], [1, 0], [2, 0]], [[1, 0], [1, 2]]), [True, True])
]

for test in tests:
    print(Solution().checkIfPrerequisite(*test[0]), test[1])
