class Solution:
    def coinChange(self, coins, amount):
        pass


tests = [
    (([1, 2, 5], 11), 3),
    (([2], 3), -1),
    (([1], 0), 0)
]

for test in tests:
    print(Solution().coinChange(*test[0]), test[1])
