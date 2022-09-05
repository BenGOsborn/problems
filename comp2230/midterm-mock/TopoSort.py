def topological_sort_h(graph, start, marked):
    if start in marked:
        return

    for elem in graph[start]:
        if elem not in marked:
            topological_sort_h(graph, elem, marked)

    marked[start] = True
    print(start)


def topological_sort(graph):
    marked = {}

    for elem in graph:
        topological_sort_h(graph, elem, marked)


graph = {"1": ["2"], "2": ["3", "5"], "3": [], "4": ["1", "7"], "5": [
    "8"], "6": ["3", "9"], "7": ["8"], "8": ["9"], "9": [], "10": ["8"]}

topological_sort(graph)
