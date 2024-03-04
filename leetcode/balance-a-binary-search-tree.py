# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        res = []

        def dfs(root):
            if not root:
                return

            dfs(root.left)
            res.append(root)
            dfs(root.right)  
        
        dfs(root)

        def helper(res):
            if not res:
                return None
            mid = len(res) // 2
            root = res[mid]
            root.left = helper(res[:mid])
            root.right = helper(res[mid+1:])
            
            return root
        return helper(res)