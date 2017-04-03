import collections
class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        c = collections.Counter(s)
        odd_count = 0
        ans = 0
        for x in c:
            if c[x] % 2 == 1:
                odd_count += 1
            ans += c[x]
        if odd_count >= 2:
            ans -= odd_count - 1
        return ans
