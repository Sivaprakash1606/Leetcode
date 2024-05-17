# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def removeLeafNodes(self, root: Optional[TreeNode], target: int) -> Optional[TreeNode]:
        if root:
           return self.dfs(root,target)
        return None   
    def dfs(self,root,target):
        if not root:
            return None    
        root.left=self.dfs(root.left,target)
        root.right=self.dfs(root.right,target)
        if root.left is None and root.right is None and root.val ==target:
            return None
        return root 
                       


        