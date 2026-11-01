class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)

        if total % 2 != 0: return False 

        half = total // 2 


        #basically want to try all the combinations to see if it's possible to get a combination that is equal to the half 
        #can do dp where we get all the numbers from 0 to half and see if it's possible 



        def dfs(i, amt):
            if i >= len(nums) or amt > half: return False 
            
            if amt == half: return True 

            return dfs(i+1, amt + nums[i]) or dfs(i+1, amt)

        return dfs(0, 0)


