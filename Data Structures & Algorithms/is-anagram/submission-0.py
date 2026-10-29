class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        count_s, count_t = {}, {}

        for el in s:
            if el not in count_s:
                count_s[el] = 0
            else:
                count_s[el] += 1
        
        for el in t:
            if el not in count_t:
                count_t[el] = 0
            else:
                count_t[el] += 1
        
        return count_s == count_t
