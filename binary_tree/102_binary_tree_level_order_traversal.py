# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import deque
class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []

        queue = deque()
        queue.append(root)
        start = 1
        prev_end = 1
        end = 1
        i = 0
        level = []
        ans = []
        while len(queue) > 0:
            curr = queue.popleft()
            i += 1
            level.append(curr.val)
            if curr.left:
                queue.append(curr.left)
                end += 1
            if curr.right:
                queue.append(curr.right)
                end += 1
            if i == prev_end:
                ans.append(level)
                level = []
                prev_end = end
        return ans
