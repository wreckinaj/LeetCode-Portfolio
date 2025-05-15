'''
Given the root of a binary tree, return the length of the diameter of the tree.

The diameter of a binary tree is the length of the longest path between any two
nodes in a tree. This path may or may not pass through the root.

The length of a path between two nodes is represented by the number of edges
between them.
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # Update class variable as we traverse through the tree
        self.res = 0

        # Use DFS to traverse through the tree
        def dfs(root):
            # Handle empty nodes (nodes that do not exist)
            if not root:
                return 0
            # Find diameter of left and right subtrees
            left_diameter = dfs(root.left)
            right_diameter = dfs(root.right)
            # Change stored answer if adding the diameters of both subtrees produces
            # a larger value
            self.res = max(self.res, left_diameter + right_diameter)
            # Return the diameter of the tree as the maximum of the left and right
            # diameters, plus 1 to account for the edge
            # connected the max subtree (not needed for root of tree)
            return 1 + max(left_diameter, right_diameter)

        dfs(root)
        return self.res