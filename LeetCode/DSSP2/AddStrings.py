class Solution:
    def preprocess(self, raw1, raw2):
        out1 = None
        out2 = None

        if len(raw1) == len(raw2):
            out1, out2 = raw1, raw2
        elif len(raw1) > len(raw2):
            out1, out2 = raw1, (len(raw1) - len(raw2)) * "0" + raw2
        else:
            out1, out2 = (len(raw2) - len(raw1)) * "0" + raw1, raw2

        return out1[::-1], out2[::-1]

    def addStrings(self, num1: str, num2: str) -> str:
        p1, p2 = self.preprocess(num1, num2)

        out_list = [0 for _ in range(len(p1) + 1)]

        for i in range(len(p1)):
            digit1 = int(p1[i])
            digit2 = int(p2[i])
            digit_out = out_list[i]

            summed = digit1 + digit2 + digit_out

            if summed >= 10:
                out_list[i] = summed % 10
                out_list[i + 1] += 1
            else:
                out_list[i] = summed

        out_list = out_list[::-1]

        if out_list[0] == 0 and len(out_list) > 1:
            out_list = out_list[1:]

        print(out_list)


print(Solution().addStrings("121", "50"))
