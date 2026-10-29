class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        """
          index 0 
          -2    +2
          index 1
        -2  +2  -2 +2 
        
        
        """

        dp = {}

        def backtrack(idx, total):
            if (idx, total) in dp:
                return dp[(idx, total)]
            if idx >= len(nums):
                if total == target: 
                    return 1
                else:
                    return 0 
        

            res = backtrack(idx+1, total - nums[idx]) + backtrack(idx+1, total + nums[idx])
            dp[(idx, total)] = res 
            return res 

        return backtrack(0, 0)
