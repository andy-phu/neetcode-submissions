class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        """
        - two choices per index 
        1. take the current coint 
        2. take the next coin 

        brute force try all the combinations and update the res if we find a smaller amt of coins 

        """
        cache = {}
        def backtrack(total):
            if total == amount: 
                return 0 
            if total in cache:
                return cache[total]
            
                
            res = float('inf')

            for coin in coins: 
                if total + coin <= amount: 
                    res = min(res, 1 + backtrack(total + coin)) 

            cache[total] = res 
            return res 

        res = backtrack(0)
    
        return res if res != float('inf') else -1 
        


            

