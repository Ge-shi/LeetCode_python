def reverseWords(s: str) -> str:
    """
    def reversr(s: str) -> str:
        s = list(s)
        # print(''.join(reversed(s)))
        return ''.join(reversed(s))    
    n = len(s)
    j = 0
    t = ""
    for i in range(n):
        if s[i] == ' ':
            # print(i)
            t += (reversr(s[j:i]) + " ")
            j = i + 1
    t += reversr(s[j:])
    return t
    """
    return ' '.join(s.split(' ')[::-1])[::-1]


str1 = "Let's take LeetCode contest"
# print(str1[0:5][::-1])
print(reverseWords(str1))