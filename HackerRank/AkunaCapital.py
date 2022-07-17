def convert_to_tuple(elem):
    # Return element and number of 1's
    count = 0

    bin_digit = bin(elem)[2:]
    for char in bin_digit:
        if char == "1":
            count += 1

    return (elem, count)

def rearrange(elements):
    mapped = []

    for elem in elements:
        mapped.append(convert_to_tuple(elem))
    
    return [x[0] for x in sorted(mapped, key=lambda x: (x[1], x[0]))]


elements = [1, 2, 3, 4, 89]

print(rearrange(elements))

def dfs(seen, graph, node):
    if node in seen:
        return 0

    seen[node] = True

    for elem in graph[node]:
        dfs(seen, graph, elem)

    return 1

def minOperations(comp_nodes, comp_from, comp_to):
    if len(comp_from) < comp_nodes - 1:
        return -1

    graph = {}
    for i, j in zip(comp_from, comp_to):
        if i in graph:
            graph[i].add(j)
        else:
            graph[i] = set({j})

        if j in graph:
            graph[j].add(i)
        else:
            graph[j] = set({i})

    seen = {}

    return sum(dfs(seen, graph, node) for node in comp_from) - 1

print(minOperations(4, [1, 1, 3], [2, 3, 2]))