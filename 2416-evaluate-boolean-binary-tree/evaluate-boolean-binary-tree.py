# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def evaluateTree(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return False
        if root.val == 1:
            return True    
        if root:
            left = self.dfs(root.left)
            right = self.dfs(root.right) 
            if root.val == 2:
                return left or right
            elif root.val == 3:
                return left and right    
                
    def dfs(self, root):
        if root is None:
            return False
        if root.val <= 1:
            if root.val == 0:

                return False
            return True
        if root.val == 2: 
            return self.dfs(root.left) or self.dfs(root.right)
        elif root.val == 3:
            return self.dfs(root.left) and self.dfs(root.right)
