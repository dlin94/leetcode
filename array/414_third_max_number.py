class Solution(object):
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) < 3:
            return max(nums)

        s = set(nums)
        if len(s) < 3:
            return max(s)

        m1 = None
        m2 = None
        m3 = None
        for x in s:
            if x > m1:
                m1, m2, m3 = x, m1, m2
            elif x < m1 and x > m2:
                m2, m3 = x, m2
            elif x < m2 and x > m3:
                m3 = x
        return m3
