# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        columns = {}  
        min_col = max_col = 0  
        
        def traverse(node, row, col):
            nonlocal min_col, max_col
            
            if node is None:
                return
            
            if col in columns:
                columns[col].append((row, node.val))  
            else:
                columns[col] = [(row, node.val)]  
            
            min_col = min(min_col, col)
            max_col = max(max_col, col)  
            
            traverse(node.left, row + 1, col - 1)  
            traverse(node.right, row + 1, col + 1) 
        
        traverse(root, 0, 0)
        
        result = []
        for col in range(min_col, max_col + 1):
            result.append([val for _, val in sorted(columns[col])])
        
        return result