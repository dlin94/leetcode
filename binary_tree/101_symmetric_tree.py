# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True

        self.flip(root.left)
        return self.is_same(root.left, root.right)

    def flip(self, root):
        if not root:
            return

        self.flip(root.left)
        self.flip(root.right)
        root.left, root.right = root.right, root.left

    def is_same(self, a, b):
        if not a and not b:
            return True
        elif not a or not b:
            return False
        elif a.val != b.val:
            return False
        else:
            return self.is_same(a.left, b.left) and self.is_same(a.right, b.right)
