def make_hash(string):
    dic = {}

    for char in string:
        if char not in dic:
            dic[char] = 1
        else:
            dic[char] += 1

    return dic

def is_anagram(s1, s2):
    dic1 = make_hash(s1)
    dic2 = make_hash(s2)

    for key in dic1:
        if key in dic2:
            val = dic2[key]

            dic2[key] = max(val - dic1[key], 0)
            dic1[key] = max(dic1[key] - val, 0)

    return sum(list(dic1.values()) + list(dic2.values()))

def main():
    print(is_anagram("cde", "abc"))

if __name__ == "__main__":
    main()