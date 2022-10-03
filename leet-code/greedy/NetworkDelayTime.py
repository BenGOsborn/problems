from queue import PriorityQueue

# Algorithm
# - Implement djikstras to find the shortest path to every node
# - Return the minimum of the shortest paths (including -1)


class Solution:
    def djikstras(self, graph, start, cache):
        if start in graph:
            while not graph[start].empty():
                print(graph[start])

    def networkDelayTime(self, times, n, k):
        graph = {}
        for time in times:
            if time[0] not in graph:
                graph[time[0]] = PriorityQueue()

            graph[time[0]].put((time[2], time))

        cache = [-1] * n
        self.djikstras(graph, k, cache)

        return min(cache)


tests = [
    (([[2, 1, 1], [2, 3, 1], [3, 4, 1]], 4, 2), 2),
    (([[1, 2, 1]], 2, 1), 1),
    (([[1, 2, 1]], 2, 2), -1)
]

for test in tests:
    print(Solution().networkDelayTime(*test[0]), test[1])
