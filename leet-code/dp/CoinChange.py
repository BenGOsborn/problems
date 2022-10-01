# Algorithm
# - Assuming that amounts is ordered in ascending order
# - Start from the right part of the array, and decrement the amount by the given coin if possible, then move onto the next part recursively, keeping track of how many coins were used
# - Return the amount that used the least coins - if we have -1, we must continue on to the next one
# - Cache the result for each amount and coin index
# - Base case if we hit i == -1 then we need to return -1, and if we hit amount = 0 then we return 0

class Solution:
    def coin_change(self, coins, amount, i):
        if amount == 0:
            return 0

        # **** How do I handle the -1 case... ????

        mn = -1
        j = 0

        while amount >= coins[i]:
            out = self.coin_change(coins, amount, i - 1)

            if out != -1:
                if mn == -1:
                    mn = j + out
                else:
                    mn = min(mn, j + out)

            j += 1
            amount -= coins[i]

        if mn == -1:
            return -1
        return mn

    def coinChange(self, coins, amount):
        return self.coin_change(coins, amount, len(coins) - 1)


tests = [
    (([1, 2, 5], 11), 3),
    (([2], 3), -1),
    (([1], 0), 0)
]

for test in tests:
    print(Solution().coinChange(*test[0]), test[1])
