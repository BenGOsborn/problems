def one_away(string1, string2):
    print(string1, string2)

    pass


tests = [("pale", "pie"), ("pales", "pale"),
         ("pale", "bale"), ("pale", "bake")]

for test in tests:
    print(one_away(test[0], test[1]))
