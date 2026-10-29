# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


"""
      5 (4,5)
    4   6 (5,6)
       3  7

for each node bottom to top we run dfs and check if the current node is less than the right min and greater than the max left

for each node we did dfs on return the min,max of each node so we can compare when we return 

right check 
- current node is less than the right's min

left check
- current node is greater than the left's max


for each node replace it's value with the min

"""



class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:


        def dfs(node, minLeft, rightMax):
            if not node:
                return True
            if node.val <= minLeft or node.val >= rightMax:
                return False
            
            return dfs(node.left, minLeft, node.val) and dfs(node.right, node.val, rightMax)
         
        return dfs(root, float('-inf'), float('inf'))    
            
            




        
       
            

        