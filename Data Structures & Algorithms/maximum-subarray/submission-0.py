class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        """
        [2,-3,4,-2,2,1,-1,4]
        l
        r

        1st choice: do we want to expand r
        2nd choise: do we want to move l to r and run dfs from r
        """ 

        res = float('-inf')
        prev = float('-inf')
        for i in range(len(nums) - 1, -1, -1):
            prev = max(nums[i], prev + nums[i])
            res = max(prev, res)

        return res
