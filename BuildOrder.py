def find(elem, dep, seen, solved):
    out = ""
    seen[elem] = True

    if elem in dep:
        for item in dep[elem]:
            if item in solved and solved[item] == True:
                continue;
            elif item in seen and seen[item] == True:
                raise Exception("Loop exists")
            else:
                out += find(item, dep, seen, solved) + " "

    solved[elem] = True
    
    return out + " " + elem

def graph_to_dict(graph):
    for pair in graph:
        pass

if __name__ == "__main__":
    elem = "a"
    # dep = {"a": ["b", "e"], "b": ["c", "d", "f"], "d": ["c"], "f": ["e"], "e": ["f"]}
    # dep = {"a": ["b", "e"], "b": ["c", "d", "f"], "d": ["c"], "f": ["e"]}

    graph = [[1, 0], [2, 0], [3, 1], [3, 2]]
    dep = graph_to_dict(graph)

    seen = {}
    solved = {}

    print(find(elem, dep, seen, solved))