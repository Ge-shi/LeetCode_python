def isPalindrome(s: str) -> bool:
    res = ""
    for lt in s:
        if (lt >= '0' and lt <='9'):
            res += lt
        if lt >= 'A' and lt <= 'Z':
            lt = lt.lower()
        if lt >= 'a' and lt <='z':
            res += lt
    print(res)
    return res == res[::-1]


st = "676767cxhu--.gygygUY09-po,."
print(isPalindrome(st))