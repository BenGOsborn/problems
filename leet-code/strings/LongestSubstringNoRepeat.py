# Algorithm
# - When we iterate through, we will keep count of the max substring that we encounter, as well as when the subarray started
# - We will iterate over the string and will keep a count of the indexes of our seen elements
# - I can check if the element is a duplicate access by looking at where the index occurs - we can overwrite the previous index with a new one once we resee it which will be in a valid range

class Solution:
    def lengthOfLongestSubstring(self, s):
        seen = {}
        start = 0

        max_len = 0

        for i, elem in enumerate(s):
            if elem in seen and seen[elem] >= start:
                start = seen[elem] + 1
                seen[elem] = i
                continue

            seen[elem] = i

            max_len = max(max_len, i - start + 1)

        return max_len


tests = [
    ("abcabcbb", 3),
    ("bbbbb", 1),
    ("pwwkew", 3),
    ("c", 1),
    (" ", 1),
    ("aab", 2)
]

for test in tests:
    print(Solution().lengthOfLongestSubstring(test[0]), test[1], "\n")
