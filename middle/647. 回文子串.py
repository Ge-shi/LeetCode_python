def countSubstrings(s: str) -> int:
    res = 0
    n = len(s)
    for i in range(2*n - 1):
        left = i // 2
        right = left + i % 2
        while left >= 0 and right < n and s[left] == s[right]:
            left -= 1
            right += 1
            res += 1
    return res 


print(countSubstrings("aaa"))