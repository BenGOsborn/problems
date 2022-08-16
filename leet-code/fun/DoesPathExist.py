class Solution:
    def edges_to_graph(self, edges):
        graph = {}

        for f, t in edges:
            if f not in graph:
                graph[f] = {t}
            else:
                graph[f].add(t)

            if t not in graph:
                graph[t] = {f}
            else:
                graph[t].add(f)

        return graph

    def dfs(self, seen, graph, source, destination):
        if source in seen:
            return False

        seen[source] = True

        for elem in graph[source]:
            if elem == destination:
                return True
            if self.dfs(seen, graph, elem, destination):
                return True

        return False

    def validPath(self, n, edges, source, destination):
        if n == 1:
            return True

        graph = self.edges_to_graph(edges)
        seen = {}

        return self.dfs(seen, graph, source, destination)

tests = [(3, [[0,1],[1,2],[2,0]], 0, 2),
         (6, [[0,1],[0,2],[3,5],[5,4],[4,3]], 0, 5)]

for test in tests:
    print(Solution().validPath(*test))