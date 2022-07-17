def main():
    start = "a"
    end = "f"
    graph = {"a": {"b", "c"}, "b": {"c", "d"}, "c": {"e"}, "e": {"d"}, "d": {"f"}, "f": set()}

    seen = {}
    stack = [start]

    while len(stack) > 0:
        pass

    print(stack)

if __name__ == "__main__":
    main()