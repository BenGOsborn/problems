# Questions

## 1

Coin weighting problem for n = 5 using 3 weightings in the worst case
We need to determine if a coin is heavier or lighter

Algorithm

-   We will weigh 2 coins at a time
-   If the coins are equal, we can remove them from the array and determine that they are not the bad coin
-   If the coins are not equal, we know that ONE of them is the bad coin, but we do not know which one. At this point, we know that none of the other coins could possibly be bad
-   We will then have to do 2 comparisons with the remaining good coins. Whichever coin is equal we will know it is the good coin, and for the remaining coin we will determine if it tips up or down which corresponds to being lighter or heavier respectively

## 2

With reference to the previous algorithm
Proof
Since we know that when we use a coin pair and they are equal, they both must be good coins This means that we can write them off and only deal with the previous one Therefore, since we have an odd number of coins, we will use the pigeonhole principle with groups of 2 as a 2 coin pair into the 5 coins to determine the last coin However, we also need to determine if the coin is heavier or lighter, which will require another attempt with a previous good coin, which we will use to determine if it is greatest Therefore, in the worst case, we cannot solve this in less than 3 attempts

## 5

Using masters theorm, we have T(n) = 4T(n / 2) + n ^ 0

We have a = 4, b = 2, and k = 0

Therefore 4 > 2 ^ 0, so we have O(n^2)

## 6

Algorithm

-   We will do our first attempt which will yield 2 good coins (as this is worst cast)
-   From here, we know that our remaining coins will contain one bad (without having to test)
-   We will then have to test one coin against one of the previous good coins, which as the worst case will yield the good coin
-   This means the remaining 4th coin will be the bad one, but we have to determine if it is the heavier or the lighter coin, which we will weigh against one of our good ones to determine again

## 7

With reference to the previous algorithm

We need at minimum 3 attempts for the worst case which are necessary to complete the condition

-   The first do a first attempt which will allow us to narrow down where the bad coin is (as required)
-   We then need a second attempt to figure out which coin is the bad coin out of the remainders
-   We then need a third attempt to determine if it is lighter or less

All of these conditions are required to satisfy the algorithm, and therefore we need to perform these 3 steps in the worst case as we cannot know the next step without the previous

## 8

Why not weigh 5 coins against 5 coins, and in that case we will only have to check the remainder ones, which will result in 3 times in the worst case scenario

## 9

This can be thought of like a 2d binary search. We will first determine the row in logn time, and then we will determine the column, giving us a logn response

For example, we will ask if the pictures row is greater than or equal to row 4 (half of our current row), and based on its answer, we will get rid of a particular section we have to search. Once we have finished with this, we will then only have to search through the columns of the row we are left with using the same approach until we find the picture

## 10

Topological sort: We will hit every vertex in the graph once and we will explore every edge in the graph once, therefore we have O(|V| + |E|) time complexity. O(|V| + |E|) for the worst case, and ohm(|V| + |E|) in the best case, therefore these are our lower and upper bounds which converge to theta(|V| + |E|) time complexity
