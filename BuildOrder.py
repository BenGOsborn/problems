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

if __name__ == "__main__":
    elem = "a"
    dep = {"a": ["b", "e"], "b": ["c", "d", "f"], "d": ["c"], "f": ["e"], "e": ["f"]}
    # dep = {"a": ["b", "e"], "b": ["c", "d", "f"], "d": ["c"], "f": ["e"]}

    seen = {}
    solved = {}

    print(find(elem, dep, seen, solved))