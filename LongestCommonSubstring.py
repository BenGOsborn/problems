def longest_common_same(s1, s2):
    compared = []

    for i in range(len(s1)):
        t = i

        temp_compared = []



def main():
    s1 = ["/start", "/green", "/blue", "/pink", "/register", "/orange", "/one/two"]
    s2 = ["/start", "/pink", "/register", "/orange", "/red", "a"]

    print(longest_common_same(s1, s2))

if __name__ == "__main__":
    main()