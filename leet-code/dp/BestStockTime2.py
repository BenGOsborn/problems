class Solution:
    def maxProfit(self, pricesList):
        pass


tests = [
    ([7, 1, 5, 3, 6, 4], 7),
    ([1, 2, 3, 4, 5], 4),
    ([7, 6, 4, 3, 1], 0)
]

for test in tests:
    print(Solution().maxProfit(test[0]), test[1])
