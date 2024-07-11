# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result=[]
        if root is None:
            return result
        else:
            left=self.inorderTraversal(root.left)   
            result=result+left
            result.append(root.val) 
            right=self.inorderTraversal(root.right)  
            result=result+right 
        return result    

        