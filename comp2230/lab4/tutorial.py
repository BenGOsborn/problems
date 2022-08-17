# 1

# No, it is not the same as the binary search relies on indexing which the linked list cannot support.
# In order to implement binary search with the linked list, we need to move the pointer over to the amount of elements to reach the index

# 2

# Assuming the ascending order (DFS):
# 1, 2, 3, 4, 8, 7, 6, 5, 9, 10, 13, 14, 11, 12, 16, 15

# 3

# Assuming the ascending order (BFS):
# 1, 2, 5, 6, 3, 7, 9, 10, 15, 4, 8, 11, 13, 14, 16, 12

# 4

# We can use BFS for this as it explores the closest elements first, so when we find it, we know it will be the shortest first occurance

def bfs_path(start, find, graph):
    queue = [start]

    seen = {}

    while len(queue):
        elem = queue.pop(0)

        if elem in graph:
            for item in graph[elem]:
                if item not in seen:
                    seen[item] = elem
                    queue.append(item)

    out = []
    while find in seen:
        out.append(find)
        find = seen[find]

    return [start] + out[::-1]


graph = {"a": ["b", "s"], "s": ["g", "c"], "g": [
    "f", "h"], "c": ["d", "e", "f"], "e": ["h"]}

print(bfs_path("a", "f", graph))

# 5

# [-1, -5, 1, 2, 4, 6, 7]

# Algorithm (time / space complexity O(1))


def index_equal_elem(array):
    if array[0] == 0:
        return 0

    return -1


tests = [[-1, -5, 1, 2, 4, 6, 7], [0, 1, 3]]

for test in tests:
    print(index_equal_elem(test))


# 6

def dfs_non_resursive(graph):
    stack = []

    seen = {}

    for key in graph.keys():
        stack.append(key)

        while len(stack):
            item = stack.pop(-1)

            if item in seen:
                continue

            seen[item] = True

            print(item)

            if item in graph:
                for elem in graph[item][::-1]:
                    stack.append(elem)


dfs_non_resursive(graph)

# 7

# Best case time is O(m + n) because we still have to explore each node and edge once

# 8

matrix = [[0, 0, 0, 0, 0],
          [1, 0, 0, 0, 0],
          [0, 1, 0, 0, 0],
          [0, 1, 1, 0, 0],
          [1, 1, 0, 1, 0]]


def dfs_adjacency_matrix(matrix):
    seen = {}

    for i in range(len(matrix)):
        dfs_adjacency_matrix_recursive(i, matrix, seen)


def dfs_adjacency_matrix_recursive(row, matrix, seen):
    if row in seen:
        return
    seen[row] = True

    print(row)

    for i in range(len(matrix[row])):
        if matrix[row][i] == 1:
            dfs_adjacency_matrix_recursive(i, matrix, seen)


dfs_adjacency_matrix(matrix)

# The worst case time for this is O(V^2) where V is the number of vertexes

# 9

print("9\n")


def bfs(graph):
    seen = {}

    queue = []

    for key in graph.keys():
        queue.append(key)

        while len(queue):
            popped = queue.pop(0)

            if popped in seen:
                continue
            seen[popped] = True

            print(popped)

            if popped in graph:
                for edge in graph[popped]:
                    queue.append(edge)


g1 = {"1": ["2", "4"], "2": ["1", "3", "5"], "3": [
    "2", "5", "4"], "4": ["1", "3", "5"], "5": ["2", "3", "4"]}

g2 = {"1": ["2", "4", "5"], "2": ["1", "5", "3"], "3": ["2", "5", "6"], "4": ["1", "5", "7"], "5": ["1", "2", "3", "4", "6", "7", "8", "9"], "6": ["3", "5", "9"],
      "7": ["4", "5", "8", "10"], "8": ["5", "7", "9", "10", "11", "12"], "9": ["6", "5", "8", "12"], "10": ["7", "8", "11"], "11": ["10", "8", "12"], "12": ["11", "8", "9"]}

print("BFS:g1\n")
bfs(g1)
print("BFS:g2\n")
bfs(g2)

print("DFS:g1\n")
dfs_non_resursive(g1)
print("DFS:g2\n")
dfs_non_resursive(g2)
