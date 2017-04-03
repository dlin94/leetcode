class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        sum_s = 0
        for char in s:
            sum_s += ord(char)
        sum_t = 0
        for char in t:
            sum_t += ord(char)
        return chr(sum_t - sum_s)
