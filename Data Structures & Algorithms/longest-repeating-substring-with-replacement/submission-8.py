

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        #iterate through each char 
        #if the char to the right is not the same to the left decrement k and continue 
        #keep going until k is 0 and get the length 
        #then increment l and continue again from there 

        maxf = 0 
        l = 0 
        count = collections.defaultdict(int)

        for r in range(len(s)):
            count[s[r]] += 1

            maxf = max(maxf, count[s[r]])

            if (r-l+1) - maxf > k:
                count[s[l]] -= 1
                l+=1 
            
        
        return (r-l+1)