class Solution:
    def topological_sort(self, start, graph, marked, out):
        if start in marked:
            if marked[start]:
                return True
            return False

        marked[start] = False

        if start in graph:
            for elem in graph[start]:
                if not self.topological_sort(elem, graph, marked, out):
                    return False

        marked[start] = True
        out.append(start)

        return True

    def findOrder(self, numCourses, prerequisites):
        graph = {}
        for elem in prerequisites:
            if elem[0] in graph:
                graph[elem[0]].append(elem[1])
            else:
                graph[elem[0]] = [elem[1]]

        out = []
        marked = {}
        for elem in range(numCourses):
            if elem not in marked and not self.topological_sort(elem, graph, marked, out):
                return []

        return out


tests = [
    (2, [[1, 0]]),
    (4, [[1, 0], [2, 0], [3, 1], [3, 2]]),
    (1, [])
]

for test in tests:
    print(Solution().findOrder(*test))
