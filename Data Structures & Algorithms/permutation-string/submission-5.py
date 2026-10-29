class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        """
        want = a:1 b:1 c:1
        have = c:1 a:1 b:1 -> return true



        - when have == want: return true
        - when have does not equal want shift l and r to the right by 1 and update our have and want 
        - if l is in have decrement the count and add the new r if the r is in want
        
        """

        want = {}
        have = {}

        for c in s1:
            if c not in want:
                want[c] = 1
            else: 
                want[c] += 1

        if len(s1) > len(s2):
            return False
        
        for i in range(len(s1)):
            if s2[i] in want:
                if s2[i] not in have:
                    have[s2[i]] = 1
                else:
                    have[s2[i]] += 1

        if have == want:
            return True
        
        l = 0

        for r in range(len(s1), len(s2)):
            if s2[l] in have: 
                have[s2[l]] -= 1
                if have[s2[l]] == 0:
                    del have[s2[l]]

            l += 1
            if s2[r] in want: 
                if s2[r] not in have:
                    have[s2[r]] = 1
                else:
                    have[s2[r]] += 1
            if have == want:
                return True

        return False

             

