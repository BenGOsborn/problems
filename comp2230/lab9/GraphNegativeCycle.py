# Algorithm
# - Record the weight from each node to the next node inside of the vertex
# - If we get to a cycle, subtract the cumulative weight from the last node to the original vertex entry weight - if it is negative, we have a negative cycle, else continue
# - If we can't find anything, return false


def graph_negative_cycle_rec(entry, prev_weight, graph, cum_weights):
    if entry in cum_weights:
        if prev_weight - cum_weights[entry] < 0:
            return True
        return False

    cum_weights[entry] = prev_weight

    for elem in graph[entry]:
        out = graph_negative_cycle_rec(
            elem[1], prev_weight + elem[0], graph, cum_weights)
        if out:
            return True

    return False


def graph_negative_cycle(graph):
    cum_weights = {}

    for elem in graph:
        if elem not in cum_weights:
            out = graph_negative_cycle_rec(elem, 0, graph, cum_weights)
            if out:
                return True

    return False


tests = [
    {"a": [(2, "b"), (4, "c")], "b": [(4, "a")], "c": []},
    {"a": [(2, "b"), (4, "c")], "b": [(-4, "a")], "c": []}
]

for test in tests:
    print(graph_negative_cycle(test))
