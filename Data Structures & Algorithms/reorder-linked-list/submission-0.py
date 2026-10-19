# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # get length of linked list
        curr = head
        listLength = 0
        while curr.next is not None:
            listLength += 1
            curr = curr.next
        
        # calculate split point of first/second half
        split = listLength // 2
        
        # get to second half
        curr = head
        for i in range(split):
            curr = curr.next

        # set first half of list to end on null
        temp = curr.next
        curr.next = None
        
        # set up for reversing portion
        prev = None
        curr = temp

        # reverse second half of linked list
        while curr is not None:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp

        ### merge lists

        # r is the reversed list's head
        r = prev

        # lprev and lcurr are the pointers for the main list
        lprev = head
        lcurr = head.next

        while lcurr is not None:
            lprev.next = r
            r = r.next
            lprev.next.next = lcurr
            
            # move main list pointers to next valid interval
            lprev = lcurr
            lcurr = lcurr.next
        lprev.next = r




