# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        ans = []
        stack = [root]
        node = root
        while stack:
            while node:
                node = node.left
                stack.append(node)
            node = stack.pop()
            if node:
                ans.append(node.val)
                node = node.right
                stack.append(node)
        return ans
