# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        def bfs(curr):
            if not root:
                return []
            result = []
            queue = deque([root])

            while queue:
                level_size = len(queue)
                current_level = []

                for _ in range(level_size):
                    curr_node = queue.popleft()
                    current_level.append(curr_node.val)

                    if curr_node.left:
                        queue.append(curr_node.left)
                    if curr_node.right:
                        queue.append(curr_node.right)

                result.append(current_level[-1])

            return result

        return bfs(root)
