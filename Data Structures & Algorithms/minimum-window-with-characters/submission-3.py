class Solution:
    def minWindow(self, s: str, t: str) -> str:
        tMap = collections.defaultdict(int)
        sMap = collections.defaultdict(int)

        for c in t:
            tMap[c] += 1
            sMap[c] = 0
        
        l = 0 
        res = ""
        have, need = 0, len(tMap)


        for r in range(len(s)):
            c = s[r]
            if c in sMap:
                sMap[c] += 1
            
                if sMap[c] == tMap[c]:
                    have += 1
            
            while have == need:
                print(sMap)
                print(tMap)
                temp = s[l:r+1]
                if res == "":
                    res = temp
                elif len(res) > len(temp):
                    res = temp
                
                if s[l] in t:
                    sMap[s[l]] -= 1
                    if sMap[s[l]] < tMap[s[l]]:
                        have -= 1
                    
                l+=1

        return res