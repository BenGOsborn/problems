class Solution:
    def topological_sort(self, start, graph, current, seen):
        # **** We need to consider the edge case where we have a cycle
        pass

    def findOrder(self, numCourses, prerequisites):
        graph = {}
        for elem in prerequisites:
            if elem[0] in graph:
                graph[elem[0]].append(elem[1])
            else:
                graph[elem[0]] = [elem[1]]

        for course_num in range(numCourses):
            pass


tests = [
    (2, [[1, 0]]),
    (4, [[1, 0], [2, 0], [3, 1], [3, 2]])
]

for test in tests:
    print(Solution().findOrder(*test))
