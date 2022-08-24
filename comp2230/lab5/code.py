# 1

# Coin weighting problem for n = 5 using 3 weightings in the worst case
# We need to determine if a coin is heavier or lighter

# Algorithm
# - We will weigh 2 coins at a time
# - If the coins are equal, we can remove them from the array and determine that they are not the bad coin
# - If the coins are not equal, we know that ONE of them is the bad coin, but we do not know which one. At this point, we know that none of the other coins could possibly be bad
# - We will then have to do 2 comparisons with the remaining good coins. Whichever coin is equal we will know it is the good coin, and for the remaining coin we will
# determine if it tips up or down which corresponds to being lighter or heavier respectively

# 2

# With reference to the previous algorithm
# Proof
# Since we know that when we use a coin pair and they are equal, they both must be good coins
# This means that we can write them off and only deal with the previous one
# Therefore, since we have an odd number of coins, we will use the pigeonhole principle with groups of 2 as a 2 coin pair into the 5 coins to determine the last coin
# However, we also need to determine if the coin is heavier or lighter, which will require another attempt with a previous good coin, which we will use to determine if it is greatest
# Therefore, in the worst case, we cannot solve this in less than 3 attempts

# 3 (Topological sort)

# Algorithm
# - DFS through the nodes, and before navigating to a node we will check if has been reached
# - If all of the children of the current node have been marked, then we can set the current node as marked
# - Else, we will have to recursively DFS through the children nodes and mark them off recursively
# - We will store all of the marked off nodes in an out array (if they have not already been seen of course)


def topological_sort_helper(graph, key, out, finished):
    for elem in graph[key]:
        if elem not in finished:
            topological_sort_helper(graph, elem, out, finished)

    out.append(key)
    finished[key] = True


def topological_sort(graph):
    seen = {}
    out = []

    for key in graph.keys():
        if key not in seen:
            topological_sort_helper(graph, key, out, seen)

    return out


gr_3 = {"1": ["3"], "2": ["3"], "3": ["4", "6"], "4": [], "5": ["2", "6", "8"], "6": [
    "4", "9"], "7": ["4", "10"], "8": ["9"], "9": ["10"], "10": []}
out = []
print(topological_sort(gr_3))
