# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        if root is None:
            return []
        result =[]
        queue=[root]
        while queue:
            total=0
            length=len(queue)
            for i in range(length):
                current=queue.pop(0)
                total=total+current.val
                if current.left:
                    queue.append(current.left)
                if current.right:
                    queue.append(current.right)
            result.append(total/length)
        return result            


        