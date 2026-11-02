class Solution:
    def longestPalindrome(self, s: str) -> str:
        longest = ""
        
        for i in range(len(s)):
            counter = 0
            l,r = i, i

            while l >= 0 and  r < len(s) and s[l] == s[r]:
                if r-l+1 > len(longest):
                    longest = s[l:r+1]

                l -= 1
                r += 1
                
                if l < 0 or r >= len(s) or s[l] != s[r]:
                    break
                
            

            l,r = i, i+1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if r-l+1 > len(longest):
                    longest = s[l:r+1]
                # print(i,l,r)

                l -= 1
                r += 1
                if l < 0 or r >= len(s) or s[l] != s[r]:
                    break
            

        return longest 


            

            