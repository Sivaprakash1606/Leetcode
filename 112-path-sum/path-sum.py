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
        left=root.val
        right=root.val
        l=False
        r=False
        if root.left is None and root.right is None and targetSum == root.val:
            return True
        if root:
            if root.left:
                l=self.dfs(root.left,left,targetSum)
            if root.right:
                r=self.dfs(root.right,right,targetSum)  
            if l or r:
                return True
            return False        
    
    def dfs(self,root,total,targetSum ):
        if not root:
            return False
        total=total+root.val
        if root.left is None and root.right is None and total == targetSum:
            return True
        if root.left:
            if self.dfs(root.left,total,targetSum):
                return True
        if root.right: 
            if self.dfs(root.right, total, targetSum):
                return True        
        return False    

        



        