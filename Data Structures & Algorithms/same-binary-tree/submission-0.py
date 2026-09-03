# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # Trees empty / not empty cases
        if not p and not q:
            return True

        if not p and q:
            return False

        if p and not q:
            return False

        # Values are different
        if p.val != q.val:
            return False

        # Compare left sides and right sides
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)