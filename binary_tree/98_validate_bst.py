# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
import sys
class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """

        return self.isValid(root)

    def isValid(self, root, mini=-sys.maxsize, maxi=sys.maxsize):
        if not root:
            return True
        if not root.left and not root.right:
            return True

        if not root.right and root.left.val > mini and root.left.val < root.val:
            return self.isValid(root.left, mini, root.val)
        elif not root.left and root.right.val > root.val and root.right.val < maxi:
            return self.isValid(root.right, root.val, maxi)
        elif root.left and root.right:
            if root.left.val > mini and root.left.val < root.val and root.right.val > root.val and root.right.val < maxi:
                return self.isValid(root.left, mini, root.val) and self.isValid(root.right, root.val, maxi)
            else:
                return False
        else:
            return False
