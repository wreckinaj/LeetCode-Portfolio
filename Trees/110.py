'''
Given a binary tree, determine if it is height-balanced.
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def check_balance(root):
            # Ignore checking the balance if node is null
            if not root:
                return 0
            # Both subtrees must satisfy being balanced
            left = check_balance(root.left)
            right = check_balance(root.right)
            # The tree is not balanced if the left and right subtrees are not
            # balanced, or if the heights of the subtrees differ by more than
            # one
            if left == -1 or right == -1 or abs(left - right) > 1:
                return -1
            # Return the subtree height, plus one for the extra edge for the next
            # level up
            return max(left, right) + 1

        return check_balance(root) != -1