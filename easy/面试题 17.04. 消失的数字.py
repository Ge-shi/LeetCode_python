def missingNumber(nums: list) -> int:
    n = len(nums)
    for i in range(n):
        if nums.count(i) == 0:
            return i
    return n

def missingNumber2(nums: list) -> int:
    n = len(nums)
    total = sum(nums)
    return ((n+1)*n) // 2 - total


def missingNumber3(nums: list) -> int:
    n = len(nums)
    res = 0
    for i in range(n):
        res ^= nums[i]
        res ^= i
    res ^= n
    return res


list1 = [8, 6, 4, 2, 3, 5, 7, 0, 1]
print(missingNumber3(list1))