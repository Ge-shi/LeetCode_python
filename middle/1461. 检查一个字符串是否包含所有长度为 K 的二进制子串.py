def hasAllCodes(s: str, k: int) -> bool:
    n = len(s)
    st = set()
    for i in range(n - k + 1):
        st.add(s[i:i+k])
        print(st)
    return len(st) == 2**k


s = "00110"
k = 2
print(hasAllCodes(s,k))