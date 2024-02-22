# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        def helper(root, ans):
            if root:
                left = helper(root.left, ans + 1)
                right = helper(root.right, ans + 1)
                ans = max(left, right)
                
            return ans

        return helper(root, 0)

        