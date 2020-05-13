def strStr(haystack: str, needle: str) -> int:
    # if needle == "":
    #     return 0
    # if haystack == "":
    #     return -1
    # l1 = len(haystack)
    # l2 = len(needle)
    # if l2 > l1:
    #     return -1
    # s = l1 - l2 + 1
    # for i in range(s):
    #     if haystack[i:i+l2] == needle:
    #         return i
    # return -1
    """KMP"""
    if needle == "":
        return 0
    """generate pnext"""
    i, k, m = 0, -1, len(needle)
    pnext = [-1] * m
    while i < m-1:
        if k==-1 or needle[i]==needle[k]:
            i, k = i+1, k+1
            pnext[i]=k
            # print(pnext[i], "--1")
        else:
            k = pnext[k]
            # print(k, "...2")
    print(pnext)
    """matching"""
    h, j =0, 0
    n = len(haystack)
    while h < m and j < n:
        if h == -1 or needle[h] == haystack[j]:
            h, j = h + 1, j + 1
        else:
            h = pnext[h]
    if h == m:
        return j - h
    return -1


strs = "abcdabdabcdabcdabd"
strs2 = "abcdabd"
print(strStr(strs, strs2))