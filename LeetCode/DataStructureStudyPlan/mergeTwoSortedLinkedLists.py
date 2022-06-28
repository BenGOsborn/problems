class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1, list2):
        out = None
        out_ptr = None

        # **** Now what we will do is simply iterate through the different lists from their head, check them one by one, and then add them to the list in the correct order
        # **** This will have to be updated on our first visit to point to out