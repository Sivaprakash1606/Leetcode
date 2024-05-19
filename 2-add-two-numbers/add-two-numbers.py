# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        current1 = l1
        current2 = l2
        result = ListNode()
        current = result
        rem = 0
        while current1 or current2:
            if current1 :
                val1=current1.val
            else:
                val1=0    
            if current2 :
                val2=current2.val
            else:
                val2=0    
            p = val1 + val2 + rem
            if p >= 10:
                rem = 1
                p = p - 10
                current.next = ListNode(p)
            else:
                rem=0
                current.next = ListNode(p)  
            if current1:    
                current1 = current1.next
            if current2:    
                current2 = current2.next
            current=current.next    
        if rem > 0:      
            current.next = ListNode(rem)
        return result.next
