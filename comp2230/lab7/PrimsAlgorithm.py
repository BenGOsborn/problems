import collections
import heapq


def prims(edges):
    graph = collections.defaultdict(list)
    for edge in edges:
        graph[edge[0]].append((edge[1], edge[2]))
        graph[edge[1]].append((edge[0], edge[2]))

    tree = collections.defaultdict(list)

    heap = [(edges[0][2], edges[0][:2])]
    while heap:
        elem = heapq.heappop(heap)[1]

        if elem[0] in tree and elem[1] in tree:
            continue

        tree[elem[0]].append(elem[1])
        tree[elem[1]].append(elem[0])

        for item in graph[elem[1]]:
            heapq.heappush(heap, (item[1], [elem[1], item[0]]))

    return tree


graph = [
    [0, 1, 4],
    [0, 7, 8],
    [1, 2, 8],
    [1, 7, 11],
    [2, 8, 2],
    [7, 8, 7],
    [7, 6, 1],
    [8, 6, 6],
    [6, 5, 2],
    [2, 5, 4],
    [2, 3, 7],
    [3, 5, 14],
    [3, 4, 9],
    [4, 5, 10]
]

print(prims(graph))
