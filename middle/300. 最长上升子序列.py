def lengthOfLIS(nums: list) -> int:
    n = len(nums)
    if n == 0:
        return 0
    ans = [1]
    for i in range(1, n):
        res = 1
        for j in range(0, i):
            if nums[j] < nums[i]:
                res = max(res, ans[j] + 1)
        ans.append(res)
    return max(ans)