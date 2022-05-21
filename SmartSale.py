def get_occurances(ids):
    occurances = {}
    occurances_arr = []

    for elem in ids:
        if elem in occurances:
            occurances[elem] += 1
        else:
            occurances[elem] = 1

    for key in occurances:
        occurances_arr.append([occurances[key], key])
    
    return sorted(occurances_arr)

def delete_products(ids, m):
    count = 0

    occurances = get_occurances(ids)

    size = len(occurances)

    for i in range(size):
        if (occurances[i][0] <= m):
            m -= occurances[i][0]
            count += 1

        else:
            return size - count

    return size - count


def main():
    ids = [1, 2, 3, 1, 2, 2]
    m = 3

    print(delete_products(ids, m))


if __name__ == "__main__":
    main()
