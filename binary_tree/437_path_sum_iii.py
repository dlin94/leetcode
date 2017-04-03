# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: int
        """
        return self.path_sum(root, sum, True)

    def path_sum(self, root, sum, cont): # cont indicates if we should pass both the sum and sum - root.val or just sum - root.val
        if not root:
            return 0
        else:
            # We shouldn't pass on the subtracted sums
            s = self.path_sum(root.left, sum - root.val, False) + \
                self.path_sum(root.right, sum - root.val, False)
            if cont:
                # But we should pass on the main sum (i.e., the sum given in pathSum())
                s += self.path_sum(root.left, sum, True) + \
                     self.path_sum(root.right, sum, True)

            if root.val == sum:
                return 1+s
            else:
                return s
