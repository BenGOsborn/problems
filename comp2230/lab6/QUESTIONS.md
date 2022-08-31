# Questions

## Tutorial

### 1

Insertion sort also has to consider shifting the remaining elements of the sorted array to make room for the next element, therefore in addition to logn for the sort we have to consider the O(n) time to move the elements, therefore we have O((logn + n) \* n) = O(n^2)

### 2

c[0, 10] = 0
Update c with the respective counts of each element in the given array

From there, we accumulate the sums of each element together

We then take these accumulated indexes, and add the current element to the array until we get to the index of the next element, in which we repeat the same process until we get to the end

This results in

[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17]
[0, 0, 1, 1, 0, 0, 0, 0, 1, 1, 2, 0, 0, 0, 0, 1, 0, 1]

[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17]
[0, 0, 1, 2, 2, 2, 2, 2, 3, 4, 6, 6, 6, 6, 6, 7, 7, 8]

Now we shift to the right

[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17]
[0, 0, 0, 1, 2, 2, 2, 2, 2, 3, 04, 06, 06, 06, 06, 06, 07, 07] (and then the last one until the end of the index)

Then we print

[2, 3, 8, 9, 10, 10, 15, 17]

### 3

Assuming that there is not an error in for k = 1 to m as we do not need to iterate that far so far

It does actually work by filling in based off of how many times the element has been seen in its correct positions, however, it is not stable as it reverses the relative order of the sort keys

### 4

Two sum - DONE

### 5

Modified merge algorithm - DONE

### 6

Create a sorted array at the front of the array

| 14 40 31 28 3 15 17 51

14 | 40 31 28 3 15 17 51

40 14 | 31 28 3 15 17 51

14 31 40 | 28 3 15 17 51

14 28 31 40 | 3 15 17 51

3 14 28 31 40 | 15 17 51

3 14 15 28 31 40 | 17 51

3 14 15 17 28 31 40 | 51

3 14 15 17 28 31 40 51 |

---

3 14 15 17 28 31 40 51

### 7

Consider we partition around one of the elements 28

Make it so that all elements that come before 28 appear before it in any order, and make sure all the elements after 28 come after it in any order

14 40 31 | 28 | 3 15 17 51

->

14 3 15 17 | 28 | 31 51 40

^ Partition one - from there, we would go to each subarray recursively and keep partitioning until the elements were all ordered

## Homework

### 8

[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17]
[0, 0, 1, 1, 0, 0, 0, 0, 1, 1, 01, 00, 00, 00, 00, 01, 00, 01]
[0, 0, 1, 2, 2, 2, 2, 2, 3, 4, 05, 05, 05, 05, 05, 06, 06, 07]
[0, 0, 0, 1, 2, 2, 2, 2, 2, 3, 04, 05, 05, 05, 05, 05, 06, 06]

[2, 3, 8, 9, 10, 15, 17]

### 9

We would still have nlogn to remove the elements in the heap, however if all of insert was n time then we would still have nlogn

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

Quicksort in the worst case is where all of the elements are out of order

For each partition we make, we will have a runtime of n time complexity, such as it follows 1 + 2 + 3 + 4 + .. + n = n(n + 1) / 2 worst case

Since n(n + 1) / 2 <= cn^2 where c = 10, and n(n + 1) / 2 >= cn^2 where n = 1, then we see that since our Big O is n^2 and our big omega is n^2, then our big theta is also n^2 for the worst case

### 13

<!-- TODO -->

### 14

If we pick the middle element for each pivot which is optimal as it divides the sets evenly as the list is already sorted, then we will end up with nlogn time

### 15

Mergesort will halve the number of elements in the array each time until it gets to a single element, and then will merge each section together in O(n) time, therefore we have 2logn \* n = O(nlogn)

### 16

Merge sort - DONE
