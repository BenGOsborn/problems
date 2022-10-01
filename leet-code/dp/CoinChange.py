# https://www.youtube.com/watch?v=H9bfqozjoqs&t=469s, https://leetcode.com/problems/coin-change/

# Algorithm
# - Bottom up solution: for each amount we go to, we will calculate the minimum amount of coins needed to get to the next level

class Solution:
    def coinChange(self, coins, amount):
        cache = [-1] * (amount + 1)

        cache[0] = 0

        for i in range(1, amount + 1):
            mn = -1
            for elem in coins:
                if i >= elem:
                    prev = cache[i - elem]
                    if prev == -1:
                        continue
                    elif mn == -1:
                        mn = 1 + prev
                    else:
                        mn = min(mn, 1 + prev)
            cache[i] = mn

        return cache[amount]


tests = [
    (([1, 2, 5], 11), 3),
    (([2], 3), -1),
    (([1], 0), 0)
]

for test in tests:
    print(Solution().coinChange(*test[0]), test[1])
