def backtrack(graph, start, finish, path):
    if start == finish:
        print(path)
        return

    for elem in graph[start]:
        if elem not in path:
            backtrack(graph, elem, finish, path + [elem])


graph = {"1": ["2", "5"], "2": ["3", "5"], "3": ["4"], "4": ["6"], "5": ["4"]}

backtrack(graph, "1", "6", ["1"])
