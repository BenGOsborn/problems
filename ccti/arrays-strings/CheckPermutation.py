def check_permutation(string1, string2):
    if len(string1) != len(string2):
        return False

    seen = {}
    for char in string1:
        if char not in seen:
            seen[char] = 1
        else:
            seen[char] += 1

    for char in string2:
        if char not in seen:
            return False
        elif seen[char] == 0:
            return False
        else:
            seen[char] -= 1

    return True

tests = [("abcd", "bcad"), ("abcd", "aabc")]

for test in tests:
    print(check_permutation(test[0], test[1]))