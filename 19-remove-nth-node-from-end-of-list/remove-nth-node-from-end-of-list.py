# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        current=head
        count=1
        while current:
            current=current.next
            count=count+1 
        count=count-n
        i=1
        prev=None
        current=head
        while current:
            if i == count:
                if prev:
                    prev.next=current.next
                else:
                    head=head.next
                break
            prev=current    
            current=current.next 
            i=i+1 
        return head            
                     

        