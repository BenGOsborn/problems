def one_away(string1, string2):
    if string1 == string2:
        return True

    if abs(len(string1) - len(string2)) > 2:
        return False

    # We need to check the append case
    # We need to check the removal case
    # We need to check the replace case

# We need to check if one (or zero) edit can be made to the strings to make them equal
# - If they are equal they are valid
# - If they are more than two in length away it is invalid
# - If we can construct one out of the other and only have to make one change, we know we have found the result


tests = [("paie", "pie"), ("pales", "pale"),
         ("pale", "bale"), ("pale", "bake")]

for test in tests:
    print(one_away(test[0], test[1]))
