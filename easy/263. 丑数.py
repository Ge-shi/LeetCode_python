def isUgly(num: int) -> bool:
    if num == 0:
        return False
    nums = [2,3,5]
    i = 0
    while i <= 2:
        if num % nums[i] == 0:
            num = num // nums[i]
        else:
            i += 1
    if num == 1:
        return True
    else:
        return False