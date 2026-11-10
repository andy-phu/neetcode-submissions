import math

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        """
        
        - go from 1 to max(piles)
        - calculate the amt of hours it takes using the banana/hr rate
        - the first one with the amt of hrs <= h then that's the answer
        
        
        
        """

        max_banana_rate = max(piles)
        arr = []

        def calculate_hours(rate):
            hours = 0
            for banana_amt in piles:
                hours += math.ceil(banana_amt / rate)

            return hours <= h

        l,r = 1, max_banana_rate
        final_rate = max_banana_rate 

        while l <= r:
            mid = (r+l) // 2

            if calculate_hours(mid):
                final_rate = min(final_rate, mid)
                r = mid - 1
            else:
                l = mid + 1 

        return final_rate 



            



