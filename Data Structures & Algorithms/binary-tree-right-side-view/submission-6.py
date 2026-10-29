# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        q = deque()

        res = []
        if not root:
            return []
        q.append(root)


        while q:
            temp = []

            for i in range(len(q)):
                curr = q.popleft()
                temp.append(curr.val)
                if curr.left: 
                    q.append(curr.left)
                if curr.right:
                    q.append(curr.right)
            
            res.append(temp)

        final_res = []
        for sub in res:
            final_res.append(sub[-1])

        return final_res