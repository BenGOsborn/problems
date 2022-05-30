def dfs_iterative(graph, entry):
    stack = []
    visited = {}

    stack.append(entry)
    visited[entry] = True

    while len(stack) > 0:
        val = stack.pop(-1)
        print(val)

        if val in graph:
            for elem in graph[val]:
                if elem not in visited:
                    stack.append(elem)
                    visited[elem] = True

def dfs_recursive(graph, entry):
    print(entry)

    if entry in graph:
        for elem in graph[entry]:
            dfs_recursive(graph, elem)
    
def main():
    graph = {
        "a": ["b", "c"],
        "c": ["d", "e"],
        "e": ["f"],
        "f": ["g", "z"]
    }

    dfs_iterative(graph, "a")
    # print()
    # dfs_recursive(graph, "a")
    DFS(graph, "a")

if __name__ == "__main__":
    main()