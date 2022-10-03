# Algorithm
# - Implement dijkstras to find the shortest path to every node
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

        cache = [-1] * n
        cache[k - 1] = 0

        visited = {}

        for _ in range(n):
            min_elem = -1
            mn = -1

            for j in range(1, n + 1):
                if cache[j - 1] == -1:
                    continue
                elif (mn == -1 or cache[j - 1] < mn) and j not in visited:
                    mn = cache[j - 1]
                    min_elem = j

            visited[min_elem] = True

            if min_elem in graph:
                for elem in graph[min_elem]:
                    updated = mn + elem[0]
                    if cache[elem[1] - 1] != -1:
                        updated = min(cache[elem[1] - 1], updated)
                    cache[elem[1] - 1] = updated

        if min(cache) == -1:
            return -1
        return max(cache)


tests = [
    (([[2, 1, 1], [2, 3, 1], [3, 4, 1]], 4, 2), 2),
    (([[1, 2, 1]], 2, 1), 1),
    (([[1, 2, 1]], 2, 2), -1),
    (([[1, 2, 1], [2, 1, 3]], 2, 2), 3),
]

for test in tests:
    print(Solution().networkDelayTime(*test[0]), test[1])
