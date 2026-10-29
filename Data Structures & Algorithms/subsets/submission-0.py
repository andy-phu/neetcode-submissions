class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        res.append([])
        def dfs(temp, index):

            if index >= len(nums):
                return 

            temp.append(nums[index])
            print(f"index: {index} temp: {temp}")
            
            res.append(temp.copy())
            #include the next one 
            dfs(temp,index+1)
            #exclude the next one
            temp.pop()
            dfs(temp,index+1)

        dfs([],0)
        return res