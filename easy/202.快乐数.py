def isHappy(n: int) -> bool:
    s = {1}
    while n not in s:
        s.add(n)
        cnt = 0
        while n > 0:
            n, dig = divmod(n, 10)
            cnt += dig ** 2
        n = cnt
    return n == 1