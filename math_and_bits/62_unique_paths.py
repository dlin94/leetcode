import math
class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        k = (m - 1) + (n - 1)
        return math.factorial(k)/(math.factorial(n-1)*math.factorial(m-1))
