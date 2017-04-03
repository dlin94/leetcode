class Solution(object):
    def isPowerOfFour(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num == 1:
            return True

        binary = bin(num)
        return binary.count("1") == 1 and binary[2] == "1" and len(binary) % 2 == 1
