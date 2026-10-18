# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 is None and list2 is None:
            return None
        if list1 is None:
            return list2
        if list2 is None:
            return list1
        
        if list2.val < list1.val:
            temp = list1
            list1 = list2
            list2 = temp
        
        tempHead = list1

        prev = list1
        list1 = list1.next
        
        while list1 is not None and list2 is not None:
            if list2.val < list1.val:
                prev.next = list2
                list2 = list2.next
                prev.next.next = list1
                prev = prev.next
            else:
                prev = list1
                list1 = list1.next
        
        if list1 is None:
            prev.next = list2
        
        return tempHead