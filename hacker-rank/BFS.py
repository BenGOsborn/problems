def bfs_iterative(graph, entry):
    q = []
    visited = {}

    q.append(entry)
    visited[entry] = True

    while len(q) > 0:
        val = q.pop(0)
        print(val)

        if val in graph:
            for elem in graph[val]:
                if elem not in visited:
                    q.append(elem)
                    visited[elem] = True

def main():
    graph = {
        "a": ["b", "c"],
        "b": ["d", "e"],
        "c": ["f"],
        "f": ["g", "z"]
    }

    bfs_iterative(graph, "a")

if __name__ == "__main__":
    main()