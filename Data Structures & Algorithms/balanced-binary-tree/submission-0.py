# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        # Idea: dfs() returns height if tree is balanced
        # but returns - 1 if tree is unbalanced, use this.

        def dfs(curr):
            if not curr:
                return 0 

            # If not balanced - left
            left = dfs(curr.left)
            if left == -1:
                return - 1
            
            # If not balanced - right
            right = dfs(curr.right)
            if right == -1:
                return -1

            # If balanced but difference larger than 1
            if abs(left - right) > 1:
                return - 1

            # How tall is the tree? - add +1 for current node
            return max(left, right) + 1

        if dfs(root) != -1:
            return True
        else:
            return False
