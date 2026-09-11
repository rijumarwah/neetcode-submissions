# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(node, max_so_far):
            if not node:
                return 0

            # check and count if value is good
            if node.val >= max_so_far:
                good = 1
            else:
                good = 0

            # Update maximum seen on the path
            max_so_far = max(max_so_far, node.val)
            
            # Each dfs() returns the number of good nodes in that subtree.
            # Explore left and right:
            return good + dfs(node.left, max_so_far) + dfs(node.right, max_so_far)
        
        return dfs(root, root.val)