class Solution:
    def wordBreak(self, s: str, wordDict: list) -> bool:
        n = len(s)
        dp = [False for _ in range(n + 1)]
        dp[0] = True 
        for i in range(n):
            if dp[i]:
                for j in range(i + 1, n + 1):
                    if s[i:j] in wordDict:
                        dp[j] = True
        return dp[-1]