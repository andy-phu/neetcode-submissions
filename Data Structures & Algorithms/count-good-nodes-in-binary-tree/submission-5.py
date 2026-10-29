# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:


        def dfs(curr, largest):

            if not curr:
                return 0
            
            res = 0 
            if curr.val >= largest:
                largest = curr.val
                res = 1 


            res += dfs(curr.left, largest)
            res += dfs(curr.right,largest)

            return res 


        

        return dfs(root, root.val)

        


        