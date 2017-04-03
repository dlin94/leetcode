# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import deque
class Solution(object):
    def findBottomLeftValue(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        queue = deque()
        queue.append(root)
        left = root.val
        while len(queue) > 0:
            curr = queue.popleft()

            if curr.right:
                left = curr.right.val
                queue.append(curr.right)
            if curr.left:
                left = curr.left.val
                queue.append(curr.left)
        return left
