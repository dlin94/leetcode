class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        d = { }
        ans = []
        for str in strs:
            h = sum([ord(char)**5 for char in str])
            if h not in d:
                d[h] = [str]
            else:
                d[h].append(str)
        return d.values()
