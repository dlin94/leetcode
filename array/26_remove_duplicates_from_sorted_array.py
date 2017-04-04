class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        curr = None
        n = len(nums)
        i = 0
        loops = 0
        while loops < n:
            if nums[i] == curr:
                del nums[i]
            else:
                curr = nums[i]
                i += 1
            loops += 1
        return len(nums)
