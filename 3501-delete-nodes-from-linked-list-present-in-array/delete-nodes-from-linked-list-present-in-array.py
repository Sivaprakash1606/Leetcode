# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def modifiedList(self, nums: List[int], head: Optional[ListNode]) -> Optional[ListNode]:
        s=set(nums)
        while head and head.val in s:
            head=head.next

        if not head:
            return None

        prev=head
        current=head.next
        while current:
            if current.val not in s:
                prev.next=current
                prev=current
            current=current.next
        prev.next=None    
        return head              
        