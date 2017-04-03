class Solution(object):
    def reverseStr(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        n = len(s)
        i = 0
        slist = list(s)
        while i < len(s):
            if n < k:
                for j in range(i, (i+len(s))/2):
                    slist[j], slist[len(s)-(j-i)-1] = slist[len(s)-(j-i)-1], slist[j]
                break
            else:
                for j in range(i, (i+i+k)/2):
                    slist[j], slist[(k+i)-(j-i)-1] = slist[(k+i)-(j-i)-1], slist[j]
                i += 2*k
                n -= 2*k

        return "".join(slist)
