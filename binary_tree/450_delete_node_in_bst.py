# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def deleteNode(self, root, key):
        """
        :type root: TreeNode
        :type key: int
        :rtype: TreeNode
        """
        parent = None
        node = root
        while node and node.val != key:
            if key > node.val:
                parent = node
                node = node.right
            else:
                parent = node
                node = node.left

        if not node:
            return root

        if not node.left:
            root = self.transplant(root, parent, node, node.right)
        elif not node.right:
            root = self.transplant(root, parent, node, node.left)
        else:
            succ = node.right
            succ_parent = node
            while succ.left:
                succ_parent = succ
                succ = succ.left
            if succ_parent != node:
                self.transplant(root, succ_parent, succ, succ.right)
                succ.right = node.right
            root = self.transplant(root, parent, node, succ)
            succ.left = node.left
        return root

    def transplant(self, root, parent, node, replace):
        if not parent:
            root = replace
        elif node == parent.left:
            parent.left = replace
        else:
            parent.right = replace
        return root
