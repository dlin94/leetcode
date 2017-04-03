class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        n, m = len(s), len(p)
        if m > n:
            return []

        hp = [0] * 123
        hs = [0] * 123

        for x in p:
            hp[ord(x)] += 1

        ans = []
        for i in range(0, n-m+1):
            if i == 0:
                for x in s[i:i+m]:
                    hs[ord(x)] += 1
            else:
                hs[ord(s[i-1])] -= 1
                hs[ord(s[i+m-1])] += 1

            if hs == hp:
                ans.append(i)
        return ans
