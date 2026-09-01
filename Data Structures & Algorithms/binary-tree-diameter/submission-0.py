# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    # the recursive function returns height, while diameter keeps track 
    # of the  best left + right seen anywhere.
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.diameter = 0

        # Calc height
        def dfs(curr):
            if not curr:
                return 0

            left = dfs(curr.left)
            right = dfs(curr.right)

            # Update the max diameter 
            self.diameter = max(self.diameter, left + right)
            
            # Return height
            return max(left, right) + 1

        dfs(root)
        return self.diameter