class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        #can contain duplicates as long as their index isn't the same 
        #no need to sort because it's okay if the number is the same 

        res = []
        subset = []
        candidates.sort()

        def dfs(index, total):
            if total == target:
                res.append(subset.copy())
                return
            if index >= len(candidates):
                return 

            subset.append(candidates[index])
            dfs(index + 1, total + candidates[index])
            subset.pop()

            while index+1 < len(candidates) and candidates[index] == candidates[index + 1]:
                index += 1 
            dfs(index + 1, total)

        dfs(0,0)

        return res
