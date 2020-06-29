def replaceSpace(s: str) -> str:
    # return s.replace(" ", "%20")
    res = []
    for c in s:
        if c == " ":
            res.append("%20")
        else:
            res.append(c)
    return "".join(res)


st = ""
print(replaceSpace(st))