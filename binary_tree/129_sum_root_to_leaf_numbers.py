# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        paths = self.get_paths(root)
        ans = 0
        for path in paths:
            num = ""
            for x in path:
                num += str(x)
            ans += int(num)
        return ans

    def get_paths(self, root):
        if not root:
            return []
        elif not root.right and not root.left:
            return [[root.val]]
        else:
            left = self.get_paths(root.left)
            if len(left) > 0:
                for l in left:
                    l.insert(0, root.val)
            right = self.get_paths(root.right)
            if len(right) > 0:
                for r in right:
                    r.insert(0, root.val)
            return left + right
