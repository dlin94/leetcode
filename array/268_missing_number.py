class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        s = set([x for x in range (0, len(nums)+1)])
        for x in nums:
            if x in s:
                s.remove(x)
        return s.pop()
