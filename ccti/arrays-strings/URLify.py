def urlify(string):
    return "".join(["%20" if char == " " else char for char in string])

tests = ["Mr 3ohn Smith", "Hello This world"]

for test in tests:
    print(urlify(test))