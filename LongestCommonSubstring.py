def longest_common_same(s1, s2):
    compared = []

    for i in range(len(s1)):
        t = i

        temp_compared = []

        for j in range(len(s2)):
            if s1[t] == s2[j]:
                temp_compared.append(s2[j])
                t += 1

                if t == len(s1):
                    break
            else:
                t = i

        if len(temp_compared) > len(compared):
            compared = temp_compared

    return compared



def main():
    s1 = ["/start", "/green", "/blue", "/pink", "/register", "/orange", "/one/two"]
    s2 = ["/start", "/pink", "/register", "/orange", "/red", "a"]

    print(longest_common_same(s1, s2))

if __name__ == "__main__":
    main()