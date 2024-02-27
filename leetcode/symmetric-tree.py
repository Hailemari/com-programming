# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        
        def helper(left_node, right_node):
            if not left_node and not right_node:
                return True
            if not left_node and right_node:
               return False
            
            if not right_node and left_node:
                return False
            
            if right_node.val != left_node.val:
                return False
            
            if not helper(left_node.left, right_node.right):
                return False
            if not helper(left_node.right, right_node.left):
                return False

            return True
        return helper(root.left, root.right)