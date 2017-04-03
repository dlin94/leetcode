class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        if s == "":
            return 0

        j = len(s) - 1
        while j >= 0 and not s[j].isalpha():
            j -= 1

        count = 0
        while j >= 0 and s[j].isalpha():
            count += 1
            j -= 1
        return count
