from functools import lru_cache
class Solution:
    @lru_cache(0)
    def waysToStep(self, n: int) -> int:
        a = 1
        b = 2
        c = 4
        d = 7
        if n == 2:
            return b
        if n == 3:
            return c
        if n == 4:
            return d
        for _ in range(n - 4):
            a = (b + c + d)%1000000007
            b = c
            c = d
            d = a
        return a%1000000007