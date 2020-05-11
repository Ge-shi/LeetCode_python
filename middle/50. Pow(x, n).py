def myPow(x: float, n: int) -> float:
    # return x**n
    ans = 1.0
    i = abs(n)
    while i != 0:
        print(i)
        if i % 2 != 0:
            ans *= x
        x *= x
        i = i // 2
    return ans if n > 0 else 1/ans


print(myPow(2.0, -2))