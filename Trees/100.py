'''
Given the roots of two binary trees p and q, write a function to check if they
are the same or not.

Two binary trees are considered the same if they are structurally identical, and
the nodes have the same value.
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def isSameSubtree(p, q):
            # No need to check if both nodes do not exist
            if not p and not q:
                return 0
            # Not the same tree if there is an extra node or node in the wrong
            # place, or if the nodes are not equal
            if ((not p) and q) or (p and (not q)) or p.val != q.val:
                return -1
            # We must check the subtrees as well
            left = isSameSubtree(p.left, q.left)
            right = isSameSubtree(p.right, q.right)
            # If any subtree is not the same, then the entire tree is not the same
            if left == -1 or right == -1:
                return -1
            else:
                return 0
        
        return isSameSubtree(p, q) != -1