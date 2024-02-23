# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        
        def check(node1, node2, ans):
            if node1 and not node2:
                ans[0] = False
            if not node1 and node2:
                ans[0] = False

            if node1 and node2:
                if node1.val == node2.val:
                    check(node1.left, node2.left, ans)
                    check(node1.right, node2.right, ans)
                else:
                    ans[0] = False

            return ans[0]

        return check(p, q, [True])