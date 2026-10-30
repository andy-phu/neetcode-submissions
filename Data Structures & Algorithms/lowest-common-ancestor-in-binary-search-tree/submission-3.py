# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        """
        
        5,3
        5,3,4


        5,3
        5,8
        
        """
        def backtrack(node):
            if not node:
                return None
            pVal = p.val
            qVal = q.val
            if node.val > pVal and node.val > qVal:
                return backtrack(node.left)
            elif node.val < pVal and node.val < qVal:
                return backtrack(node.right)
            else:
                # if one is equal or the current node is between p and q then that means the current node is the LCA
                return node 


        return backtrack(root)