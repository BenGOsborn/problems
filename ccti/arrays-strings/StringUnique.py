def string_unique(string):
    seen = {}

    for char in string:
        if char not in seen:
            seen[char] = True
        else:
            return False

    return True

tests = ["aabcd", "abcd"]

for test in tests:
    print(string_unique(test))