# Algorithm
# - We will define the subproblems as getting the maximum profit between any two elements
# - We will work backwards, and will store the maximum result for each as well as the total maximum amount obtainable (which will begin at zero)
# - We will only allow this to be updated if the element in front of it is greater than the element we are previously on

class Solution:
    # def max_profit(self, prices, i, cache):
    #     if i == len(prices) - 1:
    #         cache[i] = 0
    #         return cache[i]

    #     mx = 0

    #     for j in range(i + 1, len(prices)):
    #         elem = cache[j]
    #         if elem == -1:
    #             elem = self.max_profit(prices, j, cache)
    #         mx = max(mx, prices[j] - prices[i] + elem, elem)

    #     cache[i] = mx
    #     return cache[i]

    # def maxProfit(self, pricesList):
    #     return self.max_profit(pricesList, 0, [-1] * len(pricesList))

    def maxProfit(self, pricesList):
        total = 0

        for i in range(1, len(pricesList)):
            if pricesList[i] > pricesList[i - 1]:
                total += pricesList[i] - pricesList[i - 1]

        return total


tests = [
    ([7, 1, 5, 3, 6, 4], 7),
    ([1, 2, 3, 4, 5], 4),
    ([7, 6, 4, 3, 1], 0)
]

for test in tests:
    print(Solution().maxProfit(test[0]), test[1])
