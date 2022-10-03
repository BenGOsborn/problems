import heapq

# Algorithm
# - Implement djikstras to find the shortest path to every node
# - Return the minimum of the shortest paths (including -1)


class Solution:
    def networkDelayTime(self, times, n, k):
        graph = {}
        for time in times:
            to_add = (time[2], time[1])
            if time[0] not in graph:
                graph[time[0]] = [to_add]
            else:
                graph[time[0]].append(to_add)

        print(graph)


tests = [
    (([[2, 1, 1], [2, 3, 1], [3, 4, 1]], 4, 2), 2),
    # (([[1, 2, 1]], 2, 1), 1),
    # (([[1, 2, 1]], 2, 2), -1)
]

for test in tests:
    print(Solution().networkDelayTime(*test[0]), test[1])
