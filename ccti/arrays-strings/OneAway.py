def one_away(string1, string2):
    if abs(len(string1) - len(string2)) > 2:
        return False

    # **** Now we just need to check how much the characters differ by... ?


tests = [("pale", "pie"), ("pales", "pale"),
         ("pale", "bale"), ("pale", "bake")]

for test in tests:
    print(one_away(test[0], test[1]))
