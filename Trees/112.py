'''
Given the root of a binary tree and an integer targetSum, return true if the tree
has a root-to-leaf path such that adding up all the values along the path equals
targetSum.

A leaf is a node with no children.
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        # Use DFS to traverse through the tree and get the path to leaf sums
        def dfs(root, currVal):
            # Stop if root does not exist
            if not root:
                return False
            # Stop if root is a leaf node (no children), and see if the path sum
            # is equal to the target sum
            if root.left == None and root.right == None:
                return (currVal + root.val) == targetSum
            # Add to the current path sum
            currVal += root.val
            # See if the paths through the left and right subtrees add up
            return dfs(root.left, currVal) or dfs(root.right, currVal)

        return dfs(root, 0)