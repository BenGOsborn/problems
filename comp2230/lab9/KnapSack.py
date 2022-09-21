
# def knapsack(current_value, current_weight, remaining, max_weight):
#     current_max = current_value

#     for i, elem in enumerate(remaining):
#         new_weight = current_weight + elem[0]
#         if new_weight > max_weight:
#             continue

#         out = knapsack(current_value + elem[1], new_weight,
#                        remaining[:i] + remaining[i+1:], max_weight)

#         if out > current_max:
#             current_max = out

#     return current_max


weights = [2, 3, 1, 2]
values = [5, 8, 7, 15]

weight = 5
n = len(values)

cache = [[-1 for _ in range(weight + 1)] for _ in range(n + 1)]


def knapsack(weights, values, weight, n):

    if n == 0 or weight == 0:
        return 0

    if cache[n][weight] != -1:
        return cache[n][weight]

    if weights[n - 1] <= weight:
        cache[n][weight] = max(values[n - 1] + knapsack(weights, values, weight -
                               weights[n - 1], n - 1), knapsack(weights, values, weight, n - 1))
    else:
        cache[n][weight] = knapsack(weights, values, weight, n - 1)

    return cache[n][weight]


print(knapsack(weights, values, weight, n))
