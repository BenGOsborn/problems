# Algorithm
# - Simple DFS for every node (and we will find the connected graphs)
# - We will go through our list and we will then run an explore function which will mark all elements and increase the counter
# - We will then loop over the entire 2d array, and if we find a node we have not previously explored through a DFS, increment our counter, explore it
# - At the end, return the total amount of islands we have found

class Solution:
    def bfs(self, grid, i, j):
        queue = [[i, j]]

        while len(queue):
            popped = queue.pop(0)
            print(popped)

            if popped[0] < 0 or popped[0] >= len(grid) or popped[1] < 0 or popped[1] >= len(grid[0]) or grid[i][j] == "#" or grid[i][j] == "0":
                continue

            grid[i][j] = "#"

            for y, x in [[-1, 0], [1, 0], [0, -1], [0, 1]]:
                queue.append([i + y, j + x])

    def numIslands(self, grid):
        islands = 0

        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] != "#" and grid[i][j] != "0":
                    islands += 1
                    self.bfs(grid, i, j)

        return islands


tests = [
    ([
        ["1", "1", "1", "1", "0"],
        ["1", "1", "0", "1", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "0", "0", "0"]
    ], 1),
    # ([
    #     ["1", "1", "0", "0", "0"],
    #     ["1", "1", "0", "0", "0"],
    #     ["0", "0", "1", "0", "0"],
    #     ["0", "0", "0", "1", "1"]
    # ], 3),
]

for grid, sol in tests:
    print(Solution().numIslands(grid) == sol)
