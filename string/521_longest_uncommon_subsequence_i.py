class Solution(object):
    def findLUSlength(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: int
        """
        if a == b:
            return -1
        elif len(b) > len(a):
            return len(b)
        else:
            return len(a)
