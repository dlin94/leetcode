class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        n = len(nums)
        if n < 2:
            return False

        d = { }
        for i in range(0, n):
            x = nums[i]
            if x in d:
                for y in d[x]:
                    if abs(i - y) <= k:
                        return True
                d[x].append(i)
            else:
                d[x] = [i]

        return False
