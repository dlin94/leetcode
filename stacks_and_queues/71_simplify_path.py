class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        # split into a list
        # push onto stack if it is a named directory
        # ignore if period or null string
        # pop from stack if ..
        split = path.split("/")
        stack = []
        for x in split:
            if stack and x == "..":
                stack.pop()

            if x and x != "." and x != "..":
                stack.append(x)

        return "/" + "/".join(stack)
