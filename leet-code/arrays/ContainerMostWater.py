# Algorithm
# - Use two pointers starting from either end to maximize the distance
# - Keep track of the max on either side and the current container max
# - If we find a new element that creates a larger array, we will update the size of the container, and then update the current pointers max
# - If we find an element that is taller BUT closer together, we will update it, but keep the original max


class Solution:
    def maxArea(self, height):
        i = 0
        j = len(height) - 1
        i_max = i
        j_max = j

        max_container = -1

        # **** I also need to keep track of where the max pointer was
        # **** The tricky part is knowing when to update the pointer

        while i < j:
            if height[i] > height[i_max]:
                i_max = i
            if height[j] > height[j_max]:
                j_max = j

            i += 1
            j -= 1


tests = [
    ([1, 8, 6, 2, 5, 4, 8, 3, 7], 49),
    ([1, 1], 1)
]


for test in tests:
    print(Solution().maxArea(test[0]))
    print(test[1])
    print()
