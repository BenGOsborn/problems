class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        split = s.split(" ")

        if len(pattern) != len(split):
            return False

        mapping_1 = {}

        for i, char in enumerate(pattern):
            if char not in mapping_1:
                mapping_1[char] = split[i]

        if s != " ".join([mapping_1[x] for x in pattern]):
            return False

        mapping_2 = {}

        for i, elem in enumerate(split):
            if elem not in mapping_2:
                mapping_2[elem] = pattern[i]

        return pattern == "".join([mapping_2[x] for x in split])

tests = [("abba", "dog cat cat dog"), ("abba", "dog cat cat fish"), ("aaaa", "dog cat cat dog"), ("abba", "dog dog dog dog")]

for test in tests:
    print(Solution().wordPattern(test[0], test[1]))