def validPalindrome(s: str) -> bool:
    def isPalindome(st: str) -> bool:
        return st == st[::-1]
    m = 0
    n = len(s) - 1
    while m < n and s[m] == s[n]:
        m += 1
        n -= 1
    return isPalindome(s[m: n + 1]) or isPalindome(s[m : n])

st = "abcda"
print(validPalindrome(st))