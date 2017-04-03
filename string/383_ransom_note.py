from collections import Counter
class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        c = Counter(magazine)
        for x in ransomNote:
            if x in c:
                if c[x] > 0:
                    c[x] -= 1
                else:
                    return False
            else:
                return False
        return True
