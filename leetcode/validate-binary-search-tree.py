# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        def checkBST(root, ans):
            if root:
                checkBST(root.left, ans)
                ans.append(root.val)
                checkBST(root.right, ans)
            else:
                return

            
          
            return ans
            
        ans = checkBST(root, [])
        for i in range(1, len(ans)):
            if ans[i] <= ans[i - 1]:
                return False

        return True
        