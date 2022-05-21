def clouds(c):
    # **** So basically we are just going to step through using 2 jumps, and if the next element lands on 2 jumps then we will just not go to it
    # **** Our non jump conditions are going to be if it lands on a 1 OR if it lands outside of the array

    jumps = 0
    index = 0

    end_index = len(c) - 1

    while index < end_index:
        if index + 2 > end_index or c[index + 2] == 1:
            index += 1
        else:
            index += 2

        jumps += 1

    return jumps

def main():
    c = [0, 1, 0, 0, 0, 1, 0]

    print(clouds(c))

if __name__ == "__main__":
    main();