def valleys(string):
    seen = 0
    height = 0

    started_valley = False

    for char in string:
        if char == "U":
            height += 1
        else:
            height -= 1

        if height < 0:
            started_valley = True
        elif height == 0 and started_valley:
            seen += 1
            started_valley = False

    return seen

def main():
    inp = "UDDDUDUU"
    steps = len(inp)

    print(valleys(inp))

if __name__ == "__main__":
    main();