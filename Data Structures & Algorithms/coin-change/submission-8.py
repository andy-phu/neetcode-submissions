class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        """
        - two choices per index 
        1. take the current coint 
        2. take the next coin 

        brute force try all the combinations and update the res if we find a smaller amt of coins 

        """
        cache = {}
        def backtrack(i, total):
            if (i, total) in cache:
                return cache[(i, total)]
            if total == amount: 
                return 0
            if i >= len(coins) or total > amount: 
                return float('inf')
                
            cache[(i, total)] =  min(1 + backtrack(i, total + coins[i]), backtrack(i+1, total))
            return cache[(i, total)]

        res = backtrack(0,0)

        return res if res != float('inf') else -1 
        


            

