def longestPalindromeSubseq(s: str) -> int:
    """递归实现（超时）
    size = len(s)
    if size == 0:
        return 0
    if size == 1:
        return 1
    if s[0] == s[size - 1]:
        return longestPalindromeSubseq(s[1:size - 1]) + 2
    else:
        return max(longestPalindromeSubseq(s[1:size]), longestPalindromeSubseq(s[0:size - 1]))
    """
    size = len(s)
    dp = [[0 for _ in range(size)] for _ in range(size)]
    # print(size)
    for j in range(size):
        dp[j][j] = 1
        # print(j)
        for i in range(j - 1, -1 , -1):
            if s[i] == s[j]:
                dp[i][j] = dp[i + 1][j - 1] + 2
            else:
                dp[i][j] = max(dp[i + 1][j], dp[i][j - 1])
    return dp[0][size - 1]



a = "euazbipzncptldueeuechubrcourfpftcebikrxhybkymimgvldiwqvkszfycvqyvtiwfckexmowcxztkfyzqovbtmzpxojfofbvwnncajvrvdbvjhcrameamcfmcoxryjukhpljwszknhiypvyskmsujkuggpztltpgoczafmfelahqwjbhxtjmebnymdyxoeodqmvkxittxjnlltmoobsgzdfhismogqfpfhvqnxeuosjqqalvwhsidgiavcatjjgeztrjuoixxxoznklcxolgpuktirmduxdywwlbikaqkqajzbsjvdgjcnbtfksqhquiwnwflkldgdrqrnwmshdpykicozfowmumzeuznolmgjlltypyufpzjpuvucmesnnrwppheizkapovoloneaxpfinaontwtdqsdvzmqlgkdxlbeguackbdkftzbnynmcejtwudocemcfnuzbttcoew"
print(longestPalindromeSubseq(a))