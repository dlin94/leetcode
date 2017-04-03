class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if strs == []:
            return ""

        min = None
        for string in strs:
            if min == None:
                min = len(string)
            else:
                if min > len(string):
                    min = len(string)
        prefix = ""
        for i in range(0, min):
            for string in strs:
                if len(prefix) == i:
                    prefix += string[i]
                else:
                    if prefix[i] != string[i]:
                        prefix = prefix[:-1]
                        return prefix
        return prefix
