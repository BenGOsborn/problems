def encode():
    pass


total_calls = 0


def knapsack(current_value, current_weight, remaining, max_weight):
    current_max = current_value

    global total_calls
    total_calls += 1

    for i, elem in enumerate(remaining):
        new_weight = current_weight + elem[0]
        if new_weight > max_weight:
            continue

        out = knapsack(current_value + elem[1], new_weight,
                       remaining[:i] + remaining[i+1:], max_weight)

        if out > current_max:
            current_max = out

    return current_max


available = [(2, 5), (3, 8), (1, 7), (2, 15)]
weight = 5
print(knapsack(0, 0, available, weight))
print(total_calls)
