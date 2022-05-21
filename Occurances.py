def get_substrings(string, min_len, max_len):
    str_len = len(string)

    out = []

    for _len in range(min_len, max_len + 1):
        for i in range(str_len - _len + 1):
            temp = ""

            for k in range(i,i + _len):
                temp += string[k]

            out.append(temp)
        
    return out

def max_occurances(components, min_length, max_length):
    substrings = get_substrings(components, min_length, max_length)

    return substrings

def main():
    components = "abcde"
    min_length = 2
    max_length = 3
    max_unique = 3

    print(max_occurances(components, min_length, max_length))

if __name__ == "__main__":
    main()