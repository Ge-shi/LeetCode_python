def romanToInt(s: str) -> int:
    ans = 0
    n = len(s)
    i = 0
    while i < n:
        if s[i] == 'M':
            ans += 1000
            i += 1
            continue
        if s[i] == 'D':
            ans += 500
            i += 1
            continue
        if s[i] == 'C':
            if i == n-1 or (s[i+1] != 'D' and s[i+1] != 'M'):
                ans += 100
                i += 1
                continue
            elif s[i+1] =='D':
                ans += 400
                i += 2
                continue
            elif s[i+1] == 'M':
                ans += 900
                i += 2
                continue
        if s[i] == 'L':
            ans += 50
            i += 1
            continue
        if s[i] == 'X':
            if i == n-1 or (s[i+1] != 'L' and s[i+1] != 'C'):
                print("UU")
                ans += 10
                i += 1
                continue
            elif s[i+1] =='L':
                ans += 40
                i += 2
                continue
            elif s[i+1] == 'C':
                ans += 90
                i += 2
                continue
        if s[i] == 'V':
            ans += 5
            i += 1
            continue
        if s[i] == 'I':
            if i == n-1 or (s[i+1] != 'V' and s[i+1] != 'X'):
                ans += 1
                i += 1
                continue
            elif s[i+1] =='V':
                print("V")
                ans += 4
                i += 2
                continue
            elif s[i+1] == 'X':
                print("X")
                ans += 9
                i += 2
                continue
    return ans
def romanToInt2(s: str) -> int:
    Roman2Int = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
    Int = 0
    n = len(s)

    for index in range(n - 1):
        if Roman2Int[s[index]] < Roman2Int[s[index + 1]]:
            Int -= Roman2Int[s[index]]
        else:
            Int += Roman2Int[s[index]]

    return Int + Roman2Int[s[-1]]


s = "MMCDXXV"
print(romanToInt2(s))

# for i in range(10):
#     i += 2
#     print(i)