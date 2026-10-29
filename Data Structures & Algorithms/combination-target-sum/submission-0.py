class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        """
            2
            2  5
            2   5 6
        


        two options per index
        1. choose the same index
        2. go to the next index

        """ 


        res = []
        combination = []
        def backtrack(i, current):
            if current == target:
                res.append(combination.copy())
                return 
            if i >= len(nums) or current > target:
                return 
            

            combination.append(nums[i])
            backtrack(i, current + nums[i])
            combination.pop()
            backtrack(i+1, current)

        backtrack(0, 0)

        return res 
            