class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        val = []
        for i in range(n):
            if i == 0:
                val.append(1)
            elif i == 1:
                val.append(2)
            else:
                val.append(val[-1] + val[-2])

        return val[-1]
