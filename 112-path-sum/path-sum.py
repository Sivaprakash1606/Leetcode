# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False
        # Check if root is a leaf node and its value matches targetSum
        if root.left is None and root.right is None:
            return root.val == targetSum
        
        left = root.val
        right = root.val
        
        # Check paths from the left and right children
        if root.left:
            if self.dfs(root.left, left, targetSum):
                return True
        if root.right:
            if self.dfs(root.right, right, targetSum):
                return True
        
        return False
    
    def dfs(self, root, total, targetSum):
        total = total + root.val
        if root.left is None and root.right is None:
            return total == targetSum
        if root.left:
            if self.dfs(root.left, total, targetSum):
                return True
        if root.right:
            if self.dfs(root.right, total, targetSum):
                return True
        return False