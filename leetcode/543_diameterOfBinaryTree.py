# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        if not root: return 0

        def calc(node, n=0):
            if not node: return 0
            if n == 0:
                return calc(node.left) + calc(node.right)
            if node.left and node.right:
                return max(1 + calc(node.left, n+1), 1 + calc(node.right, n+1))
            if node.left:
                return 1 + calc(node.left, n+1)
            if node.right:
                return 1 + calc(node.left, n+1)

            return 0

        return calc(root)