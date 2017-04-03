class Solution(object):
    def find132pattern(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if len(nums) < 3:
            return False

        mini = None
        maxi = None
        stack = []
        for x in nums:
            if stack:
                if x > stack[-1][1]:
                    stack.pop()
                if stack and x > stack[-1][0]:
                    for i in range(len(stack)-1, -1, -1):
                        if x > stack[i][0] and x < stack[i][1]:
                            return True

            if mini is None or x < mini:
                mini = x
                maxi = None
            elif maxi is None or x > maxi:
                maxi = x
                stack.append((mini, maxi))
        return False
