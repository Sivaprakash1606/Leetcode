# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isEvenOddTree(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True
        queue=[root]
        level=0
        while queue:
            l=len(queue)
            res=[]
            prev=None
            for i in range(l):
                current=queue.pop(0)
                if level%2 ==0:
                    if current.val %2==0 or (prev is not None and prev>=current.val):
                        return False
                if level%2 ==1:        
                    if current.val %2==1 or (prev is not None and prev<=current.val):
                        return False    
                prev=current.val
                if current.left:
                    res.append(current.left)
                if current.right:
                    res.append(current.right)
            queue=res
            level=level+1
        return True     



        