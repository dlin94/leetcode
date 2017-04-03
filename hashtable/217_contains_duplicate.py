class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if len(nums) < 2:
            return False

        s = set()
        for x in nums:
            if x in s:
                return True
            else:
                s.add(x)
        return False
