def compress(string):
    if len(string) == 0:
        return string

    current = string[0]
    count = 0

    out = ""

    i = 0
    while i < len(string):
        if string[i] != current:
            out += current + str(count)

            current = string[i]
            count = 1
        else:
            count += 1

        i += 1

    return out + current + str(count)


tests = ["hello", "world", "aabcccccaaa"]

for test in tests:
    print(compress(test))
