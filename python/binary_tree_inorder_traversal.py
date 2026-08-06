from typing import List, Optional

# Definition for a binary tree node.
class TreeNode:
    """二叉树节点类"""
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    """二叉树中序遍历解决方案"""
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        """
        递归方法实现中序遍历
        中序遍历顺序：左子树 -> 根节点 -> 右子树
        时间复杂度: O(n)，空间复杂度: O(n)
        """
        result = []
        def inorder(node):
            if not node:
                return
            inorder(node.left)
            result.append(node.val)
            inorder(node.right)
        inorder(root)
        return result


if __name__ == "__main__":
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    print(Solution().inorderTraversal(root))  # [4, 2, 5, 1, 3]
