class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max = 0
        curr = 0
        for num in nums:
            if num == 1:
                curr += 1
                if curr > max:
                    max = curr
            else:
                curr = 0
        return max
