class Solution(object):
    def findPairs(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        if k < 0:
            return 0

        d = { }

        for num in nums:
            if num not in d:
                d[num] = 1
            else:
                d[num] += 1

        count = 0
        for key in d:
            if k == 0:
                if d[key] > 1:
                    count += 1
            else:
                if key - k in d:
                    count += 1
        return count
