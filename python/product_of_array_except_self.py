def productExceptSelf(nums):
    """
    除自身以外数组的乘积 - LeetCode #238 - 中等
    不使用除法，时间复杂度: O(n)，空间复杂度: O(1)
    """
    n = len(nums)
    answer = [1] * n
    left_product = 1
    for i in range(n):
        answer[i] = left_product
        left_product *= nums[i]
    right_product = 1
    for i in range(n-1, -1, -1):
        answer[i] *= right_product
        right_product *= nums[i]
    return answer


if __name__ == "__main__":
    print(productExceptSelf([1, 2, 3, 4]))       # [24, 12, 8, 6]
    print(productExceptSelf([-1, 1, 0, -3, 3]))  # [0, 0, 9, 0, 0]
