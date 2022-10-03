class Solution:
    def strStr(self, haystack, needle):
        pass


tests = [
    (("sadbutsad", "sad"), 0),
    (("leetcode", "leeto"), -1),
]

for test in tests:
    print(Solution().strStr(*test[0]), test[1])
