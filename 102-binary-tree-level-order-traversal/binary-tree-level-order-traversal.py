# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []
        result=[]
        queue=[root]
        while queue:
            val=[]
            level=[]
            for i in queue:
                val.append(i.val)
                if i.left:
                    level.append(i.left)
                if i.right:
                    level.append(i.right)
            queue=level  
            result.append(val)
        return result              

        