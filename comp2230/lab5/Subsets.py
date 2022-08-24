# Generate all subsets from a given set

# Algorithm
# - We will first just work on generating the combinations for a particular row, which we can easily use to generate the entire subset tree
# - To generate for a row, the next digit of our generate string needs to be greater than it, and NOT equal
# - We will do this recursively for each element in the until we have sufficient digits
# - Inside of each, we will use recursive backtracking to increment the element, which will raise the previous digit and then start again
# - We will store all of our digits in an out array

def subset_row(row, set_size, current, out):
    if len(current) == row:
        out.append(current)
        return

    index = current[-1] + 1 if len(current) > 0 else 0
    for i in range(index, set_size):
        subset_row(row, set_size, current[:] + [i], out)


def subsets(set_size):
    out = []

    for row in range(set_size + 1):
        temp = []
        subset_row(row, set_size, [], temp)
        out += temp

    return out


set_size = 4
out = subsets(set_size)
print(out)
