#
# @lc app=leetcode.cn id=10 lang=python3
# @lcpr version=30304
#
# [10] 正则表达式匹配
#

# @lc code=start
def findMedianSortedArrays(nums1, nums2):
    """
    Find the median of two sorted arrays
    Time Complexity: O(log(min(m, n)))
    Space Complexity: O(1)

    Using binary search to solve this problem
    """
    # Ensure nums1 is the shorter array
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


class Solution:
    def isMatch(self, s, p):
        """
        Regular Expression Matching with '.' and '*'
        Time Complexity: O(m * n)
        Space Complexity: O(m * n)

        '.' matches any single character
        '*' matches zero or more of the preceding element
        """
        m, n = len(s), len(p)

        # dp[i][j] represents if s[:i] matches p[:j]
        dp = [[False] * (n + 1) for _ in range(m + 1)]

        # Empty string matches empty pattern
        dp[0][0] = True

        # Handle patterns like a*, a*b*, a*b*c* that can match empty string
        for j in range(2, n + 1):
            if p[j - 1] == '*':
                dp[0][j] = dp[0][j - 2]

        # Fill the DP table
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if p[j - 1] == '.' or p[j - 1] == s[i - 1]:
                    # Direct match or '.' wildcard
                    dp[i][j] = dp[i - 1][j - 1]
                elif p[j - 1] == '*':
                    # '*' can match zero of the preceding element
                    dp[i][j] = dp[i][j - 2]
                    # '*' can match one or more of the preceding element
                    if p[j - 2] == '.' or p[j - 2] == s[i - 1]:
                        dp[i][j] = dp[i][j] or dp[i - 1][j]
                else:
                    # No match
                    dp[i][j] = False

        return dp[m][n]


def isMatch(s, p):
    """
    Helper function for standalone testing
    """
    solution = Solution()
    return solution.isMatch(s, p)      
# @lc code=end



#
# @lcpr case=start
# "aa"\n"a"\n
# @lcpr case=end

# @lcpr case=start
# "aa"\n"a*"\n
# @lcpr case=end

# @lcpr case=start
# "ab"\n".*"\n
# @lcpr case=end

#

