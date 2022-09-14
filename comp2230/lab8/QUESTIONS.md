# Lab 8

## Question 1

Alphabet size = 2
Window size = 3

101, 011010011001110

P[i] = {1: 0, 2: 1}

## 1.1.

Prime no = 2

Hash 101 = ((2^2 _ 2) % 2 + (2^1 _ 1) % 2 + (2^0 \* 2) % 2) % 2 = 0

Hash 011 = ((2 ^ 2 _ 1) % 2 + (2^1 _ 2) % 2 + (2^0 \* 2) % 2) % 2 = 0
Compare; fails to match at index = 0

Hash 110 = ((2 ^ 2 _ 2) % 2 + (2^1 _ 2) % 2 + (2^0 \* 1) % 2) % 2 = 1
Bad hash; don't compare

Hash 101 = ((2^2 _ 2) % 2 + (2^1 _ 1) % 2 + (2^0 \* 2) % 2) % 2 = 0
Compare; matches. Terminate

We used 2 comparisons

## 1.2.

Prime no = 5

Hash 101 = ((2^2 _ 2) % 5 + (2^1 _ 1) % 5 + (2^0 \* 2) % 5) % 5 = 2

Hash 011 = ((2 ^ 2 _ 1) % 5 + (2^1 _ 2) % 5 + (2^0 \* 2) % 5) % 5 = 0
Bad hash; don't compare

Hash 110 = ((2 ^ 2 \* 2) % 5 + (2^1 \* 2) % 5 + (2^0 \* 1) % 5) % 5 = 3
Bad hash; don't compare

Hash 101 = ((2^2 _ 2) % 5 + (2^1 _ 1) % 5 + (2^0 \* 2) % 5) % 5 = 2
Compare; matches. Terminate

We used 1 comparison

## 1.3.

Worst case where every hash matches the specified hash, out loop loops n - m + 1 times, as this is the maximum index before out pattern goes over the end of the search string
From there, if our hashes collide each time, we have to do m searches for each index we land on in the outerloop

Therefore, we have O(m(n - m + 1)) worst case

## Question 2

## 2.1

[p, a, p, p, a, r]
[0, 1, 2, 3, 4, 5]
[0, 0, 1, 1, 2, 0]

[a, b, a, b, b, c, a, b, a, b]
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
[0, 0, 1, 2, 0, 0, 1, 2, 3, 4]
