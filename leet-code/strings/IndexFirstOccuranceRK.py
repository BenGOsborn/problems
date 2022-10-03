import string


class Solution:
    def strStr(self, haystack, needle):
        if len(needle) > len(haystack):
            return -1

        prime = 5

        lookup = {}
        for i, char in enumerate(string.digits + string.ascii_lowercase):
            lookup[char] = i + 1

        compare_hash = 0
        check_hash = 0
        for i in range(len(needle) - 1, -1, -1):
            hashed = lookup[needle[len(needle) - 1 - i]]
            compare_hash += ((len(lookup) ** i) * hashed) % prime

            hashed = lookup[haystack[len(needle) - 1 - i]]
            check_hash += ((len(lookup) ** i) * hashed) % prime
        compare_hash %= prime
        check_hash %= prime

        if compare_hash == check_hash:
            match = True
            for j in range(len(needle)):
                if needle[j] != haystack[j]:
                    match = False
                    break
            if match:
                return 0

        for i in range(1, len(haystack) - len(needle) + 1):
            check_hash = (((check_hash - ((len(lookup) ** (len(needle) - 1) * lookup[haystack[i - 1]]) % prime)) * len(
                lookup)) % prime + lookup[haystack[i + len(needle) - 1]]) % prime

            if compare_hash == check_hash:
                match = True
                for j in range(len(needle)):
                    if needle[j] != haystack[i + j]:
                        match = False
                        break
                if match:
                    return i

        return -1

    # Knuth Morris Pratt
    # def strStr(self, haystack, needle):
    #     pass


tests = [
    (("011010011001110", "101"), 2),
    (("sadbutsad", "sad"), 0),
    (("leetcode", "leeto"), -1),
    (("hello", "ll"), 2),
]

for test in tests:
    print(Solution().strStr(*test[0]), test[1])
