class Solution:
    def permuteUnique(self, nums):
        out = []
        self.permute_h([], nums, out)

        return out

    def permute_h(self, current, available, out):
        if len(available) == 0:
            out.append(current)
            return

        seen = {}
        for i, elem in enumerate(available):
            if elem not in seen:
                self.permute_h(current + [elem],
                               available[:i] + available[i+1:], out)
                seen[elem] = True
