# Questions

## Tutorial

### 1

Insertion sort also has to consider shifting the remaining elements of the sorted array to make room for the next element, therefore in addition to logn for the sort we have to consider the O(n) time to move the elements, therefore we have O((logn + n) \* n) = O(n^2)

### 2

<!-- TODO -->

### 3

<!-- TODO -->

### 4

Two sum - DONE

### 5

Modified merge algorithm - DONE

### 6

<!-- TODO -->

### 7

<!-- TODO -->

## Homework

### 8

<!-- TODO -->

### 9

<!-- TODO -->

### 10

Prove sorting algorithm has worst case of minimum when adjacent swapping elements n^2

-   Consider a simple algorithm where the elements can only swap with their adjacent
-   This means for each element to get where it needs to go is linear with the size of the array
-   Therefore, we have n elements that can be ordered in n time
-   Consider the worst case, where the elements are ordered in the opposite order
-   Order eaching element will be 1 + 2 + 3 + ... + n = n(n + 1) / 2 time in the worst case minimum, without doing any extra swaps

### 11

Prove insertion sort runtime is theta(n ^ 2) - we just need to get the average time, and then put it between the elements ???

We know that we will not have to do more than n swaps for n elements, therefore the big O is O(n \* n) = O(n^2)

We also know that the algorithm in the worst case runs with complexity 1 + 2 + 3 + ... + n = n(n + 1) / 2. Therefore, since both Big O and Big omega run in n^2 time, big theta also is n^2 = theta(n^2)

## Extra questions

### 12

<!-- TODO -->

### 13

<!-- TODO -->

### 14

<!-- TODO -->

### 15

Mergesort will halve the number of elements in the array each time until it gets to a single element, and then will merge each section together in O(n) time, therefore we have 2logn \* n = O(nlogn)

### 16

Merge sort - DONE
