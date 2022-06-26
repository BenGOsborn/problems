tests = [("a", "b"), ("aa", "ab"), ("aa", "aab")]


class Solution:
    def canConstruct(self, ransom_note, magazine):
        available = {}

        for elem in magazine:
            if elem in available:
                available[elem] += 1
            else:
                available[elem] = 1

        for elem in ransom_note:
            if elem in available and available[elem] > 0:
                available[elem] -= 1
            else:
                return False

        return True


test = tests[2]
print(Solution().canConstruct(test[0], test[1]))
