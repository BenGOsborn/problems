tests = [5, 1, 2, 3]


class Solution:
    def create_row(self, prev_row):
        out = [1]

        for i in range(len(prev_row) - 1):
            out.append(prev_row[i] + prev_row[i + 1])

        out.append(1)

        return out

    def generate(self, num_rows):
        out = [[1]]

        for i in range(1, num_rows):
            prev = out[i - 1]
            out.append(self.create_row(prev))

        return out


test = tests[3]
print(Solution().generate(test))
