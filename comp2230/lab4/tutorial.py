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


test = {"a": ["b", "s"], "s": ["g", "c"], "g": [
    "f", "h"], "c": ["d", "e", "f"], "e": ["h"]}

print(bfs_path("a", "f", test))

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
