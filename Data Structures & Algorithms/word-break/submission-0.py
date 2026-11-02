class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        """
        "neetcode", wordDict = ["neet","code"]
         i
        

        check from i to i + len(word) if the word equals the word in the wordDict

        if i reaches the end of s return True

        basically for each dfs we iterate throughout the word dict and see if we can go down that path
        
        
        """

        cache = {}
        def dfs(i):
            if i in cache:
                return cache[i]
            if i >= len(s):
                return True

            
            for word in wordDict:
                word_in_string = s[i:i + len(word)]

                if word_in_string == word:
                    if dfs(i+len(word)):
                        cache[i] = True
                        return True

            cache[i] = False 
            return False 


        return dfs(0)





        