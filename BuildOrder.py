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
    dic = {}

    for pair in graph:
        if pair[0] in dic:
            dic[pair[0]].append(pair[1])
        else:
            dic[pair[0]] = [pair[1]]
    
    return dic

if __name__ == "__main__":
    # Test case 1
    elem = "a"
    # dep = {"a": ["b", "e"], "b": ["c", "d", "f"], "d": ["c"], "f": ["e"], "e": ["f"]}
    dep = {"a": ["b", "e"], "b": ["c", "d", "f"], "d": ["c"], "f": ["e"]}

    seen = {}
    solved = {}

    print(find(elem, dep, seen, solved))

    # Test case 2 (different format)
    elem = "a"
    graph = [["a", "b"], ["b", "c"], ["d", "c"], ["b", "d"], ["f", "e"], ["a", "e"], ["b", "f"]]
    dep = graph_to_dict(graph)

    seen = {}
    solved = {}

    print(find(elem, dep, seen, solved))