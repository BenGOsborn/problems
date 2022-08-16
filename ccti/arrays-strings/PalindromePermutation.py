def is_palindrome_permutation(string):
    mapping = {}
    for char in string:
        if char not in mapping:
            mapping[char] = 1
        else:
            mapping[char] += 1

    odd_flag = False
    for key in mapping.keys():
        if mapping[key] % 2 != 0:
            if odd_flag == True:
                return False
            odd_flag = True

    return True

# Assume no spaces

tests = ["tacocat", "arceacr", "cat"]

for test in tests:
    print(is_palindrome_permutation(test))