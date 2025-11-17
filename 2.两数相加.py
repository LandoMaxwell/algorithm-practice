#
# @lc app=leetcode.cn id=2 lang=python3
# @lcpr version=30304
#
# [2] 两数相加
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy_head = ListNode(0)
        current = dummy_head
        carry = 0  # 进位
        
        # 遍历两个链表，直到两个链表都为空且没有进位
        while l1 is not None or l2 is not None or carry != 0:
            # 获取当前节点的值，如果链表已经遍历完则为0
            val1 = l1.val if l1 is not None else 0
            val2 = l2.val if l2 is not None else 0
            
            # 计算当前位的和以及进位
            total = val1 + val2 + carry
            carry = total // 10  # 计算进位
            digit = total % 10   # 计算当前位的数字
            
            # 创建新节点并移动current指针
            current.next = ListNode(digit)
            current = current.next
            
            # 移动l1和l2指针（如果存在）
            if l1 is not None:
                l1 = l1.next
            if l2 is not None:
                l2 = l2.next
        
        # 返回结果链表（跳过虚拟头节点）
        return dummy_head.next

# 辅助函数：将列表转换为链表
def create_linked_list(lst):
    dummy_head = ListNode(0)
    current = dummy_head
    for val in lst:
        current.next = ListNode(val)
        current = current.next
    return dummy_head.next

# 辅助函数：将链表转换为列表
def linked_list_to_list(head):
    result = []
    current = head
    while current is not None:
        result.append(current.val)
        current = current.next
    return result

# @lc code=end



#
# @lcpr case=start
# [2,4,3]\n[5,6,4]\n
# @lcpr case=end

# @lcpr case=start
# [0]\n[0]\n
# @lcpr case=end

# @lcpr case=start
# [9,9,9,9,9,9,9]\n[9,9,9,9]\n
# @lcpr case=end

#

