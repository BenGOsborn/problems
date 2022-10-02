class Solution:
    def minCostClimbingStairs(self, cost):
        cache = [-1] * len(cost)
        cache[-1] = cost[-1]
        cache[-2] = cost[-2]

        for i in range(len(cost) - 1 - 2, -1, -1):
            cache[i] = min(cost[i] + cache[i + 1], cost[i] + cache[i + 2])

        return min(cache[0], cache[1])


tests = [
    ([10, 15, 20], 15),
    ([1, 100, 1, 1, 1, 100, 1, 1, 100, 1], 6)
]

for test in tests:
    print(Solution().minCostClimbingStairs(test[0]), test[1])
