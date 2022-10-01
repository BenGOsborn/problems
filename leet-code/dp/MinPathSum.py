# Algorithm
# - For each square starting from the top left, calculate each cell as the minimum of its current value + what is above and to the left of it
# - When we get to the bottom right node, we will return this calculated value

class Solution:
    def minPathSum(self, grid):
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if i == 0 and j == 0:
                    continue
                elif i == 0:
                    grid[i][j] += grid[i][j - 1]
                elif j == 0:
                    grid[i][j] += grid[i - 1][j]
                else:
                    grid[i][j] = min(grid[i - 1][j] + grid[i]
                                     [j], grid[i][j - 1] + grid[i][j])

        return grid[len(grid) - 1][len(grid[0]) - 1]


tests = [
    ([[1, 3, 1], [1, 5, 1], [4, 2, 1]], 7),
    ([[1, 2, 3], [4, 5, 6]], 12)
]

for test in tests:
    print(Solution().minPathSum(test[0]), test[1])
