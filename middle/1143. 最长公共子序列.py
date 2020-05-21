def longestCommonSubsequence(text1: str, text2: str) -> int:
    m = len(text1)
    n = len(text2)
    # res = 0
    dp = [[0 for _ in range(n + 1)] for _ in range(m + 1)]
    # print(dp)
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            # print(i,j)
            if text1[i - 1] == text2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
    return dp[m][n] 
    # i, j = 0, 0
    # res = 0
    # while i < m and j < n:
    #     if text1.count(text2[j]) != 0:
    #         if text1[i] == text2[j]:
    #             i += 1
    #             j += 1
    #             res += 1
    #         else:
    #             i += 1
    #     else:
    #         j += 1
    # return res


text1 = "abcde"
text2 = "actydje" 
print(longestCommonSubsequence(text1, text2))
