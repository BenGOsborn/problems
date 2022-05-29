def min_removals_for_alt(string):
    if len(string) == 0:
        return 0

    removals = 0

    prev_char = string[0] 
    for char in string[1:]:
        if char == prev_char:
            removals += 1
        prev_char = char

    return removals


def main():
    print(min_removals_for_alt("AABAAB"))

if __name__ == "__main__":
    main()