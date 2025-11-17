#
# @lc app=leetcode.cn id=41 lang=python3
# @lcpr version=30304
#
# [41] 缺失的第一个正数
#

# @lc code=start
class Solution:
    def firstMissingPositive(self, nums):
        """
        找出缺失的第一个正数

        Args:
            nums: List[int] - 未排序的整数数组

        Returns:
            int - 缺失的第一个正数
        """
        n = len(nums)

        # 第一阶段：清理数组
        # 将所有非正数和大于n的数重置为n+1
        # 因为这些数不可能是答案，也不需要标记
        for i in range(n):
            if nums[i] <= 0 or nums[i] > n:
                nums[i] = n + 1

        # 第二阶段：标记出现的数字
        # 对于每个有效的正数x（1 <= x <= n），
        # 将位置x-1的数标记为负数，表示数字x出现过
        for i in range(n):
            num = abs(nums[i])  # 使用绝对值，因为可能已经被标记为负数
            if num <= n:
                # 标记位置num-1，取负数表示已访问
                # 使用绝对值避免重复标记同一个位置
                nums[num - 1] = -abs(nums[num - 1])

        # 第三阶段：查找缺失的第一个正数
        # 第一个正数的位置+1就是答案
        for i in range(n):
            if nums[i] > 0:
                return i + 1

        # 如果所有位置都被标记（都是负数），
        # 说明1到n都出现了，答案是n+1
        return n + 1    
# @lc code=end



#
# @lcpr case=start
# [1,2,0]\n
# @lcpr case=end

# @lcpr case=start
# [3,4,-1,1]\n
# @lcpr case=end

# @lcpr case=start
# [7,8,9,11,12]\n
# @lcpr case=end

#

