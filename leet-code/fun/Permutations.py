class Solution:
    def permute_h(self, current, available, out):
        if len(available) == 0:
            out.append(current)
            return

        for i in range(len(available)):
            self.permute_h(current + [available[i]],
                           available[:i] + available[i+1:], out)

    def permute(self, nums):
        out = []
        self.permute_h([], nums, out)

        return out
