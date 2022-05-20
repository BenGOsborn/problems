def find(elem, dep, seen, solved):
    # **** This is going to have to recursively look through until it cannot find anymore
    pass


if __name__ == "__main__":
    elem = "a"
    dep = {"a": ["b", "e"], "b": ["c", "d", "f"], "d": ["c"], "f": ["e"]}
    seen = {}
    solved = {}

    print(find(elem, dep, seen, solved))
