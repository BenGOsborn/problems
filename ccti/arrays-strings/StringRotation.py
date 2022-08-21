def is_rotation(string1, string2):
    concat = string1 + string2
    return string2 in concat

# The easiest way to do this is going to be to rotate the characters back a specific amount ?


tests = [("waterbottle", "erbottlewat")]

for test in tests:
    print(is_rotation(*test))
