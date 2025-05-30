'''
Given the root of a binary tree, invert the tree, and return its root.
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # Use for the case where a node does not exist, which is a sign to backtrack
        if not root:
            return root
        # Invert left and right subtrees first
        self.invertTree(root.left)
        self.invertTree(root.right)
        # then swap roots of left and right subtrees
        root.left, root.right = root.right, root.left
        return root