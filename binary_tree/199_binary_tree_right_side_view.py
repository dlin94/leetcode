# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []

        if not root.right:
            return [root.val] + self.rightSideView(root.left)
        else:
            left = self.rightSideView(root.left)
            right = self.rightSideView(root.right)

            if len(left) > len(right):
                diff = len(left) - len(right)
                right += left[-diff:]
            return [root.val] + right
