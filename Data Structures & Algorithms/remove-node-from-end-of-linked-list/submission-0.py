# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # reverse the whole list
        prev = None
        curr = head
        while curr is not None:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        
        # set the reversed head to the end node
        reverseHead = prev

        # make the removal
        dummy = ListNode(0, reverseHead)
        curr = dummy
        for i in range(n - 1):
            curr = curr.next
        curr.next = curr.next.next
        reverseHead = dummy.next

        # reverse the whole list
        prev = None
        curr = reverseHead
        while curr is not None:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp

        return prev