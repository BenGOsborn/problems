def binary_search(x, v, i, j):
    mid = (i + j) // 2

    if x[mid] == v:
        return True
    else:
        if i == j:
            return False  
        elif x[mid] > v:
            return binary_search(x, v, i, mid)
        else:
            return binary_search(x, v, mid, j)

def main():
    x = [1, 2, 3, 4, 5, 6]

    print(binary_search(x, -1, 0, len(x)))


if __name__ == "__main__":
    main()
