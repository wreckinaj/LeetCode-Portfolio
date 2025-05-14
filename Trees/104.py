'''
Given the root of a binary tree, return its maximum depth.

A binary tree's maximum depth is the number of nodes along the longest path
from the root node down to the farthest leaf node.
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        # Use the recursive DFS algorithm to get the depth of each subtree, then take
        # the maximum depth
        d1 = self.maxDepth(root.left)
        d2 = self.maxDepth(root.right)
        return max(d1, d2) + 1