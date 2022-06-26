tests = [[7, 1, 5, 3, 4, 6], [7, 6, 4, 3, 1]]


def max_profit(prices):
    i = 0  # Min
    j = 0  # Max

    max_profit = 0

    for index in range(len(prices)):
        if prices[index] < prices[i]:
            i = index
            j = index
        if prices[index] > prices[j]:
            j = index

        current_min = prices[i]
        current_max = prices[j]

        max_profit = max(current_max - current_min, max_profit)

    return max_profit


test = tests[1]
print(max_profit(test))
