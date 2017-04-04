from collections import Counter
class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        ht1 = Counter(nums1)
        ht2 = Counter(nums2)
        ans = []
        for k in ht1:
            if k in ht2:
                for i in range(0, min(ht1[k], ht2[k])):
                    ans.append(k)
        return ans
