class Solution:
    def minFallingPathSum(self, matrix):
        pass


tests = [
    ([[2, 1, 3], [6, 5, 4], [7, 8, 9]], 13),
    ([[-19, 57], [-40, -5]], -59)
]

for test in tests:
    print(Solution().minFallingPathSum(test[0]), test[1])
