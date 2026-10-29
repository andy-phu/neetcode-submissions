class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        map_t, map_s = {}, {}

        for el in s:
            map_s[el] = map_s.get(el, 0) +1
        for el in t:
            map_t[el] = map_t.get(el, 0) +1

        return map_t == map_s