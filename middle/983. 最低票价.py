from functools import lru_cache


def mincostTickets(days: list, costs: list) -> int:

    # @lru_cache(None) # 加速
    # def dp(i):
    #     if i > days[len(days) - 1]:
    #         return 0
    #     elif i in days:
    #         return min(dp(i + 1) + costs[0], dp(i + 7) + costs[1], dp(i + 30) + costs[2])
    #     else:
    #         return dp(i + 1)
    # return dp(1)
    durations = [1, 7, 30]
    n = len(days)
    @lru_cache(None) # 加速
    def dp(i):
        if i >= n:
            return 0
        ans = 10 ** 9
        j = i
        for c, d in zip(costs, durations):
            while j < n and days[j] < days[i] + d:
                j += 1
            ans = min(ans, dp(j) + c)
        return ans
    return dp(0)


days = [1,2,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,20,21,24,25,27,28,29,30,31,34,37,38,39,41,43,44,45,47,48,49,54,57,60,62,63,66,69,70,72,74,76,78,80,81,82,83,84,85,88,89,91,93,94,97,99]
costs = [9,38,134]  
print(mincostTickets(days, costs))