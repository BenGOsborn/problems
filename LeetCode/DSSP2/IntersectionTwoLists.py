# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA, headB):
        if not headA or not headB:
            return None

        pointer_a = headA
        pointer_b = headB

        # If they are of uneven lengths, the first iteration over the list is used to compensate for the offset to get them from the exact distance length from the end
        # Realistically we could have also just counter the elements in the list and done some iterations to get to that spot, then begun our checks

        while pointer_a and pointer_b and pointer_a != pointer_b:
            pointer_a = pointer_a.next
            pointer_b = pointer_b.next

            # Only can happen when the two are the same OR when they reach the end of the second iteration and are both none
            if pointer_a == pointer_b:
                return pointer_b

            if not pointer_a:
                pointer_a = headB

            if not pointer_b:
                pointer_b = headA

        return pointer_a