def rotate(nums, k):
    """
    轮转数组 - LeetCode #189 - 中等
    将数组中的元素向右轮转 k 个位置
    时间复杂度: O(n)，空间复杂度: O(1)
    """
    n = len(nums)
    k = k % n
    nums.reverse()
    nums[:k] = nums[:k][::-1]
    nums[k:] = nums[k:][::-1]


if __name__ == "__main__":
    nums = [1, 2, 3, 4, 5, 6, 7]
    rotate(nums, 3)
    print(nums)  # [5, 6, 7, 1, 2, 3, 4]
