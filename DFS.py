from collections import deque

def dfs_iterative(graph, entry):
    stack = deque()

    stack.append(entry)

    while len(stack) > 0:
        popped = stack.pop()
        print(popped)

        if popped in graph:
            for elem in graph[popped]:
                stack.append(elem)

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
    print()
    dfs_recursive(graph, "a")

if __name__ == "__main__":
    main()