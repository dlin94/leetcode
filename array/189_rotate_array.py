class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k = k % len(nums)

        # Method #1
        for i in range(0, k):
            x = nums.pop()
            nums.insert(0, x)

        # Brute-force Method
        #pos = 0
        #for i in range(n-k, n):
        #    for j in range(i, pos, -1):
        #        nums[j], nums[j-1] = nums[j-1], nums[j]
        #    pos += 1
