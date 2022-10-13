import collections


def kmp_shift(pattern):
    shift = collections.defaultdict(int)

    shift[-1] = 1
    shift[0] = 1

    i = 1
    j = 0

    while i + j < len(pattern):
        if pattern[i + j] == pattern[j]:
            shift[i + j] = i
            j += 1
        else:
            if j == 0:
                shift[i] = i + 1
            i = i + shift[j - 1]
            j = max(j - shift[j - 1], 0)

        print(i, j, shift)

    return shift


tests = [
    ("ababbcababa",)
]

for test in tests:
    kmp_shift(test[0])
