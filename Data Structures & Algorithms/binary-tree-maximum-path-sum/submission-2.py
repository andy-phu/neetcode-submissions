# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        max_path = root.val

        def dfs(node):
            nonlocal max_path
            if not node:
                return 0

            leftMax = max(dfs(node.left), 0)
            rightMax = max(dfs(node.right), 0)
            better_path = max(leftMax, rightMax) + node.val
            max_path = max(max_path, leftMax + rightMax +  node.val)
            return better_path

        dfs(root)

        return max_path