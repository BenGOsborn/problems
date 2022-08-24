# 3 (Topological sort)

# Algorithm
# - DFS through the nodes, and before navigating to a node we will check if has been reached
# - If all of the children of the current node have been marked, then we can set the current node as marked
# - Else, we will have to recursively DFS through the children nodes and mark them off recursively
# - We will store all of the marked off nodes in an out array (if they have not already been seen of course)


def topological_sort_helper(graph, key, out, finished):
    for elem in graph[key]:
        if elem not in finished:
            topological_sort_helper(graph, elem, out, finished)

    out.append(key)
    finished[key] = True


def topological_sort(graph):
    seen = {}
    out = []

    for key in graph.keys():
        if key not in seen:
            topological_sort_helper(graph, key, out, seen)

    return out


gr_3 = {"1": ["3"], "2": ["3"], "3": ["4", "6"], "4": [], "5": ["2", "6", "8"], "6": [
    "4", "9"], "7": ["4", "10"], "8": ["9"], "9": ["10"], "10": []}
out = []
print(topological_sort(gr_3))
