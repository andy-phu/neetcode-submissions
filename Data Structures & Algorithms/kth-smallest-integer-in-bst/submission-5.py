# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        count = k
        res = [1]
        def inOrder(node):
            nonlocal count
            if not node:
                return

            inOrder(node.left)
            if count == 0:
                return
            count -= 1
            if count == 0:
                res[0] = node.val
                return
            
            inOrder(node.right)  
  

        inOrder(root)

        return res[0]
    