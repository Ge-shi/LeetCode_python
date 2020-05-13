def longestPalindrome(s: str) -> str:
    leng = len(s)
    if leng < 2:
        return s
    #dp = [[1] * leng] * leng
    dp = [[False for _ in range(leng)] for _ in range(leng)]
    ans = 1
    start = 0
    for i in range(leng):
        dp[i][i] = True
    for j in range(1, leng):
        for i in range(j):
            if s[i] == s[j]:
                if j - i < 3:
                    dp[i][j] = True
                else:
                    dp[i][j] = dp[i+1][j-1]
            else:
                dp[i][j] = False
            if dp[i][j]:
                if ans < j - i + 1:
                    ans = j - i + 1
                    start = i
    return s[start:ans+start]


s = "abcdcbabcd"
print(longestPalindrome(s))