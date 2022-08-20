def one_away(string1, string2):
    if string1 == string2:
        return True

    diff = abs(len(string1) - len(string2))

    if diff > 1:
        return False

    min_size = min(len(string1), len(string2))

    if diff == 1:
        for i in range(min_size):
            if string1[i] != string2[i]:
                if len(string1) > len(string2):
                    cmpre = string1[:i] + string1[i + 1:]
                    return cmpre == string2
                else:
                    cmpre = string2[:i] + string2[i + 1:]
                    return cmpre == string1

        return True

    if diff == 0:
        for i in range(min_size):
            if string1[i] != string2[i]:
                cmpre = string1[:i] + string2[i] + string1[i + 1:]
                return cmpre == string2

# We need to check if one (or zero) edit can be made to the strings to make them equal
# - If they are equal they are valid
# - If they are more than two in length away it is invalid
# - If they have a difference of one between them, we simply just need to find where the differ, remove the point, then check if they are equal or not. If no, it is invalid
# - If they have a difference of zero between them, we just need to replace one character, and if replacing that one character does not work it is invalid


tests = [("paie", "pie"), ("pales", "pale"),
         ("pale", "bale"), ("pale", "bake")]

for test in tests:
    print(one_away(test[0], test[1]))
