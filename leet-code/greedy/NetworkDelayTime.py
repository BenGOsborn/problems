from queue import PriorityQueue

# Algorithm
# - Implement djikstras to find the shortest path to every node
# - Return the minimum of the shortest paths (including -1)


class Solution:
    def networkDelayTime(self, times, n, k):
        cache = [-1] * n  # Seen elements are not -1

        graph = {}
        for time in times:
            if time[0] not in graph:
                graph[time[0]] = PriorityQueue()

            graph[time[0]].put((time[2], time))

        print(graph)

        # **** We just need to explore every node, and then update the previous node with the new value if it has already been taken

        return min(cache)


tests = [
    (([[2, 1, 1], [2, 3, 1], [3, 4, 1]], 4, 2), 2),
    (([[1, 2, 1]], 2, 1), 1),
    (([[1, 2, 1]], 2, 2), -1)
]

for test in tests:
    print(Solution().networkDelayTime(*test[0]), test[1])
