class Solution:
    def exists(self, graph, start, finish, seen):
        if start in seen:
            return False

        if start == finish:
            return True

        seen[start] = True

        if start in graph:
            for elem in graph[start]:
                if self.exists(graph, elem, finish, seen):
                    return True

        return False

    def findRedundantConnection(self, edges):
        graph = {}

        for edge in edges:
            if self.exists(graph, edge[0], edge[1], {}):
                return edge

            if edge[0] not in graph:
                graph[edge[0]] = [edge[1]]
            else:
                graph[edge[0]].append(edge[1])
            if edge[1] not in graph:
                graph[edge[1]] = [edge[0]]
            else:
                graph[edge[1]].append(edge[0])

        print(graph)


tests = [
    ([[1, 2], [1, 3], [2, 3]], [2, 3]),
    ([[1, 2], [2, 3], [3, 4], [1, 4], [1, 5]], [1, 4])
]

for test in tests:
    print(Solution().findRedundantConnection(test[0]))
    print(test[1])
