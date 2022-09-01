# Questions

## Q2

Since the least numbered nodes are preferred, start with 1 and search from there

4 7 1 2 5 8 9 6 3

## Q3

[1 2 3 4 5 6 7]

---

[2 1 3 4 5 6 7]
[2 4 3 1 5 6 7]
[2 4 3 1 5 6 7]

We will swap the current level of the element with the elements at the next height of the tree if the element below it is greater

## Q4

Depth first search requires to search the nodes of the most recently found node, and therefore the stack lends itself to this, where the most recent element added is the top of the stack, and therefore we explore from this most recent element and keep doing this

Breadth first search requires a searching of the elements in the order in which they are found and requires a LIFO ordering, and therefore a queue is suited to this task, where elements retrieved last are dealt with first compared to newly added elements - allows us to maintain the ordering of the elements

## Q6

[1 5 | 8 3 9 2]
[1 5 8 | 3 9 2]
[1 3 5 8 | 9 2]
[1 3 5 8 9 | 2]
[1 2 3 5 8 9 |]
