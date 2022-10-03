class Solution:
    def strStr(self, haystack, needle):
        if len(needle) > len(haystack):
            return -1

        table = self.build_table(needle)
        return table

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
    # (("abxabcabcaby", "abcdabcabcx"), -1),
    (("abxabcabcabyzzz", "jabcdabcjabcx"), -1),
    # (("abxabcabcaby", "abcabya"), 6),
    # (("sadbutsad", "sad"), 0),
    # (("leetcode", "leeto"), -1),
    # (("hello", "ll"), 2),
]

for test in tests:
    print(Solution().strStr(*test[0]), test[1])
