def max_difference(px):
    global_max_range = -1

    mn = px[0]
    mx = px[1]

    for elem in px[1:]:
        new_max_range = elem - mn
        if new_max_range > global_max_range:
            global_max_range = new_max_range
        
        if elem > mx:
            mx = elem

        if elem < mn:
            mn = elem
    
    return global_max_range if global_max_range > 0 else -1
        

def main():
    # px = [7, 1, 2, 5]
    # px = [2, 3, 10, 2, 4, 8, 1]
    px = [7, 9, 5, 6, 3, 2]
    

    print(max_difference(px))

if __name__ == "__main__":
    main()