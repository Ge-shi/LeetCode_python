def lengthOfLongestSubstring(s: str) -> int:
    """滑动窗口"""
    st = set()
    lenth = 0
    left = 0
    cnt = 0
    for i in range(0,len(s)):
        while s[i] in st:
            st.remove(s[left])
            left += 1
            cnt = i - left + 1
        else:
            st.add(s[i])
            cnt = i - left +1
        if lenth < cnt:
            lenth = cnt
    return lenth
    # st = {}
    #     i, ans = 0, 0
    #     for j in range(len(s)):
    #         if s[j] in st:
    #             i = max(st[s[j]], i)
    #         ans = max(ans, j - i + 1)
    #         st[s[j]] = j + 1
    #     return ans;