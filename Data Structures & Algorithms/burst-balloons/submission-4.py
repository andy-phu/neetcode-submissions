class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        """
        - burst every baloon and do backtracking 
        - every path reduces the input and you have to try all the options choose the path with the max 
        - stop when there is nothing left in nums 


        [8, 24, 42, 21]

        1[4,2,3,7]1
          l  
            i
                r

        1[4,2,3,7]1
          l  
            i
            r

        1[4,2,3,7]1
            l  
            i
                r





        """

        cache = {}
        nums = [1] + nums + [1]
        def dfs(l, r): 
            if (l,r) in cache: 
                return cache[(l,r)]
            if l > r:
                return 0
            
            points = 0
            for i in range(l,r+1): 
                curr = nums[l-1] * nums[i] * nums[r+1]
                points = max(points, curr + dfs(l,i-1) + dfs(i+1,r))
            
            cache[(l,r)] = points
            return points

        res = dfs(1,len(nums)-2)
        return res
