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
        :rtype: List[List[int]]
        """
        # idea: make another method use an answer array as an argument
        if not root:
            return []
        elif root.val == sum and not root.right and not root.left:
            return [[root.val]]
        else:
            left = self.pathSum(root.left, sum - root.val)
            if len(left) > 0:
                for l in left:
                    l.insert(0, root.val)
            right = self.pathSum(root.right, sum - root.val)
            if len(right) > 0:
                for r in right:
                    r.insert(0, root.val)
            return left + right
