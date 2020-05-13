def repeatedSubstringPattern(s: str) -> bool:
    # return s in (s+s)[1:-1]
    # i, k, m = 0, -1, len(s)
    # pnext = [-1] * m
    # while i < m-1:
    #     if k==-1 or s[i]==s[k]:
    #         i, k = i+1, k+1
    #         pnext[i]=k
    #         # print(pnext[i], "--1")
    #     else:
    #         k = pnext[k]
    #         # print(k, "...2")
    # print(pnext)
    # return pnext[-1] >= 0 and m % (m - 1 - pnext[-1]) == 0
    n = len(s)
    next = [-1] * n
    for i in range(1,n):
        j = next[i-1]
        while j >= 0 and s[j+1] != s[i]:
            j = next[j]
        if s[j+1] == s[i]:
            next[i] = j + 1
    print(next)
    return next[-1] >= 0 and n % (n - 1 - next[-1]) == 0      


s1 = "aaac"
print(repeatedSubstringPattern(s1)) 