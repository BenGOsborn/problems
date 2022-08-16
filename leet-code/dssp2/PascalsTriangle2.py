class Solution:
    def getRow(self, rowIndex: int):
        if rowIndex == 0:
            return [1]
        else:
            prev = self.getRow(rowIndex - 1)

            out = [1]

            for i in range(len(prev) - 1):
                out.append(prev[i] + prev[i + 1])

            out.append(1)

            return out

print(Solution().getRow(0))