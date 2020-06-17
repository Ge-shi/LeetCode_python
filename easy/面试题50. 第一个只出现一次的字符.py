def firstUniqChar(s: str) -> str:
    """
    for elem in s:
        if s.count(elem) == 1:
            return elem
    return " "
    """
    dt = {}
    for c in s:
        dt[s] = not c in dt
    for c in s:
        if dt[s]: return c
    return " "