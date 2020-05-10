def mySqrt(x: int) -> int:
    left = 0
    right = x // 2 + 1
    while right > left:
        mid = left + (right - left + 1)//2 
        print(mid)
        q = mid *mid
        if q > x:
                right = mid - 1
        else:
            left = mid
    return left


print(mySqrt(0))