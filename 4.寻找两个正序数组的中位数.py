#
# @lc app=leetcode.cn id=4 lang=python3
# @lcpr version=30304
#
# [4] 寻找两个正序数组的中位数
#

# @lc code=start
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        m, n = len(nums1), len(nums2)
        left, right = 0, m

        while left <= right:
            # Partition positions in nums1 and nums2
            partition1 = (left + right) // 2
            partition2 = (m + n + 1) // 2 - partition1

            # Get elements around the partition, handle boundary cases
            maxLeft1 = float('-inf') if partition1 == 0 else nums1[partition1 - 1]
            minRight1 = float('inf') if partition1 == m else nums1[partition1]

            maxLeft2 = float('-inf') if partition2 == 0 else nums2[partition2 - 1]
            minRight2 = float('inf') if partition2 == n else nums2[partition2]

            # Check if partition is correct
            if maxLeft1 <= minRight2 and maxLeft2 <= minRight1:
                # Found the correct partition
                if (m + n) % 2 == 0:
                    # Even number of elements, take average of max left and min right
                    return (max(maxLeft1, maxLeft2) + min(minRight1, minRight2)) / 2
                else:
                    # Odd number of elements, take max of left side
                    return max(maxLeft1, maxLeft2)
            elif maxLeft1 > minRight2:
                # nums1 partition is too far right, move left
                right = partition1 - 1
            else:
                # nums1 partition is too far left, move right
                left = partition1 + 1

        raise ValueError("Input arrays are not sorted")        
# @lc code=end



#
# @lcpr case=start
# [1,3]\n[2]\n
# @lcpr case=end

# @lcpr case=start
# [1,2]\n[3,4]\n
# @lcpr case=end

#

