# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head is None:
            return False
        p1 = head
        p2 = head
        p1 = p1.next
        p2 = p2.next
        if p2 is not None:
            p2 = p2.next
        else:
            return False
        while p1 != p2 and p1 is not None and p2 is not None:
            p1 = p1.next
            p2 = p2.next
            if p2 is not None:
                p2 = p2.next
        return p1 == p2