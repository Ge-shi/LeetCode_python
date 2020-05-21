def longestPalindrome(s: str) -> str:
    leng = len(s)
    if leng < 2:
        return s
    #dp = [[1] * leng] * leng
    dp = [[False for _ in range(leng)] for _ in range(leng)]
    ans = 1
    start = 0
    for i in range(leng):
        dp[i][i] = True
    for j in range(1, leng):
        for i in range(j):
            if s[i] == s[j]:
                if j - i < 3:
                    dp[i][j] = True
                else:
                    dp[i][j] = dp[i+1][j-1]
            else:
                dp[i][j] = False
            if dp[i][j]:
                if ans < j - i + 1:
                    ans = j - i + 1
                    start = i
    return s[start:ans+start]


def longestPalindrome2(s: str) -> str:
    size = len(s)
    if size < 2:
        return s
    res = s[0]
    max_len = 1
    for i in range(size):
        odd_str, odd_len = __centerSpread(s, size, i, i)
        even_str, even_len = __centerSpread(s, size, i, i + 1)
        cur_maxstr = odd_str if odd_len > even_len else even_str
        if len(cur_maxstr) > max_len:
            res = cur_maxstr
            max_len = len(cur_maxstr)
    return res 


def __centerSpread(s, size, left, right):
    i = left
    j = right
    while j <= size - 1 and i >=0 and s[i] == s[j]:
        i -= 1
        j += 1
    return s[i + 1:j], j - 1 - i

s = "abcdcbabcd"
print(longestPalindrome2(s))