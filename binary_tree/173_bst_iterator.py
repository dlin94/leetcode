# Definition for a  binary tree node
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class BSTIterator(object):
    def __init__(self, root):
        """
        :type root: TreeNode
        """
        self.nxt = -1
        self.nodes = []
        stack = [root]
        node = root
        while stack:
            while node:
                node = node.left
                stack.append(node)
            node = stack.pop()
            if node:
                self.nodes.append(node.val)
                node = node.right
                stack.append(node)


    def hasNext(self):
        """
        :rtype: bool
        """
        return self.nxt+1 <= len(self.nodes)-1

    def next(self):
        """
        :rtype: int
        """
        try:
            self.nxt += 1
            return self.nodes[self.nxt]
        except:
            return None


# Your BSTIterator will be called like this:
# i, v = BSTIterator(root), []
# while i.hasNext(): v.append(i.next())
