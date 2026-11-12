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

        while l < r: 
            mid = (r+l) // 2

            if nums[mid] >= nums[r]:
                l = mid + 1
            else:
                r = mid

        return nums[l]

            