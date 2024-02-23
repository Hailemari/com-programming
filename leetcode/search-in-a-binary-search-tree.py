# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:

        def preOrder(root, val):
            if root:
                if root.val == val:
                    return root
                if val < root.val:
                    return preOrder(root.left, val)
                else:
                    return preOrder(root.right, val)
            else:
                return

        return preOrder(root, val)
        