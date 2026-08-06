def firstMissingPositive(nums):
    """
    找出未排序数组中缺失的最小正整数
    LeetCode #41 - 困难
    时间复杂度: O(n)，空间复杂度: O(1)
    """
    n = len(nums)
    for i in range(n):
        if nums[i] <= 0 or nums[i] > n:
            nums[i] = n + 1
    for i in range(n):
        num = abs(nums[i])
        if num <= n:
            if nums[num - 1] > 0:
                nums[num - 1] = -nums[num - 1]
    for i in range(n):
        if nums[i] > 0:
            return i + 1
    return n + 1


if __name__ == "__main__":
    print(firstMissingPositive([1, 2, 0]))       # 3
    print(firstMissingPositive([3, 4, -1, 1]))   # 2
    print(firstMissingPositive([7, 8, 9, 11, 12]))  # 1
