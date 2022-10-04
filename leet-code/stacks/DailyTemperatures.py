class Solution:
    def dailyTemperatures(self, temperatures):
        stack = []
        out = [0] * len(temperatures)

        for i, elem in enumerate(temperatures):
            while stack and temperatures[stack[-1]] < elem:
                popped = stack.pop(-1)
                out[popped] = i - popped

            stack.append(i)

        return out


tests = [
    ([73, 74, 75, 71, 69, 72, 76, 73], [1, 1, 4, 2, 1, 1, 0, 0]),
    ([30, 40, 50, 60], [1, 1, 1, 0]),
    ([30, 60, 90], [1, 1, 0]),
]

for test in tests:
    print(Solution().dailyTemperatures(test[0]), test[1])
