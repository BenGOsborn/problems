# Algorithm
# - We are going to do a binary search to find both the start and the end of the list - but how ?

class Solution:
    def searchRange(self, nums, target):
        pass


tests = [
    (([5, 7, 7, 8, 8, 10], 8), [3, 4]),
    (([5, 7, 7, 8, 8, 10], 6), [-1, -1]),
    (([], 0), [-1, -1])
]

for test in tests:
    print(Solution().searchRange(*test[0]))
    print(str(test[1]) + "\n")
