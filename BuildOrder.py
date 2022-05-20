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

    print("Test 1", find(elem, dep, seen, solved))

    # Test case 2 (different format)
    elem = "a"
    graph = [["a", "b"], ["b", "f"], ["b", "c"], ["b", "d"], ["d", "c"], ["f", "e"], ["a", "e"]]
    dep = graph_to_dict(graph)

    seen = {}
    solved = {}

    print("Test 2", find(elem, dep, seen, solved))

    # Test case 3
    elem = "4"
    graph = [["4", "3"], ["3", "1"], ["3", "2"], ["1", "0"], ["2", "0"]]
    dep = graph_to_dict(graph)

    seen = {}
    solved = {}

    print("Test 3", find(elem, dep, seen, solved))

    # Test case 4
    elem = "a"
    dep = {"a": ["b", "e"]}

    seen = {}
    solved = {}

    print("Test 4", find(elem, dep, seen, solved))

    # Test case 5
    elem = "a"
    dep = {}

    seen = {}
    solved = {}

    print("Test 5", find(elem, dep, seen, solved))