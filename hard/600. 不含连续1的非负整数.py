def findIntegers(num: int) -> int:
    def helper(n: int) -> int:
        if n <= 0: return 1
        if n == 1: return 2
        a, b, c = 1, 2, 3
        i = n - 2
        while i:
            a = b
            b = c
            c = a + b
            i -= 1
        return c
    if num == 0:
        return 1
    if num == 1:
        return 2
    nbits = len(bin(num)) - 2
    if num >>(nbits - 2) == 3:
        return helper(nbits)
    else:
        mask = (1<<(nbits - 1)) - 1
        return helper(nbits - 1) + findIntegers(num & mask)
            

print(findIntegers(5))