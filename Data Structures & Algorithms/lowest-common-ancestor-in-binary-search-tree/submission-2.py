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


        path_p = []
        path_q = []
        def backtrack(node, targetNode, path):
            if not node:
                return

            path.append(node) 

            if node == targetNode:
                return True

            if backtrack(node.left, targetNode, path) or backtrack(node.right, targetNode, path):
                return True
            else:
                path.pop()
                return False 
            
        
        backtrack(root, p, path_p)
        backtrack(root, q, path_q)

        l,r = 0,0 
        res = root
        while l < len(path_p) and r < len(path_q):
            if path_p[l].val == path_q[r].val:
                res = path_p[l]
            else:
                break
            l += 1
            r += 1

        return res
