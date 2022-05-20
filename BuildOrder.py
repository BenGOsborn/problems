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
        if str(pair[0]) in dic:
            dic[str(pair[0])].append(str(pair[1]))
        else:
            dic[str(pair[0])] = [str(pair[1])]
    
    return dic

if __name__ == "__main__":
    # elem = "a"
    # dep = {"a": ["b", "e"], "b": ["c", "d", "f"], "d": ["c"], "f": ["e"], "e": ["f"]}
    # dep = {"a": ["b", "e"], "b": ["c", "d", "f"], "d": ["c"], "f": ["e"]}

    elem = "1"
    graph = [[1, 0], [2, 0], [3, 1], [3, 2]]
    dep = graph_to_dict(graph)
    print(dep)

    seen = {}
    solved = {}

    # print(find(elem, dep, seen, solved))