def new21Game(N: int, K: int, W: int) -> float:
    dp=[None]*(K+W)
    s=0
    for i in range(K,K+W):          # 填蓝色的格子
        dp[i] = 1 if i<=N else 0
        s+=dp[i]
    for i in range(K-1,-1,-1):      # 填橘黄色格子
        dp[i]=s/W
        s=s-dp[i+W]+dp[i]
    return dp[0]