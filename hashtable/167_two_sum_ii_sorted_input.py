class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        ht = { }

        for i in range(0, len(numbers)):
            if numbers[i] in ht:
                return [ht[numbers[i]]+1, i+1]
            else:
                ht[target - numbers[i]] = i
