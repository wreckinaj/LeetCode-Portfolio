'''
Given a binary tree, find the lowest common ancestor (LCA) of two given nodes
in the tree.

According to the definition of LCA on Wikipedia: “The lowest common ancestor is
defined between two nodes p and q as the lowest node in T that has both p and q
as descendants (where we allow a node to be a descendant of itself).”
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # Null node cannot count
        if not root:
            return None
        # Handle case where the current node is a target node, as the answer cannot be
        # below the current node
        if root == p or root == q:
            return root
        # Perform DFS by checking the left and right subtrees for the LCA
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        # If a target node is in the left subtree and the other is in the right, the
        # current node is the LCA
        if left and right:
            return root
        # Get the LCA from the left subtree
        if left:
            return left
        # Get the LCA from the right subtree
        return right