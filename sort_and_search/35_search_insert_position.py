class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if len(nums) == 0:
            return 0

        high = len(nums)-1
        low = 0
        while low<=high:
            mid = (low+high)//2
            if nums[mid] == target:
                return mid
            elif low == high:
                if target > nums[low]:
                    return low+1
                else:
                    return low
            elif nums[mid] < target:
                low = mid + 1

            else:
                high = mid - 1
        return mid
