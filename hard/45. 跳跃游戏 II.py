def jump(nums) -> int:
    n = len(nums)
    ans = 0
    end = 0
    farst = 0
    for i in range(n - 1):
        farst = max(farst, nums[i] + i)
        if i == end:
            ans += 1
            end = farst
    return ans