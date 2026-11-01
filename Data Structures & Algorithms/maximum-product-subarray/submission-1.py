class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        """
        - at each index you get to choose what is greater the index itself 
        or the index to the right's greatest product times the current index 
        - each index represents the max product from that index to the end 
        
        [-3,1,-1]
        [-3,-1,-1]
        
        globalMax = 8

        max = -15
        min = -24

        [2,4,-3,5]
             i

        options are 
        1. multiply max to current 
        2. multiply min to current 
        3. current 

        [-3,-1,-1]
                i
        global = 3
        max = -1
        min = -3


        
        """

        res = nums[0]
        minPrev = nums[0]
        maxPrev = nums[0]

        for i in range(1, len(nums)):
            current = nums[i]
            maxCurrent = maxPrev * current
            minCurrent = minPrev * current 

            maxPrev, minPrev = max(current, maxCurrent, minCurrent), min(current, maxCurrent, minCurrent)

            res = max(res, maxPrev, minPrev)

        return res


