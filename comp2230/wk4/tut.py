def invert(s):
    temp1 = []
    temp2 = []

    while len(s):
        temp1.append(s.pop(-1))

    while len(temp1):
        temp2.append(temp1.pop(-1))

    while len(temp2):
        s.append(temp2.pop(-1))

x = [1, 2, 3, 4]

invert(x)

print(x)