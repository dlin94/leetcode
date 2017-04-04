class Solution(object):
    def findRepeatedDnaSequences(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        if len(s) <= 10:
            return []

        ht = { }
        ans = []
        for i in range(0, len(s) - 9):
            if s[i:i+10] in ht and ht[s[i:i+10]] == 0:
                ans.append(s[i:i+10])
                ht[s[i:i+10]] = 1
            elif s[i:i+10] not in ht:
                ht[s[i:i+10]] = 0
        return ans
