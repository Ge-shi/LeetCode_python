def reverseStr(s: str, k: int) -> str:
    # m = len(s)
    # s = list(s)
    # l = 0
    # while m > 2 * k:
    #     print(s[l:l+k])
    #     s[l:l + k] = reversed(s[l:l+k])
    #     print(s[l:l+k])
    #     m -= 2*k
    #     l += 2 * k
    # if m < k and m > 0:
    #     s[l:] = reversed(s[l:])
    # if m >= k:
    #     s[l:l+k] = reversed(s[l:l+k])
    # return "".join(s)
    result =''
    for i in range(0,len(s),2*k):
        tmp=s[i:i+k]
        tmp=tmp[::-1]+s[i+k:i+2*k]
        result += tmp
    return result


s = "abcdefg"
k = 2
print(reverseStr(s, k))