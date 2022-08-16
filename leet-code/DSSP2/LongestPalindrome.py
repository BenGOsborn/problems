class Solution:
    def longestPalindrome(self, s: str) -> int:
        mapping = {}

        for char in s:
            if char not in mapping:
                mapping[char] = 1
            else:
                mapping[char] += 1

        seen_odd = False
        longest = 0
        for key, value in mapping.items():
            if value % 2 != 0:
                if seen_odd:
                    longest += value - 1
                else:
                    longest += value
                    seen_odd = True
            else:
                longest += value

        return longest

tests = ["abccccdd", "a"]

for test in tests:
    print(Solution().longestPalindrome(test))