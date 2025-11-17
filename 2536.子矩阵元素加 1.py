#
# @lc app=leetcode.cn id=2536 lang=python3
# @lcpr version=30304
#
# [2536] 子矩阵元素加 1
#

# @lc code=start
class Solution:
    def rangeAddQueries(self, n: int, queries: List[List[int]]) -> List[List[int]]:
        diff = [[0] * (n + 1) for _ in range(n + 1)]
    
        # 处理每个查询
        for row1, col1, row2, col2 in queries:
            # 对差分数组进行标记
            diff[row1][col1] += 1
            diff[row1][col2 + 1] -= 1
            diff[row2 + 1][col1] -= 1
            diff[row2 + 1][col2 + 1] += 1
        
        # 创建结果矩阵
        result = [[0] * n for _ in range(n)]
        
        # 通过前缀和还原原矩阵
        for i in range(n):
            for j in range(n):
                # 计算当前位置的值
                if i > 0:
                    diff[i][j] += diff[i-1][j]
                if j > 0:
                    diff[i][j] += diff[i][j-1]
                if i > 0 and j > 0:
                    diff[i][j] -= diff[i-1][j-1]
                
                result[i][j] = diff[i][j]
        
        return result    
# @lc code=end



#
# @lcpr case=start
# 3\n[[1,1,2,2],[0,0,1,1]]\n
# @lcpr case=end

# @lcpr case=start
# 2\n[[0,0,1,1]]\n
# @lcpr case=end

#

