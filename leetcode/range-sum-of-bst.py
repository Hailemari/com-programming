# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        range_sum = 0
        def helper(node):
            nonlocal range_sum
            if not node:
                return
            if low <= node.val <= high:
                range_sum += node.val

            if node.val > low:
                helper(node.left)
            if node.val < high:
                helper(node.right)

        helper(root)

        return range_sum