def reverse(self, x: int) -> int:
    # pos = False
    # if x > 0:
    #     pos = True
    # st = str(abs(x))
    # st=[i for i in st]
    # st.reverse()
    # st="".join(st)
    # if pos == False: 
    #     st = -int(st)
    # else:
    #     st = int(st) 
    # if st < -2**31 or st > 2**31 - 1:
    #     return 0
    # else:
    #     return st
    res = 0
    t = abs(x)
    while t != 0:
        t, y = divmod(x, 10)
        if res > 2147483647 // 10 or (res == 2147483647 // 10 and y > 7):
            return 0
        res = res * 10 + y
    if x > 0:
        return res
    else:
        if res <= 2147483648:
            return -res
        else:
            return 0