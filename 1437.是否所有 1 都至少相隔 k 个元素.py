#
# @lc app=leetcode.cn id=1437 lang=python3
# @lcpr version=30304
#
# [1437] 是否所有 1 都至少相隔 k 个元素
#

# @lc code=start
class Solution:
    def kLengthApart(self, nums, k):
        """
        检查所有1是否至少相隔k个元素

        Args:
            nums: List[int] - 由0和1组成的数组
            k: int - 最小间隔距离

        Returns:
            bool - 所有1是否至少相隔k个元素
        """
        # 记录上一个1的位置，初始化为-None表示还没有遇到1
        last_one = None

        # 遍历数组
        for i, num in enumerate(nums):
            if num == 1:
                if last_one is not None:
                    # 计算当前1与前一个1之间的距离
                    distance = i - last_one - 1
                    # 如果距离小于k，说明不满足条件
                    if distance < k:
                        return False
                # 更新上一个1的位置
                last_one = i

        # 所有检查都通过，返回true
        return True   
# @lc code=end



#
# @lcpr case=start
# [1,0,0,0,1,0,0,1]\n2\n
# @lcpr case=end

# @lcpr case=start
# [1,0,0,1,0,1]\n2\n
# @lcpr case=end

#

