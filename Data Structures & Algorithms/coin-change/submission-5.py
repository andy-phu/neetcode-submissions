class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        """
        
        [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 1, 2,-1]
        [0, 1, 2, 3, 4, 5, 6, 7, 8, 9,10,11,12]
        
        - make a dp array of amount + 1 
        - index 0 should be 0 minimum coins and for each coin in coins initialize their value in dp as 1
        - go left to right and for the index you're on subtract all values to the left that are not -1 to get the value and if the value is in the index and not -1 then update the current dp index with the minimum amt you were able to find

        """

        dp = [float('inf')] * (amount + 1)

        dp[0] = 0
    
        for i in range(1, len(dp)):
            for j in coins:
                if i < j or j > amount:
                    continue
                
                diff = dp[i - j]
                dp[i] = min(diff + 1, dp[i])

        if dp[amount] == float('inf'):
            return -1
        else:
            return dp[amount]
