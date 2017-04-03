# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return 0
        if root.left == None and root.right == None:
            return 1
        elif root.right == None:
            return self.minDepth(root.left) + 1
        elif root.left == None:
            return self.minDepth(root.right) + 1
        else:
            left_min = self.minDepth(root.left) + 1
            right_min = self.minDepth(root.right) + 1
            return min(left_min, right_min)
