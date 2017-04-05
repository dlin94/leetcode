#https://leetcode.com/problems/counting-bits/?tab=Description
class Solution(object):
    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        pow2 = 2
        val = []
        i = 0
        while i < num+1:
            if i == pow2:
                pow2 *= 2
                j = 0
                while i < num+1 and i < pow2:
                    val.append(val[j] + 1)
                    j += 1
                    i += 1
            elif i == 0 or i == 1:
                val.append(i)
                i += 1

        return val
