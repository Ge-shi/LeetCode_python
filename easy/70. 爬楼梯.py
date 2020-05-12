def climbStairs(n: int) -> int:
    if n==1:
        return 1
    if n==2:
        return 2
    first = 1
    second = 2
    for _ in range(3, n+1):
        ans = first + second
        first = second
        second = ans
    return ans 

print(climbStairs(45))