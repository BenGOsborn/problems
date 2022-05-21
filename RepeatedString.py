def repeated(string, n):
    # **** Our best bet is going to be to get the number of a's in the existing string

    a_num = 0
    for char in string:
        if char == "a": a_num += 1
    
    # **** So now we are going to take this number, multiply it such that it is greater or equal to the length of n, figure out how much the string is over, chop it off, and consider the number of a's in that string

def main():
    string = "abcac"
    n = 10

    print(repeated(string, n))

if __name__ == "__main__":
    main();