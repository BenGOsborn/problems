# https://www.youtube.com/watch?v=H9bfqozjoqs&t=469s

class Solution:
    def coin_change(self, coins, amount, cache):
        if amount in cache:
            return cache[amount]

        if amount == 0:
            cache[amount] = 0
            return 0
        if amount < 0:
            cache[amount] = -1
            return -1

        num = -1

        for elem in coins:
            out = self.coinChange(coins, amount - elem)
            if out == -1:
                continue

            if num == -1:
                num = out
            else:
                num = min(num, out)

        if num == -1:
            cache[amount] = -1
            return -1
        cache[amount] = num + 1
        return num + 1

    def coinChange(self, coins, amount):
        return self.coin_change(coins, amount, {})


tests = [
    (([1, 2, 5], 11), 3),
    (([2], 3), -1),
    (([1], 0), 0)
]

for test in tests:
    print(Solution().coinChange(*test[0]), test[1])
