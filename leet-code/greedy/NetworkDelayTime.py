from queue import PriorityQueue

# Algorithm
# - Implement djikstras to find the shortest path to every node
# - Return the minimum of the shortest paths (including -1)


class Solution:
    def networkDelayTime(self, times, n, k):
        graph = {}
        for time in times:
            if time[0] not in graph:
                graph[time[0]] = [time]
            else:
                graph[time[0]].append(time)

        print(graph)

        cache = [-1] * n

        cache[k - 1] = 0
        pq = PriorityQueue()
        if k in graph:
            for elem in graph[k]:
                pq.put((-elem[2], elem))

        while not pq.empty():
            elem = pq.get()[1]

            updated = cache[elem[0] - 1] + elem[2]
            if cache[elem[1] - 1] != -1:
                updated = min(cache[elem[1] - 1], updated)
            else:
                pq.put((-elem[2], elem))
            cache[elem[1] - 1] = updated

        if min(cache) == -1:
            return -1
        return max(cache)


tests = [
    (([[2, 1, 1], [2, 3, 1], [3, 4, 1]], 4, 2), 2),
    # (([[1, 2, 1]], 2, 1), 1),
    # (([[1, 2, 1]], 2, 2), -1)
]

for test in tests:
    print(Solution().networkDelayTime(*test[0]), test[1])
