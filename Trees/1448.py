'''
Given a binary tree root, a node X in the tree is named good if in the path from
root to X there are no nodes with a value greater than X.

Return the number of good nodes in the binary tree.
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        # Perform DFS to traverse through the tree path by path, keeping track
        # of the maximum value reached along the path
        def dfs(root, max_so_far):
            if not root:
                return 0
            # Check the left and right subtrees for good nodes, updating the maximum
            # if the current node has a higher value
            l = dfs(root.left, max(max_so_far, root.val))
            r = dfs(root.right, max(max_so_far, root.val))
            ans = l + r
            # Check if the current node is a good node
            if root.val >= max_so_far:
                ans += 1
            return ans

        return dfs(root, float("-inf"))