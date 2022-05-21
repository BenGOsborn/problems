def valleys(string):
    seen = 0
    height = 0

    started_valley = False

    for char in string:
        if char == "U":
            height += 1
        else:
            height -= 1

    print(height)

def main():
    inp = "UDDDUDUU"
    steps = len(inp)

    print(valleys(inp))

if __name__ == "__main__":
    main();