# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        #each node contains the max path 
        #each node can have a path 
        #1. node itself
        #2. node + left + right
        #3. node + left
        #4. node + right
        #for each node after getting the max we want to update res 
        #each time we backtrack left or right we update that node's value to the max path it can have


    #      1
    #     2 ,
    #    3 , 
    #   4 ,
    #  , 5
        res = float('-inf')


        def backtrack(node): 
            nonlocal res
            nodeSum = node.val
            
            leftVal, rightVal = 0,0 
            if node.left:
                backtrack(node.left)
                leftVal = node.left.val
                
            if node.right:
                backtrack(node.right)
                rightVal = node.right.val

            node.val = max(nodeSum, nodeSum + leftVal, nodeSum + rightVal)
            res = max(res, max(nodeSum, nodeSum + leftVal, nodeSum + rightVal, nodeSum + leftVal + rightVal))
        backtrack(root)
        return res