# **** Wait, first of all we need to be able to see what passengers overlap with each other. Then we can iterate through and avoid the ones that have overlap

def find_endpoint(drop):
    return max(drop)

def merge_ride(pickup, drop, tip):
    out = []

    for i in range(len(pickup)):
        out.append([pickup[i], drop[i], tip[i]])

    return out

def max_earnings(pickup, drop, tip):
    merged = merge_ride(pickup, drop, tip)
    n = find_endpoint(drop)

    x = {}
    for start, end, tip in merged:
        if end not in x:
            x[end] =[[start, tip]]
        else:
            x[end].append([start, tip])
    
    xp = [0] * (n + 1)
    xp[0] = 0
    
    for i in range(1, n + 1):
        xp[i] = xp[i - 1]
        if i in x:
            temp_profit = 0
            for start,tip in x[i]:
                if (i - start) + tip + xp[start] > temp_profit:
                    temp_profit = i - start + tip + xp[start]
            xp[i] = max(xp[i], temp_profit)
            
            
    return xp[-1]

def main():
    pickup = [0, 2, 9, 10, 11, 12]
    drop = [5, 9, 11, 11, 14, 17]
    tip = [1, 2, 3, 2, 2, 1]

    print(max_earnings(pickup, drop, tip))



if __name__ == "__main__":
    main()
