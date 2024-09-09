# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        result=None
        l=1
        current=head
        while current :
            if l>=left and l<=right:
                temp=ListNode(current.val)
                temp.next=result
                result=temp
            current=current.next
            l=l+1
        l=1
        current=head
        while current :  
            if l>=left and l<=right:
                current.val=result.val
                result=result.next
            current=current.next
            l=l+1      
        return head         

          
            
                


