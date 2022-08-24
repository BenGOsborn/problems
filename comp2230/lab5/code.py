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
