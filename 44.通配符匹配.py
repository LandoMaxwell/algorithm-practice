#
# @lc app=leetcode.cn id=44 lang=python3
# @lcpr version=30304
#
# [44] 通配符匹配
#

# @lc code=start
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        """
        通配符匹配

        Args:
            s: str - 输入字符串
            p: str - 字符模式

        Returns:
            bool - 是否匹配
        """
        m, n = len(s), len(p)

        # dp[i][j] 表示 s 的前 i 个字符和 p 的前 j 个字符是否匹配
        dp = [[False] * (n + 1) for _ in range(m + 1)]

        # 空字符串匹配空模式
        dp[0][0] = True

        # 处理空字符串和连续的 '*'
        for j in range(1, n + 1):
            if p[j - 1] == '*':
                dp[0][j] = dp[0][j - 1]

        # 填充 dp 表
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if p[j - 1] == '*':
                    # '*' 可以匹配空字符 (dp[i][j-1]) 或匹配一个或多个字符 (dp[i-1][j])
                    dp[i][j] = dp[i][j - 1] or dp[i - 1][j]
                elif p[j - 1] == '?' or s[i - 1] == p[j - 1]:
                    # '?' 匹配任意单个字符，或字符完全匹配
                    dp[i][j] = dp[i - 1][j - 1]
                # 其他情况 dp[i][j] 保持 False

        return dp[m][n]

# @lc code=end



#
# @lcpr case=start
# "aa"\n"a"\n
# @lcpr case=end

# @lcpr case=start
# "aa"\n"*"\n
# @lcpr case=end

# @lcpr case=start
# "cb"\n"?a"\n
# @lcpr case=end

#

