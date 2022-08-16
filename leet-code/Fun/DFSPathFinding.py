def dfs(source, graph, target, path, seen):
    if source in seen:
        return False

    seen[source] = True

    path.append(source)

    for elem in graph[source]:
        if elem == target:
            path.append(target)
            return True

        if dfs(elem, graph, target, path, seen):
            return True

    path.pop(-1)

    return False

def main():
    start = "a"
    end = "f"
    graph = {"a": {"b", "c"}, "b": {"c", "d"}, "c": {"e"}, "e": {"d"}, "d": {"f"}, "f": set()}

    seen = {}

    path = []

    dfs(start, graph, end, path, seen)

    print(path)

if __name__ == "__main__":
    main()