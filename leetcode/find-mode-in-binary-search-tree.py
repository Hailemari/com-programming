# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        ans = defaultdict(int)
        def helper(node):
            nonlocal ans
            if not node:
                return            
            ans[node.val] += 1
            helper(node.left)
            helper(node.right)

        helper(root)

        max_value = max(ans.values())
        
        res = []
        for key, value in ans.items():
            if value == max_value:
                res.append(key)
        
        return res