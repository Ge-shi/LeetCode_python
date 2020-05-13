def isValid(s: str) -> bool:
    dc = {'(' : ')', '{' : '}', '[' : ']', '?' : '?'}
    stack = ['?']
    for c in s:
        if c in dc:
            stack.append(c)
        else:
            if c != dc[stack.pop()]:
                return False
    return len(stack) == 1