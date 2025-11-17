#
# @lc app=leetcode.cn id=37 lang=python3
# @lcpr version=30304
#
# [37] 解数独
#

# @lc code=start
class Solution:
    def solveSudoku(self, board):
        """
        解决数独问题

        Args:
            board: List[List[str]] - 9x9的数独棋盘，空格用'.'表示

        Returns:
            void - 直接修改传入的board，原地解决问题
        """

        # 使用三个数组来记录行、列、3x3宫格中数字的使用情况
        # rows[i]表示第i行中数字的使用情况，用位掩码表示
        # cols[j]表示第j列中数字的使用情况，用位掩码表示
        # boxes[k]表示第k个3x3宫格中数字的使用情况，用位掩码表示
        rows = [0] * 9
        cols = [0] * 9
        boxes = [0] * 9

        # 记录所有空格的位置，用于后续回溯
        empty_cells = []

        # 初始化：遍历整个棋盘，记录已有数字的信息和空格位置
        for i in range(9):
            for j in range(9):
                if board[i][j] != '.':
                    # 将字符数字转换为整数（1-9）
                    num = int(board[i][j])
                    # 计算对应的位掩码位置（0-8对应1-9）
                    bit = 1 << (num - 1)

                    # 计算对应的3x3宫格索引
                    # 宫格按从左到右、从上到下的顺序编号（0-8）
                    box_index = (i // 3) * 3 + (j // 3)

                    # 更新行、列、宫格的位掩码
                    rows[i] |= bit
                    cols[j] |= bit
                    boxes[box_index] |= bit
                else:
                    # 记录空格位置
                    empty_cells.append((i, j))

        def backtrack(index):
            """
            回溯函数，尝试填充第index个空格

            Args:
                index: int - 当前要处理的空格在empty_cells中的索引

            Returns:
                bool - 是否找到有效解
            """
            # 基本情况：所有空格都已填充完成
            if index == len(empty_cells):
                return True

            # 获取当前要填充的空格位置
            row, col = empty_cells[index]

            # 计算对应的3x3宫格索引
            box_index = (row // 3) * 3 + (col // 3)

            # 计算当前位置可以使用的数字的位掩码
            # ~(rows[row] | cols[col] | boxes[box_index]) 得到所有可用数字的位掩码
            # & 0x1FF 保留低9位（对应数字1-9）
            available = ~(rows[row] | cols[col] | boxes[box_index]) & 0x1FF

            # 尝试所有可能的数字（1-9）
            while available:
                # 获取最低位的1，表示可用的最小数字
                bit = available & -available
                # 从位掩码计算出对应的数字
                num = (bit.bit_length() - 1) + 1

                # 尝试将数字num填入当前位置
                board[row][col] = str(num)

                # 更新行、列、宫格的使用状态
                rows[row] |= bit
                cols[col] |= bit
                boxes[box_index] |= bit

                # 递归处理下一个空格
                if backtrack(index + 1):
                    return True

                # 如果递归失败，回溯：撤销刚才的填充
                # 恢复board状态
                board[row][col] = '.'
                # 恢复行、列、宫格的使用状态
                rows[row] ^= bit
                cols[col] ^= bit
                boxes[box_index] ^= bit

                # 移除已经尝试过的数字位，继续尝试下一个可用数字
                available ^= bit

            # 所有数字都尝试过，都无效，返回False
            return False

        # 从第一个空格开始回溯
        backtrack(0)
        
# @lc code=end



#
# @lcpr case=start
# [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]\n
# @lcpr case=end

#

