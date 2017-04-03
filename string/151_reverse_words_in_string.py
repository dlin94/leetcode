class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        slist = [x for x in s.split(" ") if x != ""]
        for i in range(0, len(slist)//2):
            slist[i], slist[-i-1] = slist[-i-1], slist[i]

        return " ".join(slist)
