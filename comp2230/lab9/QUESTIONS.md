# Lab 9

## Questions

### Question 3

### Question 4

## Homework

### Question 5

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

### Question 12
