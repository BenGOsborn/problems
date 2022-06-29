tests = ["()", "()[]{}", "(]", "[", "]"]

class Solution:
    def isValid(self, s):
        stack = []

        pair = {"(": ")", "[": "]", "{": "}"}

        for elem in s:
            if elem in ["(", "[", "{"]:
                stack.append(elem)
            else:
                if len(stack) == 0:
                    return False
                out = stack.pop(-1)
                if elem != pair[out]:
                    return False

        return len(stack) == 0

test = tests[4]
print(Solution().isValid(test))