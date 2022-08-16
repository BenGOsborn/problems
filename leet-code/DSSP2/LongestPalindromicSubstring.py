# class SolutionBruteForce:
#     def is_palindrome(self, s):
#         stack = []

#         for elem in s:
#             stack.append(elem)

#         return "".join(stack[::-1]) == s

#     # **** Another alternative I could come up with is identifying each palindrome from the base layer, then trying to build it up in the next increments some way

#     def longestPalindrome(self, s: str) -> str:
#         str_len = len(s)

#         for i in range(str_len):
#             curr_len = str_len - i

#             for j in range(str_len - curr_len + 1):
#                 candidate = s[j:j + curr_len]
                
#                 if self.is_palindrome(candidate):
#                     return candidate

class Solution:
    def build_palindrome(self, s, l, r):
        while l >= 0 and r < len(s) and s[l] == s[r]:
            l -= 1
            r += 1

        return s[l + 1:r]

    def longestPalindrome(self, s: str) -> str:
        candidate = ""

        if len(s) == 1:
            return s

        for i in range(len(s) - 1):
            odd = self.build_palindrome(s, i, i)

            if len(odd) > len(candidate):
                candidate = odd

            even = self.build_palindrome(s, i, i + 1)

            if len(even) > len(candidate):
                candidate = even

        return candidate

tests = ["babad", "cbbd", "bb", "a", "ccc"]

for test in tests[4:]:
    print(Solution().longestPalindrome(test))