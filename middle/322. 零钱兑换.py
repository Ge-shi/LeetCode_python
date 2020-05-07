def coinChange(coins: list, amount: int) -> int:
    # n = len(coins)
    # coins.sort(reverse= True)
    # print(coins)
    # ans = 0
    # j = amount
    # for i in range(n):
    #     t, j = divmod(j, coins[i])
    #     ans += t
    #     print(t, j, ans)
    # if j != 0:
    #     ans = -1
    # return ans
    
    f = [float('inf')] * (amount + 1)
    f[0] = 0
    for c in coins:
        for j in range(c, amount + 1):
            f[j] = min(f[j], f[j - c] + 1)
    return f[amount] if f[amount] != float('inf') else -1


coins = [186,79,83,89]
amount = 6249
print(coinChange(coins, amount))