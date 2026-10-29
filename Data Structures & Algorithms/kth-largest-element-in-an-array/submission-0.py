class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heapq.heapify(nums)
        #1 2 4 5 
        while len(nums) > k:
            heapq.heappop(nums)

        return nums[0]