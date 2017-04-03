class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n == 1:
            return True
        binary = bin(n)
        return binary.count("1") == 1 and binary[2] == "1"
