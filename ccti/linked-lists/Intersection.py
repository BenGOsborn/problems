class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


# Determine if the two linked lists intersect at a given node

# Algorithm
# - Loop through both lists once and find the size of both of the lists
# - If they are both the same size, we will just loop through and check if two nodes have the same value
# - If they are not the same size, we will loop through the larger one the difference amount of times to compensate for the offset, then do our checks
# - Time: O(n + m) (where n and m are the respective sizes of each list) | Space: O(1)

def is_intersection(list1, list2):
    s1 = 0
    s2 = 0

    curr_1 = list1
    curr_2 = list2

    while curr_1 is not None:
        s1 += 1
        curr_1 = curr_1.next

    while curr_2 is not None:
        s2 += 1
        curr_2 = curr_2.next

    curr_1 = list1
    curr_2 = list2

    if s1 != s2:
        diff = abs(s1 - s2)

        if s1 > s2:
            for _ in range(diff):
                curr_1 = curr_1.next
        else:
            for _ in range(diff):
                curr_2 = curr_2.next

    while curr_1 is not None:
        if curr_1 == curr_2:
            return True

        curr_1 = curr_1.next
        curr_2 = curr_2.next

    return False
