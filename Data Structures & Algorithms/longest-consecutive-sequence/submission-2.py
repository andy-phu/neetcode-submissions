class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        longest = 0
        for n in nums:
            if n-1 not in nums_set:
                streak = 0
                while (n+streak) in nums_set:
                    streak+=1
                if streak > longest:
                    longest = streak
        return longest
