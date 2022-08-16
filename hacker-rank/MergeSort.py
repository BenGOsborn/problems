def merge(x, y):
    new = []

    i = 0
    j = 0
    while i < len(x) and j < len(y):
        if x[i] < y[j]:
            new.append(x[i])
            i += 1
        else:
            new.append(y[j])
            j += 1
    
    if i < len(x):
        new += x[i:]
    else:
        new += y[j:]
    
    return new

def merge_sort(x):
    if len(x) == 1:
        return x

    mid = len(x) // 2

    return merge(merge_sort(x[:mid]), merge_sort(x[mid:]))

def main():
    x = [1, 4, 2, 3, 6, 4]

    print(merge_sort(x))

if __name__ == "__main__":
    main()