def max_difference(px):
    global_max_range = -1

    mn = min(px[:2])
    mx = max(px[:2])

    for elem in px[2:]:
        new_max_range = elem - mn
        if new_max_range > global_max_range:
            global_max_range = new_max_range
        
        if elem > mx:
            mx = elem

        if elem < mn:
            mn = elem
    
    return global_max_range
        

def main():
    # px = [7, 1, 2, 5]
    # px = [2, 3, 10, 2, 4, 8, 1]
    px = [6, 7, 9, 5, 6, 3, 2]

    print(max_difference(px))

if __name__ == "__main__":
    main()