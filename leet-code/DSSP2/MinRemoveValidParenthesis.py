class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        s = [char for char in s]

        stack = []
        remainder = [] # Remainder of "("

        for i, char in enumerate(s):
            if char == "(":
                stack.append("(")
                remainder.append(i)
            elif char == ")":
                if len(stack) == 0:
                    s[i] = "#"
                else:
                    stack.pop(-1)
                    remainder.pop(-1)

        for i in remainder:
            s[i] = "#"

        return "".join(char for char in s if char != "#")

tests = ["lee(t(c)o)de)", "a)b(c)d", "))(("]

for test in tests:
    print(Solution().minRemoveToMakeValid(test))