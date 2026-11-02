class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [False] * (len(s) + 1)

        dp[-1] = True


        for i in range(len(dp)-2, -1,-1):
            for word in wordDict:
                if i + len(word) > len(s):
                    continue
                word_at_index = s[i:i+len(word)]
                if word_at_index == word and dp[i+len(word)]:
                    dp[i] = True
        return dp[0]