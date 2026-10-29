class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        my_dict = {}
        for i, n in enumerate(nums):
            if target - n in my_dict:
                return [my_dict[target-n], i]
            my_dict[n] = i
            
