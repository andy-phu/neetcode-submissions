class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l,r = 0, len(nums)-1

        while l <= r:
            mid = (l+r) // 2
            curr = nums[mid]
            if curr == target: 
                return mid 
            # elif nums[l] == target:
            #     return l
            # elif nums[r] == target:
            #     return r
            # elif nums[l] < target < curr:
            #     r = mid -1 
            # elif curr < target < nums[r]:
            #     l = mid + 1
            # else:
            #     l += 1

            #check if mid is on the right or left side 

            #apart of left side
            if curr > nums[r]:
                if nums[l] <= target <= curr:
                    r = mid -1 
                else:
                    l = mid + 1
            else:
                if curr <= target <= nums[r]:
                    l = mid + 1
                else:
                    r = mid - 1
        return -1