class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        """
        - get the half of the sum of nums
        - find a subset whos sum is exactly equal to half
        - if the total is odd then it's automatically false
        - left and right pointers and track the sum to find all the subsets
        - basically want to create a tree for each of these elements in nums where each branch is the current index + 1 : len(nums) - 1 
        """


        total = sum(nums)

        if total % 2 != 0: 
            return False

        half = total // 2


        def subsets(i,total):
            if total == half:
                return True
            if total > half or i >= len(nums):
                return False


            return subsets(i+1, total + nums[i]) or subsets(i+1, total)

        return subsets(0,0)
            