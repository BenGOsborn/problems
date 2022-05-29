from collections import deque

def bfs_iterative(graph, entry):
    stack = deque()

    stack.append(entry)

    print(entry)

    while len(stack) > 0:
        popped = stack.pop()

        if popped in graph:
            for elem in graph[popped]:
                print(elem)
                stack.append(elem)

def main():
    graph = {
        "a": ["b", "c"],
        "c": ["d", "e"],
        "e": ["f"],
        "f": ["g", "z"]
    }

    bfs_iterative(graph, "a")

if __name__ == "__main__":
    main()