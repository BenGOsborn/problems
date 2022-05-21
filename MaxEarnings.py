# **** Wait, first of all we need to be able to see what passengers overlap with each other. Then we can iterate through and avoid the ones that have overlap

def merge_ride(pickup, drop, tip):
    out = []

    for i in range(len(pickup)):
        out.append([pickup[i], drop[i], tip[i]])

    return out

def max_earnings(pickup, drop, tip):
    merged = merge_ride(pickup, drop, tip)

    d = {}

    for start, end, tip in merged:
        if end not in d:
            d[end] =[[start,tip]]
        else:
            d[end].append([start,tip])

    print(d)

def main():
    pickup = [0, 2, 9, 10, 11, 12]
    drop = [5, 9, 11, 11, 14, 17]
    tip = [1, 2, 3, 2, 2, 1]

    print(max_earnings(pickup, drop, tip))



if __name__ == "__main__":
    main()
