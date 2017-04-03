class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        self.quicksort(nums, 0, len(nums)-1)

    def quicksort(self, nums, low, high):
        if low < high:
            pivot = self.partition(nums, low, high)
            self.quicksort(nums, low, pivot - 1)
            self.quicksort(nums, pivot + 1, high)

    def partition(self, nums, low, high):
        x = nums[high]
        i = low - 1
        for j in range(low, high):
            if nums[j] <= x:
                i += 1
                nums[i], nums[j] = nums[j], nums[i]
        nums[i+1], nums[high] = nums[high], nums[i+1]
        return i + 1
