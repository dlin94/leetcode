class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """

        d = { "I":1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000 }

        ans = 0
        i = 0
        while i < len(s):
            # If the next numeral is greater than current, then apply subtractive notation
            if i != len(s) - 1 and d[s[i+1]] > d[s[i]]:
                ans += d[s[i+1]] - d[s[i]]
                i += 1
            else:
                ans += d[s[i]]
            i+= 1

        return ans
