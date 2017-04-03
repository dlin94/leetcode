class Solution(object):
    def nextGreaterElement(self, findNums, nums):
        """
        :type findNums: List[int]
        :type nums: List[int]
        :rtype: List[int]
        """
        d = { }
        ans = []
        stack = []

        for x in nums:
            while len(stack) > 0 and stack[-1] < x:
                d[stack.pop()] = x
            stack.append(x)

        for x in findNums:
            ans.append(d.get(x, -1))

        return ans
