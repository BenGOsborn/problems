tests = ["leetcode", "loveleetcode", "aabb"]


class Solution:
    def first_unique_char(self, s):
        first_seen = {}
        occurances = {}

        for i, elem in enumerate(s):
            if elem not in first_seen:
                first_seen[elem] = i

            if elem not in occurances:
                occurances[elem] = 1
            else:
                occurances[elem] += 1

        for key, value in occurances.items():
            if value == 1:
                return first_seen[key]

        return -1


test = tests[2]
print(Solution().first_unique_char(test))
