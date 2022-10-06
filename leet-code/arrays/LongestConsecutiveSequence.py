class Solution:
    def longestConsecutive(self, nums):
        hash_set = set()

        for elem in nums:
            hash_set.add(elem)

        mx = 0

        for elem in nums:
            current = 0

            r_ptr = 0
            l_ptr = 1
            while True:
                nxt = elem + r_ptr
                prev = elem - l_ptr

                if nxt in hash_set:
                    current += 1
                    hash_set.remove(nxt)
                    r_ptr += 1
                elif prev in hash_set:
                    current += 1
                    hash_set.remove(prev)
                    l_ptr += 1
                else:
                    break

            mx = max(mx, current)

        return mx


tests = [
    ([100, 4, 200, 1, 3, 2], 4),
    ([0, 3, 7, 2, 5, 8, 4, 6, 0, 1], 9),
]

for test in tests:
    print(Solution().longestConsecutive(test[0]), test[1])
