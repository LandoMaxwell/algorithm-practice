def setZeroes(matrix):
    """
    矩阵置零 - LeetCode #73 - 中等
    原地算法，时间复杂度: O(m*n)，空间复杂度: O(1)
    """
    m, n = len(matrix), len(matrix[0])
    first_row_zero = any(matrix[0][j] == 0 for j in range(n))
    first_col_zero = any(matrix[i][0] == 0 for i in range(m))
    for i in range(1, m):
        for j in range(1, n):
            if matrix[i][j] == 0:
                matrix[i][0] = 0
                matrix[0][j] = 0
    for i in range(1, m):
        for j in range(1, n):
            if matrix[i][0] == 0 or matrix[0][j] == 0:
                matrix[i][j] = 0
    if first_row_zero:
        for j in range(n):
            matrix[0][j] = 0
    if first_col_zero:
        for i in range(m):
            matrix[i][0] = 0


if __name__ == "__main__":
    matrix = [[1,1,1],[1,0,1],[1,1,1]]
    setZeroes(matrix)
    print(matrix)  # [[1,0,1],[0,0,0],[1,0,1]]
