import math

def num_a(string):
    a_num = 0
    for char in string:
        if char == "a": a_num += 1

    return a_num

def repeated(string, n):
    full = math.floor(n / len(string))
    remainder = n % len(string)

    return num_a(string) * full + num_a(string[:remainder])

def main():
    string = "abcac"
    n = 10

    print(repeated(string, n))

if __name__ == "__main__":
    main();