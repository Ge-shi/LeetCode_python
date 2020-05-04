def maxDiff(num) -> int:
    st1 = str(num)
    ind1 = ''
    k = -1
    for i in range(len(st1)):
        if st1[i] != '9':
            ind1 = st1[i]
            k = 1
            break
    if k == -1:
        temp = st1
    else:
        temp = st1.replace(ind1, '9')
    print(k, temp)
    # return int(temp)
    temp2 = st1
    if st1[0] != '1':
        ind1 = st1[0]
        temp2 = st1.replace(ind1, '1')
    else:
        k = -1
        for c in st1:
            if c == '1':
                continue
            elif c != '0':
                k = 1
                ind1 = c
                break
        if k == 1:
            temp2 = st1.replace(ind1, '0')
        else:
            temp2 = st1
    print(temp2)
    return int(temp) - int(temp2)


print(maxDiff(1101057))
