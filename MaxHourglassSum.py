def get_hourglass_sum(array):
    sm = 0

    sm += sum(array[0])
    sm += sum(array[2])
    sm += array[1][1]

    return sm

def kernel(array):
    out = []

    for i in range(len(array) - 3 + 1): # Rows
        for j in range(len(array[0]) - 3 + 1): # Cols
            slc = []
            for k in range(3):
                slc.append(array[i + k][j:j + 3])
            out.append(slc)
    
    return out

def hourglass_sum(array):
    kernels = kernel(array)

    sums = [get_hourglass_sum(kernel) for kernel in kernels]

    return max(sums)

def main():
    example = [
        [1, 1, 1, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [1, 1, 1, 0, 0, 0],
        [0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0]
    ]

    print(hourglass_sum(example))


if __name__ == "__main__":
    main()
