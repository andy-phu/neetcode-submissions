class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0 
        res = 0

        if s != "":
            res = 1 

        for r in range(1, len(s)):
            print("eatch iteration " + s[r])
            if s[r] in s[l:r]:
                #shift over the l until r is gone
                #and remove each thing that is iterated over   
                while s[r] in s[l:r]:
                    l += 1
                print(s[l])
            else:
                res = max(res, r-l+1)

        return res
        
