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

### Question 10

for k = 1 to n {
for i = 1 to n {
for j = 1 to n {
...
}
}
}

### Question 12
