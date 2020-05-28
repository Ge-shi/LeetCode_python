def isLongPressedName(name: str, typed: str) -> bool:
    n, m = len(name), len(typed)
    i = j = 0
    if name[i] != typed[j]:
        return False
    while i < n and j < m:
        if name[i] == typed[j]:
            i += 1
            j += 1
        else:
            if typed[j] != typed[j - 1]:
                return False
            j += 1
    if i < n:
        return False
    for r in range(j, m):
        if typed[r] != name[-1]:
            return False
    return True


name = "leelee"
typed = "lleeelee"
print(isLongPressedName(name, typed))