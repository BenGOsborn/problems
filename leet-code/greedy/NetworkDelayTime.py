# Algorithm
# - Implement dijkstras to find the shortest path to every node
# - Return the minimum of the shortest paths (including -1)


import collections
import heapq


class Solution:
    def networkDelayTime(self, times, n, k):
        edges = collections.defaultdict(list)
        for u, v, w in times:
            edges[u].append((v, w))

        heap = [(0, k)]
        visited = set()
        t = 0

        while heap:
            elem = heapq.heappop(heap)

            if elem[1] in visited:
                continue
            visited.add(elem[1])
            t = max(t, elem[0])

            for item in edges[elem[1]]:
                heapq.heappush(heap, (elem[0] + item[1], item[0]))

        return t if len(visited) == n else -1


tests = [
    (([[2, 1, 1], [2, 3, 1], [3, 4, 1]], 4, 2), 2),
    (([[1, 2, 1]], 2, 1), 1),
    (([[1, 2, 1]], 2, 2), -1),
    (([[1, 2, 1], [2, 1, 3]], 2, 2), 3),
]

for test in tests:
    print(Solution().networkDelayTime(*test[0]), test[1])
