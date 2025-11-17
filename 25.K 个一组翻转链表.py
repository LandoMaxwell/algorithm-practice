#
# @lc app=leetcode.cn id=25 lang=python3
# @lcpr version=30304
#
# [25] K 个一组翻转链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


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

    def mergeKLists(self, lists):
        """
        Merge K Sorted Lists
        Time Complexity: O(N log K) where N is total nodes, K is number of lists
        Space Complexity: O(K) for the priority queue

        Using min-heap approach to efficiently merge K sorted linked lists
        """
        import heapq

        # Create a min-heap to store (value, list_index, node)
        min_heap = []

        # Add the head of each non-empty list to the heap
        for i, lst in enumerate(lists):
            if lst:
                heapq.heappush(min_heap, (lst.val, i, lst))

        # Create a dummy node to serve as the head of the result list
        dummy = ListNode(0)
        current = dummy

        # Process the heap until it's empty
        while min_heap:
            val, list_idx, node = heapq.heappop(min_heap)

            # Add the node to the result list
            current.next = node
            current = current.next

            # Move to the next node in the same list
            if node.next:
                heapq.heappush(min_heap, (node.next.val, list_idx, node.next))

        return dummy.next

    def reverseKGroup(self, head, k):
        """
        Reverse Nodes in k-Group
        Time Complexity: O(N) where N is the number of nodes
        Space Complexity: O(1) for the iterative approach

        Reverses nodes of the linked list in groups of size k
        """
        if k <= 1 or not head:
            return head

        # Helper function to check if there are k nodes remaining
        def hasKNodes(node, k):
            count = 0
            while node and count < k:
                node = node.next
                count += 1
            return count == k

        # Helper function to reverse k nodes starting from given node
        def reverseKNodes(start, k):
            prev = None
            current = start
            count = 0

            # Reverse exactly k nodes
            while current and count < k:
                next_node = current.next
                current.next = prev
                prev = current
                current = next_node
                count += 1

            # prev is now the new head of the reversed portion
            # current is the next node to process
            return prev, current

        # Dummy node to handle the case where we need to reverse from the head
        dummy = ListNode(0)
        dummy.next = head
        prev_group = dummy

        while prev_group.next and hasKNodes(prev_group.next, k):
            # The first node of the current group
            group_start = prev_group.next

            # Reverse k nodes
            reversed_head, next_node = reverseKNodes(group_start, k)

            # Connect the reversed group back to the list
            prev_group.next = reversed_head
            group_start.next = next_node

            # Move prev_group to the end of the reversed group
            prev_group = group_start

        return dummy.next   
# @lc code=end



#
# @lcpr case=start
# [1,2,3,4,5]\n2\n
# @lcpr case=end

# @lcpr case=start
# [1,2,3,4,5]\n3\n
# @lcpr case=end

#

