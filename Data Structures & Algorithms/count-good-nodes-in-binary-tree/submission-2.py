# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        curr = root 
        max_val = 0 

        count = 0 

        def inOrder(node, max_val):
            nonlocal count
            if not node:
                return

            if node.val >= max_val:
                max_val = node.val
                count += 1 

            inOrder(node.left, max_val)
            inOrder(node.right, max_val)
            return 

        inOrder(root, root.val) 
        return count

        