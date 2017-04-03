class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ret = {}
        for x in nums:
            if x in ret:
                ret.pop(x)
            else:
                ret[x]=1
        for key in ret:
            return key
