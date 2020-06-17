def countCharacters(words: list, chars: str) -> int:
    ans = 0
    for elem in words:
        # print(elem)
        for i in range(len(elem)):
            if elem.count(elem[i]) > chars.count(elem[i]):
                break
        if i == len(elem) - 1 and elem.count(elem[i]) <= chars.count(elem[i]):
            ans += len(elem)
        # print(i)
    return ans