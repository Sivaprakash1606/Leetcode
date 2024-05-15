# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []
        result=[]
        queue=[root]
        while queue:
            res=[]
            r=[]
            for i in queue:
                res.append(i.val)
                if i.left:
                    r.append(i.left)
                if i.right:
                    r.append(i.right)
            queue=r
            result.append(res)
        return result[::-1]

        