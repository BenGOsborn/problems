tests = [("anagram", "nagaram"), ("rat", "car")]


class Solution:
    def isAnagram(self, s, t):
        if len(s) != len(t):
            return False

        seen = {}

        for elem in s:
            if elem in seen:
                seen[elem] += 1
            else:
                seen[elem] = 1

        missed = 0
        for elem in t:
            if elem in seen and seen[elem] > 0:
                seen[elem] -= 1
            else:
                missed += 1

        return missed == 0


test = tests[1]
print(Solution().isAnagram(test[0], test[1]))
