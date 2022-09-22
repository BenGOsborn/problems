# Lab 9

## Questions

### Question 3

. A B C D
A 0 0 1 0
B 1 0 0 0
C 0 0 0 1
D 0 1 0 0

C_A = {B}, R_A = {C}, C_A x R_A = {(B, C)}

. A B C D
A 0 0 1 0
B 1 0 1 0
C 0 0 0 1
D 0 1 0 0

C_B = {D}, R_B = {A, C}, C_B x R_B = {(D, A), (D, C)}

. A B C D
A 0 0 1 0
B 1 0 1 0
C 0 0 0 1
D 1 1 1 0

C_C = {A, B, D}, R_C = {D}, C_C x R_C = {(A, D), (B, D), (D, D)}

. A B C D
A 0 0 1 1
B 1 0 1 1
C 0 0 0 1
D 1 1 1 1

C_D = {A, B, C, D}, R_D = {A, B, C, D}, C_D x R_D = \*

. A B C D
A 1 1 1 1
B 1 1 1 1
C 1 1 1 1
D 1 1 1 1

### Question 4

Original

0 3 1 2
1 0 6 2
3 2 0 1
2 1 7 0

<!-- k = 0 -->

A[1][2] = inf, A[1][0] + A[0][1] = 1 + 5 = 6 (update)
A[1][3] = 10, A[1][0] + A[0][3] = 1 + 1 = 2 (update)
A[2][3] = 1, A[2][0] + A[0][3] = inf + 1 = inf (no-update)
A[2][1] = 3, A[2][0] + A[0][1] = inf + 5 = inf (no-update)
A[3][1] = 1, A[3][0] + A[0][1] = 7 + 5 = 12 (no-update)
A[3][2] = inf, A[3][0] + A[0][2] = 7 + 1 = 8 (update)

<!-- k = 1 -->

A[0][2] = 1, A[0][1] + A[1][2] = 5 + 6 = 11 (no-update)
A[0][3] = inf, A[0][1] + A[1][3] = 5 + 2 = 7 (update)
A[2][3] = 1, A[2][1] + A[1][3] = 3 + 2 = 5 (no-update)
A[2][0] = inf, A[2][1] + A[1][0] = 3 + 1 = 4 (update)
A[3][0] = 7, A[3][1] + A[1][0] = 1 + 1 = 2 (update)
A[3][2] = 8, A[3][1] + A[1][2] = 1 + 6 = 7 (update)

<!-- k = 2 -->

A[0][1] = 5, A[0][2] + A[2][1] = 1 + 3 = 4 (update)
A[0][3] = 7, A[0][2] + A[2][3] = 1 + 1 = 2 (update)
A[1][3] = 2, A[1][2] + A[2][3] = 6 + 1 = 7 (no-update)
A[1][0] = 1, A[1][2] + A[2][0] = 6 + 4 = 10 (no-update)
A[3][0] = 2, A[3][2] + A[2][0] = 7 + 4 = 11 (no-update)
A[3][1] = 1, A[3][2] + A[2][1] = 7 + 3 = 10 (no-update)

<!-- k = 3 -->

A[0][1] = 4, A[0][3] + A[3][1] = 2 + 1 = 3 (update)
A[0][2] = 1, A[0][3] + A[3][2] = 2 + 7 = 9 (no-update)
A[1][2] = 6, A[1][3] + A[3][2] = 2 + 7 = 9 (no-update)
A[1][0] = 1, A[1][3] + A[3][0] = 2 + 2 = 4 (no-update)
A[2][0] = 4, A[2][3] + A[3][0] = 1 + 2 = 3 (update)
A[2][1] = 3, A[2][3] + A[3][1] = 1 + 1 = 2 (update)

## Homework

### Question 5

#### A

. 1 2 3 4
1 0 1 1 0
2 0 0 0 1
3 0 0 0 0
4 1 0 0 0

C_1 = {4}, R_1 = {2, 3}, C_1 x R_1 = {(4, 2), (4, 3)}

. 1 2 3 4
1 0 1 1 0
2 0 0 0 1
3 0 0 0 0
4 1 1 1 0

C_2 = {1, 4}, R_2 = {4}, C_2 x R_2 = {(1, 4), (4, 4)}

. 1 2 3 4
1 0 1 1 1
2 0 0 0 1
3 0 0 0 0
4 1 1 1 1

C_3 = {1, 4}, R_3 = {}, C_3 x R_3 = {}

C_4 = {1, 2, 4}, R_4 = {1, 2, 3, 4}, C_4 x R_4 = {(1, 1), (1, 2), (1, 3), (1, 4), (2, 1), (2, 2), (2, 3), (2, 4), (4, 1), (4, 2), (4, 3), (4, 4)}

. 1 2 3 4
1 1 1 1 1
2 1 1 1 1
3 0 0 0 0
4 1 1 1 1

#### B

. 1 2 3 4
1 0 1 0 1
2 0 0 1 0
3 0 0 0 1
4 0 0 0 0

C_1 = {}, R_1 = {2, 4}, C_1 x R_1 = {}

C_2 = {1}, R_2 = {3}, C_2 x R_2 = {(1, 3)}

. 1 2 3 4
1 0 1 1 1
2 0 0 1 0
3 0 0 0 1
4 0 0 0 0

C_3 = {1, 2}, R_3 = {4}, C_3 x R_3 = {(1, 4), (2, 4)}

. 1 2 3 4
1 0 1 1 1
2 0 0 1 1
3 0 0 0 1
4 0 0 0 0

C_4 = {1, 2, 3}, R_4 = {}, C_4 x R_4 = {}

### Question 6

(Repeat same process as above)

### Question 8

Since the base cases only return 0 or 1, and the fib(n) relies on a summation or previous values alone, it means that fib(n) base case computations must have occured to be able to generate the number fib(n)

Using induction:

Assume for n = 3, fib(3) results in fib(3) calls (this is true) - initial case is true

Assume that for n = k, fib(k) results in fib(k) calls (inductive hypothesis)

Now let us prove that for n = k + 1, fib(k + 1) results in fib(k + 1) calls

fib(k + 1) = fib(k) + fib(k - 1)

Using our inductive hypothesis, we know that fib(k) and fib(k - 1) result in their respective amount of calls

Therefore, by summing these number of calls together, we get fib(k + 1) calls, therefore the proof is complete

(note this theory only holds for the base case of 0, 0 and 1, 0)

## Extras

### Question 9

Map to adjacency matrix and perform same process as above

### Question 10

for k = 1 to n {
for i = 1 to n {
for j = 1 to n {
...
}
}
}

### Question 12

It is able to do so as it relies on looking at the relationship between the incoming and the outgoing edges for particular nodes, and is then able to add the appropriate transitive edges which it can do simply in place. No additional memory is required for this as it all happens within the same matrix which contains all the relevent information.

The time complexity of Warshall's is O(n ^ 3), as it requires n time for the outer loop, and at most n^2 time for each iteration to perform the inplace update
