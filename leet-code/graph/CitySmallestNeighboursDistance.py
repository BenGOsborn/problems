class Solution:
    def findTheCity(self, n, edges, distanceThreshold):
        pass


tests = [
    ((4, [[0, 1, 3], [1, 2, 1], [1, 3, 4], [2, 3, 1]], 4), 3),
    ((5, [[0, 1, 2], [0, 4, 8], [1, 2, 3], [1, 4, 2], [2, 3, 1], [3, 4, 1]], 2), 0)
]

for test in tests:
    print(Solution().findTheCity(*test[0]), test[1])
