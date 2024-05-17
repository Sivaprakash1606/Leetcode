# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        self.count = 0  
        if root:
            self.counts(root)
        return self.count
    
    def counts(self, root):
        if root is None:
            return
        self.count += 1  
        self.counts(root.left)
        self.counts(root.right)
