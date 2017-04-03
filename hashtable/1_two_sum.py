from collections import Counter
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        
        d = { }
        for i in range(0,len(nums)):
            if nums[i] in d:
                d[nums[i]].append(i)
            else:
                d[nums[i]] = [i]

        print(d)
        for i in range(0, len(nums)):
            diff = target - nums[i]
            print(diff)
            if diff in d:
                print("diff in d", diff)
                if diff == nums[i]:
                    if len(d[diff]) > 1:
                        return d[diff][0:2]
                else:
                    return [i,d[diff][0]]
        return []
