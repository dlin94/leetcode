class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        s = set(nums1)
        ans = []
        for x in nums2:
            if x in s and x not in ans:
                ans.append(x)
        return ans
