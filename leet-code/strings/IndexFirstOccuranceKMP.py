class Solution:
    def strStr(self, haystack, needle):
        table = self.build_table(needle)

        print(table)

        i = 0
        j = 0
        while i < len(haystack):
            if haystack[i] == needle[j]:
                i += 1
                j += 1
            else:
                if j == 0:
                    i += 1
                else:
                    j = table[j - 1]

            if j == len(needle):
                return i - len(needle)

        return -1

    def build_table(self, string):
        pivot = [0] * len(string)

        i = 1
        j = 0
        while i < len(string):
            if string[i] == string[j]:
                j += 1
                pivot[i] = j
                i += 1
            elif j != 0:
                j = pivot[j - 1]
            else:
                pivot[i] = 0
                i += 1

        return pivot


tests = [
    (("abcxabcdabxabcdabcdabcy", "abcdabcy"), 15),
    (("sadbutsad", "sad"), 0),
    (("leetcode", "leeto"), -1),
    (("hello", "ll"), 2),
    (("mississippi", "issip"), 4),
]

for test in tests:
    print(Solution().strStr(*test[0]), test[1])
