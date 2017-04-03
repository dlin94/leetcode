class Solution(object):
    def reverseString(self, s):
        """
        :type s: str
        :rtype: str
        """
        slist = list(s)
        for i in range(len(s)//2):
            slist[i], slist[-i-1] = slist[-i-1], slist[i]
        return "".join(slist)
