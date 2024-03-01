# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxSumBST(self, root: Optional[TreeNode]) -> int:
        max_sum = 0

        def dfs(node):
            nonlocal max_sum
            if not node:
                return True, 0, float('inf'), float('-inf')
            
            is_bst_left, sum_left, min_left, max_left = dfs(node.left)
            is_bst_right, sum_right, min_right, max_right = dfs(node.right)

            if is_bst_left and is_bst_right and max_left < node.val < min_right:
                sum_of_keys = sum_left + sum_right + node.val
                max_sum = max(max_sum, sum_of_keys)
                return True, sum_of_keys, min(min_left, node.val), max(max_right, node.val)
            else:
                return False, 0, 0, 0

        dfs(root)

        return max_sum