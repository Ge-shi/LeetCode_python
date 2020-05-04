def checkIfCanBreak(s1: str, s2: str) -> bool:
    str1 = "".join(sorted(s1))
    str2 = "".join(sorted(s2))
    if str2 > str1:
        str1, str2 = str2, str1
    for i in range(len(s1)):
        if str1[i] < str2[i]:
            return False
    return True


ans = checkIfCanBreak("leetcodee", "interview")
print(ans)
