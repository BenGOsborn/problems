def find(elem, dep, seen, solved, out):
    seen[elem] = True

    if elem in dep:
        for item in dep[elem]:
            if item in solved and solved[item] == True:
                continue;
            elif item in seen and seen[item] == True:
                raise Exception("Loop exists")
            else:
                find(item, dep, seen, solved, out)

    solved[elem] = True
    
    out.append(elem)

if __name__ == "__main__":
    # Test case 1
    elem = "a"
    dep = {"a": ["b", "e"], "b": ["c", "d", "f"], "d": ["c"], "f": ["e"]}

    seen = {}
    solved = {}

    x = []
    find(elem, dep, seen, solved, x)
    print(x)