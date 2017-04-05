class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        if n == 0:
            return 0
        val = [0 for i in range(n)]
        for i in range(n):
            if i == 0:
                val[i] = nums[i]
            elif i == 1:
                val[i] = max(nums[i], nums[i-1])
            else:
                val[i] = max(val[i-2] + nums[i], val[i-1])
        return val[n-1]
