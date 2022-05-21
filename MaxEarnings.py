# **** Wait, first of all we need to be able to see what passengers overlap with each other. Then we can iterate through and avoid the ones that have overlap

def merge_ride(pickup, drop, tip):
    out = []

    for i in range(len(pickup)):
        out.append([pickup[i], drop[i], tip[i]])

    return out

def max_earnings(pickup, drop, tip):
    merged = merge_ride(pickup, drop, tip)

    print(merged)

def main():
    pickup = [0, 4, 5]
    drop = [3, 5, 7]
    tip = [1, 2, 2]

    print(max_earnings(pickup, drop, tip))



if __name__ == "__main__":
    main()
