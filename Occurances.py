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

def check_unique(string, max_unique):
    unique = list(set(string))

    dic = {}

    for char in unique:
        dic[char] = 0

    for char in string:
        dic[char] += 1
    
    uniq_cnt = 0
    for char in unique:
        if dic[char] == 1:
            uniq_cnt += 1
        if uniq_cnt > max_unique:
            return False
        
    return True

def max_combinations(occurances):
    dic = {}

    for occurance in occurances:
        if occurance in dic:
            dic[occurance] += 1
        else:
            dic[occurance] = 1
    
    if len(dic.values()) > 0:
        return max(dic.values())
    return 0

def max_occurances(components, min_length, max_length, max_unique):
    substrings = get_substrings(components, min_length, max_length)

    out = []
    for string in substrings:
        if check_unique(string, max_unique):
            out.append(string)
    
    return max_combinations(out)

def main():
    components = "abcde"
    min_length = 2
    max_length = 4
    max_unique = 3

    print(max_occurances(components, min_length, max_length, max_unique))

if __name__ == "__main__":
    main()