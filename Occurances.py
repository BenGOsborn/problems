def get_substrings(min_len, string):
    str_len = len(string)

    out = []

    for _len in range(min_len, str_len + 1):
        for i in range(str_len - _len + 1):
            temp = ""
            for k in range(i,i + _len):
                temp += string[k]
            out.append(temp)
        
    return out

def max_occurances():
    pass

def main():
    print(get_substrings(2, "abcd"))

if __name__ == "__main__":
    main()