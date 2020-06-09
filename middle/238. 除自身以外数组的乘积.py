def productExceptSelf(nums: list) -> list:
    """
    res = []
    n = len(nums)
    total = 1
    for i in range(n):
        total *= nums[i]
    for i in range(n):
        res.append(total//nums[i])
    return res
    """
    n = len(nums)
    res = [1 for _ in range(n)]
    k = 1
    for i in range(n):
        res[i] = k
        k *= nums[i]
    k = 1
    for i in range(n - 1, -1, -1):
        res[i] *= k
        k *=nums[i]
    return res