def longestPalindrome(s: str) -> str:
    """
    最长回文子串 - LeetCode #5 - 中等
    使用中心扩展算法
    时间复杂度: O(n^2)，空间复杂度: O(1)
    """
    if not s:
        return ""
    start, max_len = 0, 1

    def expand(l, r):
        nonlocal start, max_len
        while l >= 0 and r < len(s) and s[l] == s[r]:
            if r - l + 1 > max_len:
                start = l
                max_len = r - l + 1
            l -= 1
            r += 1

    for i in range(len(s)):
        expand(i, i)      # 奇数长度
        expand(i, i + 1)  # 偶数长度
    return s[start:start + max_len]


if __name__ == "__main__":
    print(longestPalindrome("babad"))   # "bab"
    print(longestPalindrome("cbbd"))    # "bb"
