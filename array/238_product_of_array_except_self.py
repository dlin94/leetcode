class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        if n == 2:
            nums[0], nums[1] = nums[1], nums[0]
            return nums

        products = {}
        p = nums[n-1]
        products[(n-1,n-1)] = p
        for i in range(n-2, 0, -1):
            p *= nums[i]
            products[(i,n-1)] = p

        ans = [products[(1, n-1)]]
        products[(0,0)] = nums[0]
        for i in range(1, n):
            if i == n-1:
                p = products[(0, i-1)]
            else:
                p = products[(i+1,n-1)] * products[(0,i-1)]
            ans.append(p)
            products[(0,i)] = products[(0,i-1)] * nums[i]
        return ans
