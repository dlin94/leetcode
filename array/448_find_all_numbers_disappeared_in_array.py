class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        s = set([x for x in range(1, len(nums)+1)])
        for x in nums:
            if x in s:
                s.remove(x)
        return [x for x in s]
