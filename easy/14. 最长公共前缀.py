def longestCommonPrefix(strs: list) -> str:
    if len(strs) == 0:
        return ""
    if len(strs)==1:
        return strs[0]
    ans = strs[0]
    for i in range(1, len(strs)):
        j = 0
        while j<len(ans) and j<len(strs[i]):
            if ans[j] != strs[i][j]:
                break 
            j += 1
        ans = "".join(ans[0:j])
        if ans == "":
            return ans
    return ans 


def longestCommonPrefix2(strs: list) -> str:
    """水平扫描法"""
    if len(strs) == 0:
        return ''
    s = strs[0]
    for i in range(1, len(strs)):
        while strs[i].find(s) != 0 :
            s = s[:-1]
    return s

def longestCommonPrefix3(strs: list) -> str:
    """垂直扫描法"""
    if len(strs) == 0:
        return ''
    for i in range(len(strs[0])):
        c = strs[0][i]
        for j in range(1,len(strs)):
            if i == len(strs[j]) or strs[j][i] != c:
                return strs[0][0:i]
    return strs[0]

def longestCommonPrefix4(strs: list) -> str:
    ans = ""
    for i in zip(*strs):
        if len(set(i))==1:
            ans += i[0]
        else:
            break
    return ans


strs = ["flower","flow","flight"]
print(longestCommonPrefix(strs))