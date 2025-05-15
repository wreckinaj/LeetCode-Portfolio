'''
Given the roots of two binary trees root and subRoot, return true if there is
a subtree of root with the same structure and node values of subRoot and false
otherwise.

A subtree of a binary tree tree is a tree that consists of a node in tree and all
of this node's descendants. The tree tree could also be considered as a subtree of
itself.
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # We serialize the tree (and its subtrees), and compare the preorder
        # traversals of each tree.
        def ser(node):
            # Character for empty node
            if not node:
                return ',#'
            # Add value for current node, and recurse through left and right
            # subtrees
            else:
                return ',' + str(node.val) + ser(node.left) + ser(node.right)
        # The second tree is a subtree of the first if the preorder traveral of
        # the second tree is entirely part of the first with no gaps.
        return ser(subRoot) in ser(root)
            