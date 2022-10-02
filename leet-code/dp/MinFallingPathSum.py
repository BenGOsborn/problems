# Algorithm
# - Use a bottom up approach to generate the minimum path sum of the elements at every level
# - From there, we just need to return the minimum path sum for the top row and then return it

class Solution:
    def minFallingPathSum(self, matrix):
        cache = []
        for i in range(len(matrix)):
            temp = []
            for j in range(len(matrix[0])):
                temp.append(None)
            cache.append(temp)

        for i in range(len(matrix) - 1, -1, -1):
            for j in range(len(matrix[0])):
                if i == len(matrix) - 1:
                    cache[i][j] = matrix[i][j]
                else:
                    cache[i][j] = matrix[i][j] + cache[i + 1][j]

                    if j > 0:
                        cache[i][j] = min(
                            cache[i][j], matrix[i][j] + cache[i + 1][j - 1])
                    if j < len(matrix[0]) - 1:
                        cache[i][j] = min(
                            cache[i][j], matrix[i][j] + cache[i + 1][j + 1])

        return min(cache[0])


tests = [
    ([[2, 1, 3], [6, 5, 4], [7, 8, 9]], 13),
    ([[-19, 57], [-40, -5]], -59)
]

for test in tests:
    print(Solution().minFallingPathSum(test[0]), test[1])
