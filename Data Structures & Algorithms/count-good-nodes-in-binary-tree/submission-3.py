# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        count = 0 

        def dfs(curr, largest):
            nonlocal count
            if not curr:
                return 
            

            if curr.val >= largest:
                largest = curr.val
                count+=1 

            dfs(curr.left, largest)
            dfs(curr.right,largest)

        dfs(root, root.val)

        return count

        


        