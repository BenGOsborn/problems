class Solution:
    def networkDelayTime(self, times, n, k):
        pass


tests = [
    (([[2, 1, 1], [2, 3, 1], [3, 4, 1]], 4, 2), 2),
    (([[1, 2, 1]], 2, 1), 1),
    (([[1, 2, 1]], 2, 2), -1)
]

for test in tests:
    print(Solution().networkDelayTime(*test[0]), test[1])
