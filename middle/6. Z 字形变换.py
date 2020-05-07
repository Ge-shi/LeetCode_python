def convert(s: str, numRows: int) -> str:
    n = len(s)
    ans = []
    if numRows == 1:
        return s
    # col, t = divmod(n, 2*numRows - 2)
    for i in range(numRows):
        j = 0
        k = i
        while k <= n-1:
            # print(k)
            ans.append(s[k])
            j += 1
            if i ==0 or i == numRows - 1:
                k = k + 2*(numRows-1)
            else:
                if j%2 != 0:
                    k = k + 2*(numRows-i-1)
                else:
                    k = k + 2*numRows - 2 - 2*(numRows-i-1)
    return "".join(ans)

# while i + 2*j*(numRows-i-1)<= n-1 and j <= n // (2*numRows - 2) + 1:
#             ans.append(s[i + 2*j*(numRows-i-1)])
#             print(i + 2*j*(numRows-i-1))
#             if j%2==0:
#                 j += 1

s = "LEETCODEISHIRING"
print(convert(s,3))
print("LCIRETOESIIGEDHN")
print(convert(s,4))
print("LDREOEIIECIHNTSG")