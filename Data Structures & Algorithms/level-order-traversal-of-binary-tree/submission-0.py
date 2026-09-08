# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        def bfs(root):
            if not root:
                return []

            result = []
            # initialize queue with root node
            queue = deque([root])

            while queue:
                level_size = len(queue)
                current_level = []

                # process all nodes present at current level 
                for _ in range(level_size):
                    curr_node = queue.popleft()
                    current_level.append(curr_node.val)

                    # enqueue left child if it exists
                    if curr_node.left:
                        queue.append(curr_node.left)

                    # enqueue right child if it exists
                    if curr_node.right:
                        queue.append(curr_node.right)

                result.append(current_level)

            return result

        return bfs(root)
