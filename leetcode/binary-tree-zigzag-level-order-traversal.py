# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        count = defaultdict(list)
        
        def helper(node, row):
            nonlocal count

            if not node:
                return
            count[row].append(node.val)
            
            helper(node.left, row + 1)
            helper(node.right, row + 1)

        helper(root, 0)

        ans = []
        for key, val in count.items():
            if key % 2:
                ans.append(reversed(val))
            else:
                ans.append(val)
        

        return ans
