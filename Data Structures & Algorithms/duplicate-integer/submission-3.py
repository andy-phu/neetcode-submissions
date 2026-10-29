class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen = set()

        for el in nums:
            if el not in seen:
                seen.add(el)
            elif el in seen:
                return True
        return False