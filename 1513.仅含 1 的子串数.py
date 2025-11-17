#
# @lc app=leetcode.cn id=1513 lang=python3
# @lcpr version=30304
#
# [1513] 仅含 1 的子串数
#

# @lc code=start
class Solution:
    def numSub(self, s: str) -> int:
        """
        计算所有字符都为 1 的子字符串的数目

        Args:
            s: 二进制字符串，仅由 '0' 和 '1' 组成

        Returns:
            int: 所有字符都为 1 的子字符串的数目，对 10^9 + 7 取模
        """
        MOD = 10**9 + 7  # 模数
        result = 0  # 结果
        current_ones = 0  # 当前连续的 '1' 的数量

        # 遍历字符串中的每个字符
        for char in s:
            if char == '1':
                # 如果当前字符是 '1'，增加连续计数
                current_ones += 1
                # 对于每个新遇到的 '1'，它可以形成 current_ones 个新的全 '1' 子字符串
                # 例如：序列 "111"，遇到第1个'1'形成1个子字符串["1"]，遇到第2个'1'形成2个新的["1", "11"]，遇到第3个'1'形成3个新的["1", "11", "111"]
                result += current_ones
                result %= MOD  # 每次都取模，防止溢出
            else:
                # 如果当前字符是 '0'，重置连续计数
                current_ones = 0

        # 返回结果（已经包含了模运算）
        return result % MOD
 
# @lc code=end



#
# @lcpr case=start
# "0110111"\n
# @lcpr case=end

# @lcpr case=start
# "101"\n
# @lcpr case=end

# @lcpr case=start
# "111111"\n
# @lcpr case=end

#

