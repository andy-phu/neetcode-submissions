class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        """
        - 3 pointers one pointing to each word
        - every time we come across across a new iteration we check if s1 pointer equals s3 pointer and if s2 pointer equals s3 pointer
        - 2 paths for every index in s3 
        - we return false if both paths dont go to the end and if both paths fail 
        - return true if c is equal to the length of s3
        """

        if len(s1) + len(s2) != len(s3):
            return False 
        sub = []
        dp = {}
        def backtrack(a,b,c):
            if c >= len(s3) and a >= len(s1) and b >= len(s2):
                return True  
            if (a,b) in dp:
                return dp[(a,b)]
            res = False
            if a < len(s1) and s1[a] == s3[c]:
                res = backtrack(a+1,b,c+1)
                    
            if b < len(s2) and s2[b] == s3[c]:
                res = backtrack(a,b + 1,c+1)
                    
            dp[(a,b)] = res 
            return res 

        return backtrack(0,0,0)
        