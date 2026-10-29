class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        """
        - get the half of the sum of nums
        - find a subset whos sum is exactly equal to half
        - if the total is odd then it's automatically false
        - left and right pointers and track the sum to find all the subsets
        - basically want to create a tree for each of these elements in nums where each branch is the current index + 1 : len(nums) - 1 
        """


        x = sum(nums)

        if x % 2 != 0: 
            return False

        half = x // 2
        dp = {}

        def subsets(i,total):
            if (i,total) in dp:
                return dp[(i, total)]
            if total == half:
                return True
            if total > half or i >= len(nums):
                return False


            res = subsets(i+1, total + nums[i]) or subsets(i+1, total)
            dp[(i,total)] = res 
            return res 

        return subsets(0,0)
            