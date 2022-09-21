tests = [-1, 5, 23, 121, 22, 15351, 15352, 0]

def is_int_palindrome(x):
    if x > 0:
        temp = x
        unassembled = []

        while temp > 0:
            digit = temp % 10
            temp = temp // 10
            unassembled.insert(0, digit)
        
        reassembled = 0
        for i, digit in enumerate(unassembled):
            reassembled += digit * 10 ** i
        
        return reassembled == x
    elif x == 0:
        return True
    else:
        return False

test = tests[6]
print(is_int_palindrome(test))