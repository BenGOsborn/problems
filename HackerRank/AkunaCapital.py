def convert_to_tuple(elem):
    # Return element and number of 1's
    count = 0

    bin_digit = bin(elem)[2:]
    for char in bin_digit:
        if char == "1":
            count += 1

    return (elem, count)

def rearrange(elements):
    mapped = []

    for elem in elements:
        mapped.append(convert_to_tuple(elem))
    
    return [x[0] for x in sorted(mapped, key=lambda x: (x[1], x[0]))]


elements = [1, 2, 3, 4, 89]

print(rearrange(elements))