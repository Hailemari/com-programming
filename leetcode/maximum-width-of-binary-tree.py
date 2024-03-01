# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        max_width = 0
        queue = deque([[root, 0]])

        while queue:

            leftmost_position = queue[0][1]

            for _ in range(len(queue)):
                node, rightmost_position = queue.popleft()

                if node.left:
                    queue.append([node.left, 2 * rightmost_position])
                if node.right:
                    queue.append([node.right, 2 * rightmost_position + 1])

            width = rightmost_position - leftmost_position + 1

            max_width = max(max_width, width)

        return max_width