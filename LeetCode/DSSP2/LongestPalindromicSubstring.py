class Solution:
    def is_palindrome(self, s):
        stack = []

        for elem in s:
            stack.append(elem)

        return "".join(stack[::-1]) == s

    # **** Another alternative I could come up with is identifying each palindrome from the base layer, then trying to build it up in the next increments some way

    def longestPalindrome(self, s: str) -> str:
        str_len = len(s)

        for i in range(str_len):
            curr_len = str_len - i

            for j in range(str_len - curr_len + 1):
                candidate = s[j:j + curr_len]
                
                if self.is_palindrome(candidate):
                    return candidate

tests = ["babad", "cbbd", "bb"]

for test in tests:
    print(Solution().longestPalindrome(test))