def nthUglyNumber(n: int) -> int:
    dp = [0] * n
    dp[0] = 1
    a, b, c = 0, 0, 0
    for i in range(1,n):
        dp[i] = min(dp[a]*2, dp[b]*3, dp[c]*5)
        if dp[i] == dp[a]*2 :
            a += 1
        if dp[i] == dp[b]*3:
            b += 1
        if dp[i] == dp[c]*5:
            c += 1
    return dp[-1]