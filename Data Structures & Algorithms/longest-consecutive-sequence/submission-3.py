class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        longest = 0
        for num in nums_set:
            if num-1 not in nums_set:
                streak = 1
                temp = num
                while temp + 1 in nums_set:
                    streak +=1
                    temp +=1
                if streak > longest:
                    longest = streak
        return longest