class Solution(object):
    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        str_list = str.split(" ")
        if len(pattern) != len(str_list):
            return False
        dict = { }
        s = set()
        for i in range(0, len(pattern)):
            if pattern[i] in dict:
                if dict[pattern[i]] != str_list[i]:
                    return False
            elif str_list[i] in s:
                return False
            else:
                dict[pattern[i]] = str_list[i]
                s.add(str_list[i])
        return True
