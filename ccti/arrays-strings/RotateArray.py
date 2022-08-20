def rotate_array(array):
    for i in range(len(array)):
        for j in range(i, len(array[i])):
            temp = array[i][j]
            array[i][j] = array[j][i]
            array[j][i] = temp

    for i in range(len(array)):
        array[i] = array[i][::-1]

# Transpose the array to rotate 90 degrees to the left then reverse the arrays


tests = [[[1, 2], [3, 4]]]

for test in tests:
    rotate_array(test)
    print(test)
