class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0
        best = 0 
        for r in range(1, len(prices)):
            if prices[l] < prices[r]:
                best = max(best, prices[r]-prices[l])
            else:
                l = r

        return best 


        