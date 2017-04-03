class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        i = len(digits)-1
        digits[i] += 1
        while digits[i] == 10:
            digits[i] = 0
            if i == 0:
                digits.insert(0,1)
                break
            digits[i-1] += 1
            i -= 1
        return digits
