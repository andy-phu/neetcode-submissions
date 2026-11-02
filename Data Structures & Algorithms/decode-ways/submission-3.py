class Solution:
    def numDecodings(self, s: str) -> int:
        """
        "123"
          l
    r

        two paths
        - take the current shift l and r 1 to the right
        - go next and combine if the current i is between 1 and 2 shift r 
        - if the size of l and r is already at 2 then just take the current dont combine 
            - shift l and r to r+1
        - base case is when r is equal to the len of s return 1

        226
         l 
           r
        ways = 1
    
        """
        def valid(i):
            lNum = int(s[i])
            if i+1 >= len(s):
                return False
                
            rNum = int(s[i+1])
            if lNum == 1 and rNum <= 9:
                return True
            elif lNum == 2 and rNum <= 6:
                return True
            else:
                return False 
        cache = {}
        def dfs(i):
            if i in cache:
                return cache[i]
            if i >= len(s):
                return 1
            elif s[i] == "0":
                return 0
            
            ways = dfs(i+1) 
            if valid(i):
                ways += dfs(i+2)
            cache[i] = ways
            return ways 

        return dfs(0)
            