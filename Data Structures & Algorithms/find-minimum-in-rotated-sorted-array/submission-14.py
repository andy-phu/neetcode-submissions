class Solution:
    def findMin(self, nums: List[int]) -> int:
        """
        - inflection point is the greatest element in the array 
        - the min would either be the one to the right or if the 
        inflection is the last element the min is the one to the right 
        
        - inflection point as the min would be 
        - everything to the right is greater and everything to the left is greater 
        
        """


        l,r = 0, len(nums) - 1
        res = nums[0]

        while l <= r: 
            if nums[l] < nums[r]:
                res = min(res, nums[l])

            mid = (r+l) // 2

            res = min(res, nums[mid])

            if nums[mid] >= nums[l]:
                l = mid + 1
            else:
                r = mid - 1

        return res

            